<template>
  <v-container id="grid" fluid>
    <v-row v-for="(item, row) in grid" :key="row" justify="center">
      <span
        v-for="(char, col) in item"
        :key="col"
        :class="
          char.content === ':' ||
          char.content === '|' ||
          char.background === '#fbae3c'
            ? 'grid-char-off'
            : 'grid-char'
        "
        :style="getStyle(char, row)"
      >
        {{ char.content }}
      </span>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import ansi from 'ansi-parser'
export default {
  name: 'Grid',

  props: {
    map: {
      type: String,
      default: '',
    },
  },

  computed: {
    ...mapState('app', ['dark']),

    dark() {
      return this.$vuetify.theme.dark
    },
  },

  data: () => ({
    grid: null,
    action: null,
    colors: [
      { ansi: '\u001B[35m', color: 'orchid', background: 'purple' },
      { ansi: '\u001B[34;1m', color: 'dodgerblue', background: 'blue' },
      { ansi: '\u001B[43m', color: 'inherit', background: '#fbae3c' },
    ],
  }),

  watch: {
    map(val) {
      this.formatMap(val)
    },
    dark(val) {
      this.formatMap(this.$props.map)
    },
  },

  mounted() {
    // if (!this.grid) this.$router.push({ path: this.localePath('home')});
    this.setLastAction('')
    this.setStep(0)
    this.setState(0)
    this.setReward(0)
  },

  methods: {
    ...mapMutations('play', [
      'setLastAction',
      'setState',
      'setReward',
      'setStep',
    ]),

    formatMap(map) {
      const newMap = Array(5)
        .fill()
        .map(() => [])

      const mapCharArray = map.split('')
      for (let i = 0; i !== map.length; ++i) {
        if (map[i] === '|' && (map[i - 1] === '\n' || map[i + 1] === '\n')) {
          mapCharArray[i] = '\n'
        }
      }

      const mapString = mapCharArray.join('')
      const fillVoid = mapString.replace(/ /g, '0')
      const parsedMap = ansi.parse(fillVoid.replace(/\n|[+-]/g, ''))
      const parsedTruncatedMap = parsedMap.slice(0, 45)
      if (parsedMap.length > 45) {
        const actionArray = parsedMap.slice(45, parsedMap.length)
        let actionString = ''
        for (const char of actionArray) {
          actionString += char.content
        }
        const action = actionString.substring(
          actionString.indexOf('(') + 1,
          actionString.lastIndexOf(')')
        )
        this.setLastAction(action)
      }

      for (let i = 0; i !== parsedTruncatedMap.length; ++i) {
        const { color, background } = this.getColorFromAnsi(
          parsedTruncatedMap[i].style
        )
        newMap[Math.trunc(i / 9)].push({
          content: parsedTruncatedMap[i].content,
          color,
          background,
        })
      }
      this.grid = newMap
    },

    getStyle(char, row) {
      let style = ''
      if (row === 0) {
        style = 'border-top: 10px solid grey;'
      } else if (row === 4) {
        style =
          'border-bottom: 10px solid grey;box-shadow: rgba(128, 128, 128, 0.4) 0px 5px, rgba(128, 128, 128, 0.3) 0px 10px, rgba(128, 128, 128, 0.2) 0px 15px, rgba(128, 128, 128, 0.1) 0px 20px, rgba(128, 128, 128, 0.05) 0px 25px;'
      }
      if (char.content === '0') {
        return style + `color: transparent;background-color: ${char.background}`
      } else if (char.content === '|') {
        return 'color: grey;background-color: grey;' + style
      } else {
        return (
          style + `color: ${char.color};background-color: ${char.background}`
        )
      }
    },

    getColorFromAnsi(ansi) {
      if (ansi) {
        const stylesCount = ansi.split('m').length - 1
        const styles = []
        for (const color of this.colors) {
          if (
            stylesCount === 2 &&
            (color.ansi.includes(ansi.split('m')[0]) ||
              color.ansi.includes(ansi.split('m')[1]))
          ) {
            styles.push({ color: color.color, background: color.background })
          } else if (color.ansi.includes(ansi)) {
            styles.push({ color: color.color, background: color.background })
          }
          if (styles.length === stylesCount) {
            return {
              color: styles[0].color,
              background:
                stylesCount === 2 ? styles[1].background : color.background,
            }
          }
        }
      }
      return { color: this.dark ? 'white' : 'black', background: 'inherit' }
    },
  },
}
</script>

<style lang="css" scoped>
.grid-char,
.grid-char-off {
  letter-spacing: 1.5em;
  font-family: 'Courier New', Courier, monospace;
  background-color: black;
  color: white;
  text-align: center;
  text-indent: 1.5em;
  line-height: 3em;
  font-size: 1.5em;
}
.grid-char:first-child,
.grid-char-off:first-child {
  border-left: 10px solid grey;
  /* box-shadow: rgba(0, 0, 0, 0.56) 0px 22px 70px 4px; */
}
.grid-char:last-child,
.grid-char-off:last-child {
  border-right: 10px solid grey;
  /* box-shadow: rgba(0, 0, 0, 0.56) 0px 22px 70px 4px; */
}
.grid-char:hover {
  cursor: pointer;
  background-color: silver !important;
}
</style>
