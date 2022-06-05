<template>
  <hero
    first
    :color="dark ? 'black' : 'white'"
    :class="`spacer-${dark ? 'dark' : 'light'}`"
  >
    <template slot="content">
      <v-container fluid>
        <v-row justify="center" align="start">
          <span
            :class="dark ? 'white--text' : 'black--text'"
            class="text-lowercase"
            :style="`font-size: ${desktop ? '8em' : '4em'}`"
            style="font-family: 'Fredoka One', cursive"
            >{{ $t('app.name') }}</span
          >
        </v-row>

        <v-row justify="center">
          <v-col cols="12" md="6" lg="6">
            <v-container fluid fill-height>
              <v-col
                v-for="(button, index) in displayButtons()"
                :key="`button-${index}`"
                class="row justify-center"
                cols="12"
                md="4"
                lg="4"
              >
                <avatar-button
                  :name="button.name"
                  :tooltip="button.tooltip"
                  :size="button.size"
                  :icon-size="button.iconSize"
                  :icon="button.icon"
                  :active="isSelected(button.name)"
                  @clicked="
                    connection
                      ? $router.push({ path: localePath('play') })
                      : $toast.error(
                          'The server must be connected to access this feature'
                        )
                  "
                />
              </v-col>
            </v-container>
          </v-col>
        </v-row>

        <keep-alive>
          <socket-connection />
        </keep-alive>
      </v-container>
    </template>
  </hero>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'Home',

  components: {
    Hero: () => import('~/components/material/Hero'),
    AvatarButton: () => import('~/components/material/AvatarButton'),
    SocketConnection: () => import('~/components/sockets/Connection'),
  },

  data: () => ({
    input: null,
    focusSearch: false,
    selected: null,
    payload: null,
    result: null,
    buttons: [
      {
        name: 'Play',
        tooltip: 'Launch the simulation',
        size: 100,
        iconSize: 32,
        icon: 'mdi-play',
      },
    ],
  }),

  computed: {
    ...mapState('app', ['connection']),

    dark() {
      return this.$vuetify.theme.dark
    },
    desktop() {
      return this.$vuetify.breakpoint.mdAndUp
    },
  },

  methods: {
    scrollTo(name, offset) {
      document.getElementById(name).scrollIntoView({
        behavior: 'smooth',
        block: 'end',
        inline: 'start',
      })
    },

    handleButtons(val) {
      this.result = null
      this.selected = val
      if (val) this[val]()
    },

    displayButtons() {
      return !this.selected
        ? this.buttons
        : this.buttons.filter((item) => this.selected === item.name)
    },

    isSelected(name) {
      return !this.selected || this.selected !== name
    },
  },
}
</script>

<style scoped>
.big-input {
  font-size: 30px !important;
}
.roll:hover {
  animation: spin 1s linear;
}
@keyframes spin {
  from {
    transform-origin: center;
    transform: rotate(0deg);
  }
  to {
    transform-origin: center;
    transform: rotate(360deg);
  }
}

.custom-shape-divider-top-1636674843 {
  position: absolute;
  transform: rotate(180deg);
  bottom: 0;
  left: 0;
  width: 100%;
  overflow: hidden;
  line-height: 0;
}

.spacer-dark {
  aspect-ratio: 900/600;
  width: 100%;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  animation: background-dark 10s ease-in infinite reverse;
  -webkit-transition: opacity 1s ease-in-out;
  -moz-transition: opacity 1s ease-in-out;
  -o-transition: opacity 1s ease-in-out;
  transition: opacity 1s ease-in-out;
  background-image: url('~/static/blob-dark.svg');
}

.spacer-light {
  aspect-ratio: 900/600;
  width: 100%;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  animation: background-light 10s ease-in infinite reverse;
  -webkit-transition: opacity 1s ease-in-out;
  -moz-transition: opacity 1s ease-in-out;
  -o-transition: opacity 1s ease-in-out;
  transition: opacity 1s ease-in-out;
  background-image: url('~/static/blob-light.svg');
}

@keyframes background-dark {
  from {
    background-image: url('~/static/blob-dark.svg');
    transition: all 0.5s;
  }
  to {
    background-image: url('~/static/blob2-dark.svg');
    transition: all 0.5s;
  }
}

@keyframes background-light {
  from {
    background-image: url('~/static/blob-light.svg');
    transition: all 0.5s;
  }
  to {
    background-image: url('~/static/blob2-light.svg');
    transition: all 0.5s;
  }
}
</style>
