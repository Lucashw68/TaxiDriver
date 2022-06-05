<template>
  <v-menu
    open-on-click
    :close-on-content-click="false"
    :top="top"
    :bottom="bottom"
    min-width="350"
    center
    offset-y
    :nudge-left="(350 - 56) / 2"
    :rounded="styleMenu()"
  >
    <template #activator="{ on, attrs }">
      <v-btn
        fab
        class="mx-1 select-transition"
        :class="styleButton(attrs)"
        v-bind="attrs"
        v-on="on"
      >
        <v-icon>{{ icon }}</v-icon>
      </v-btn>
    </template>
    <v-list
      class="mb-8 py-4 px-4"
      style="
        box-shadow: rgba(128, 128, 128, 0.4) 0px 5px,
          rgba(128, 128, 128, 0.3) 0px 10px, rgba(128, 128, 128, 0.2) 0px 15px,
          rgba(128, 128, 128, 0.1) 0px 20px, rgba(128, 128, 128, 0.05) 0px 25px;
      "
    >
      <v-list-item class="py-4">
        <v-container>
          <v-row justify="center" align="center">
            <v-text-field
              v-model.number="seedInput"
              color="#fbae3c"
              clearable
              rounded
              filled
              type="number"
              hide-spin-buttons
              label="Seed"
              placeholder="Number"
              @click:clear="clearInput()"
            >
            </v-text-field>
          </v-row>

          <v-row justify="center" align="center">
            <v-btn
              class="px-4 mb-4"
              text
              large
              rounded
              @click="seedInput = randomSeed(0, 100000)"
              >Random seed</v-btn
            >
          </v-row>
        </v-container>
      </v-list-item>

      <v-divider />

      <v-list-item class="py-4">
        <v-container>
          <v-row justify="center" align="center">
            <span>Refresh time (ms)</span>
          </v-row>
          <v-row justify="center" align="center">
            <v-slider
              v-model="refreshTimeInput"
              color="#fbae3c"
              step="100"
              min="100"
              max="1000"
              ticks="always"
              thumb-label
            >
            </v-slider>
          </v-row>
        </v-container>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  name: 'InputButton',

  props: {
    title: {
      type: String,
      default: 'Button',
    },
    icon: {
      type: String,
      default: 'mdi-arrow-up-drop-circle',
    },
    items: {
      type: Array,
      default: () => {},
    },
    selected: {
      type: String,
      default: '',
    },
    top: {
      type: Boolean,
      default: false,
    },
    bottom: {
      type: Boolean,
      default: false,
    },
  },

  computed: {
    ...mapState('play', ['seed', 'refreshTime']),

    refreshTimeInput: {
      get() {
        return this.refreshTime
      },
      set(val) {
        this.setRefreshTime(val)
        this.$emit('refresh')
      },
    },

    seedInput: {
      get() {
        return this.seed
      },
      set(val) {
        if (val && val >= 0) {
          this.setSeed(val)
        } else {
          this.setSeed(0)
        }
        this.$emit('seed')
      },
    },
  },

  methods: {
    ...mapMutations('play', ['setSeed', 'setRefreshTime']),

    styleButton(attrs) {
      const expanded = JSON.parse(attrs['aria-expanded'])
      if (!expanded) {
        return ''
      } else if (this.$props.top) {
        return 'rounded-b-xl rounded-t-0'
      } else if (this.$props.bottom) {
        return 'rounded-t-xl rounded-b-0'
      }
    },
    styleMenu() {
      return 'xl'
    },
    clearInput() {
      this.seedInput = 0
    },
    randomSeed(min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min)) + min
    },
  },
}
</script>

<style lang="css">
.select-transition {
  transition: border-radius 0.5s;
}
.select-transition:hover {
  transition: border-radius 0.5s;
}
</style>
