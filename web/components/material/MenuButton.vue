<template>
  <v-menu open-on-hover offset-y rounded="b-xl">
    <template #activator="{ on, attrs }">
      <v-btn
        dark
        text
        shaped
        :color="dark ? 'white' : 'black'"
        :fab="!desktop"
        :large="desktop"
        :height="desktop ? 100 : undefined"
        class="px-4 black--text text-capitalize menu-btn"
        v-bind="attrs"
        v-on="on"
      >
        <v-container v-if="desktop" fluid>
          <v-row justify="center" align="center">
            <v-col>
              <v-avatar
                :color="dark ? 'white' : 'black'"
                style="border-radius: 10px"
              >
                <v-img
                  :src="require('~/static/icon.png')"
                  :style="`background-color: ${dark ? 'white' : 'black'};`"
                />
              </v-avatar>
            </v-col>
            <v-col>
              <v-row justify="center" align="center">
                <span>
                  {{ $t('toolbar.menu') }}
                </span>
              </v-row>
            </v-col>
            <v-col>
              <v-row justify="center" align="center">
                <v-icon class="px-4">mdi-menu-down</v-icon>
              </v-row>
            </v-col>
          </v-row>
        </v-container>
        <v-icon v-else>mdi-menu</v-icon>
      </v-btn>
    </template>
    <v-list class="py-0">
      <v-list-item
        v-for="(item, index) in items"
        :key="index"
        style="height: 64px"
        @click="
          handle_function_call(
            inContext(item.context) ? item.action : item.oaction,
            !!item.args
              ? inContext(item.context)
                ? item.args[0]
                : item.args[1]
              : undefined
          )
        "
      >
        <v-list-item-title class="menu-btn-item-text text-h5 font-weight-light">
          <span class="px-4">{{ $t(item.text) }}</span>
        </v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  name: 'MenuButton',

  props: {
    items: {
      type: Array,
      default: () => [],
    },
  },

  data: () => ({
    randomName: null,
  }),

  computed: {
    dark() {
      return this.$vuetify.theme.dark
    },
    desktop() {
      return this.$vuetify.breakpoint.mdAndUp
    },
  },

  mounted() {
    this.loading = true
    this.randomName = this.randomString()
  },

  methods: {
    handle_function_call(name, args) {
      this[name](args)
    },

    inContext(context) {
      return !context || context === this.getRouteBaseName()
    },

    randomString() {
      return Math.random()
        .toString(36)
        .replace(/[^a-z]+/g, '')
        .substr(0, 5)
    },

    scrollTo(name) {
      document.getElementById(name).scrollIntoView({
        behavior: 'smooth',
        block: 'end',
        inline: 'start',
      })
    },

    pushTo(name) {
      this.$router.push({ path: this.localePath(name) })
    },
  },
}
</script>

<style scoped>
.menu-btn {
  font-family: 'Montserrat Alternates', cursive;
  font-size: 1.5em;
}
.menu-btn-item-text {
  transition: all 0.5s;
}
.menu-btn-item-text:hover {
  transition: all 0.5s;
  transform: translateX(10px);
  /* transform: skewX(25deg); */
}
</style>
