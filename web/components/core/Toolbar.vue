<template>
  <v-app-bar
    app
    absolute
    flat
    height="100"
    class="switchLight"
    :style="`background-color: ${dark ? 'black' : 'white'}`"
  >
    <v-toolbar-title
      v-if="!inContext('home')"
      :class="dark ? 'white--text' : 'black--text'"
      class="text-lowercase px-8 pb-2 appname"
      style="font-family: 'Fredoka One', cursive"
      :style="desktop ? 'font-size: 3em' : 'font-size: 2.5em'"
      @click="$router.push({ path: localePath('home') })"
    >
      {{ $t('app.name') }}
    </v-toolbar-title>

    <span>
      <v-row class="pa-0 ma-0">
        <v-tooltip :right="!dial" :bottom="dial">
          <template #activator="{ on, attrs }">
            <v-btn
              fab
              v-bind="attrs"
              text
              :large="desktop"
              shaped
              class="px-4 mr-2 black--text toolbar-btn"
              v-on="on"
              @click="dial = !dial"
            >
              <v-icon :color="connection ? 'green' : 'red'">
                mdi-signal
              </v-icon>
            </v-btn>
          </template>
          <span>{{ connection ? 'Connected' : 'Not connected' }}</span>
        </v-tooltip>

        <v-text-field
          v-if="dial && desktop"
          :color="dark ? 'white' : 'black'"
          class="align-center"
          rounded
          filled
          clearable
          label="Enter server URL"
          :placeholder="serverUrl"
          hide-details
          @input="newUrl = $event"
          @keyup.enter="setNewUrl()"
          @focus="cancelTimer()"
          @blur="dial = false"
        />
      </v-row>
    </span>

    <v-spacer />

    <span>
      <v-btn
        v-for="(button, index) in buttonList()"
        :key="index"
        text
        :large="desktop"
        shaped
        :fab="!desktop || button.display === 'icon'"
        :color="
          !desktop ? (dark ? 'black' : 'white') : dark ? 'white' : 'black'
        "
        class="px-4 mr-2 black--text toolbar-btn"
        :class="button.class"
        @click="
          handle_function_call(
            inContext(button.context) ? button.action : button.oaction,
            !!button.args
              ? inContext(button.context)
                ? button.args[0]
                : button.args[1]
              : undefined
          )
        "
      >
        <span v-if="desktop && button.display !== 'icon'">{{
          $t(button.text)
        }}</span>
        <v-icon v-else :color="dark ? 'white' : 'black'">{{
          button.icon
        }}</v-icon>
      </v-btn>
    </span>

    <span>
      <menu-button :items="menuList()" />
    </span>
  </v-app-bar>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  name: 'Toolbar',

  components: {
    MenuButton: () => import('~/components/material/MenuButton'),
  },

  data: () => ({
    dial: false,
    newUrl: 'eeee',
    buttonsMenu: [
      {
        text: 'contents.title',
        icon: 'mdi-newspaper-variant',
        class: 'text-capitalize',
        action: 'pushTo',
        args: ['documentations'],
        context: undefined,
      },
      {
        text: 'results.title',
        icon: 'mdi-database-plus',
        class: 'text-capitalize',
        action: 'pushTo',
        args: ['results'],
        context: undefined,
      },
    ],
    buttons: [
      {
        text: 'contents.title',
        icon: 'mdi-theme-light-dark',
        class: 'text-capitalize',
        action: 'switchLightMode',
        args: ['documentations'],
        context: undefined,
        display: 'icon',
      },
    ],
  }),

  computed: {
    ...mapState('app', ['connection', 'dark', 'url']),

    serverUrl: {
      get() {
        return this.url
      },
      set(val) {
        this.setUrl(val)
      },
    },

    desktop() {
      return this.$vuetify.breakpoint.mdAndUp
    },
  },

  watch: {
    dial(val) {
      if (val) {
        this.unfocusTimer()
      }
    },
  },

  methods: {
    ...mapMutations('app', ['setDark', 'setUrl']),

    handle_function_call(name, args) {
      this[name](args)
    },

    inContext(context) {
      return !context || context === this.getRouteBaseName()
    },

    scrollTo(name) {
      document.getElementById(name).scrollIntoView({
        behavior: 'smooth',
        block: 'end',
        inline: 'start',
      })
    },

    setNewUrl() {
      this.serverUrl = this.newUrl
      this.dial = false
    },

    unfocusTimer() {
      this.timer = setTimeout(() => {
        this.dial = false
      }, 5000)
    },

    cancelTimer() {
      clearTimeout(this.timer)
    },

    pushTo(name) {
      this.$router.push({ path: this.localePath(name) })
    },

    async logout() {
      try {
        await this.$auth.logout()
        this.$router.push({ path: this.localePath('index') })
      } catch (err) {
        console.log(err)
      }
    },

    switchLightMode() {
      this.setDark(!this.dark)
      this.$vuetify.theme.dark = this.dark
    },

    buttonList() {
      return this.buttons.filter((item) => this.inContext(item.context))
    },

    menuList() {
      return this.buttonsMenu.filter((item) => this.inContext(item.context))
    },
  },
}
</script>

<style scoped>
.toolbar-btn {
  font-family: 'Montserrat Alternates', cursive;
  font-size: 1.5em;
}
.appname:hover {
  cursor: pointer;
  filter: brightness(1.2);
}
.switchLight {
  transition: background-color 1s;
}
</style>
