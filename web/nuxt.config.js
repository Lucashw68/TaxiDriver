import colors from 'vuetify/es5/util/colors'
import pages from './config/locales/pages.json'
import ru from './config/locales/ru.json'
import en from './config/locales/en.json'
import fr from './config/locales/fr.json'

export default {
  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s',
    title: 'TaxiDriver',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Nuxt boilerplate' },
      { name: 'theme-color', content: '#424242' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'apple-touch-icon',
        sizes: '180x180',
        href: '/static/apple-touch-icon.png',
      },
      {
        rel: 'mask-icon',
        href: '/static/safari-pinned-tab.svg',
        color: '#5bbad5',
      },
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['~/css/main.css', '~/assets/fonts/fonts.css'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [{ src: '~/plugins/vuex-persist', ssr: false }],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://pwa.nuxtjs.org/onesignal
    '@nuxtjs/pwa',
    // https://go.nuxtjs.dev/content
    '@nuxt/content',
    // https://i18n.nuxtjs.org/
    'nuxt-i18n',
    // https://github.com/Maronato/vue-toastification
    'vue-toastification/nuxt',
    // https://nuxt-socket-io.netlify.app/
    'nuxt-socket-io',
  ],

  // i18n module configuration: https://i18n.nuxtjs.org/
  i18n: {
    strategy: 'prefix_except_default',
    locales: ['en', 'fr', 'ru'],
    defaultLocale: 'fr',
    vueI18n: {
      fallbackLocale: 'en',
      messages: { en, fr, ru },
    },
    parsePages: false,
    pages,
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL:
      process.env.NODE_ENV === 'production'
        ? process.env.URL_API
        : 'http://localhost:8081/api',
  },

  io: {
    sockets: [
      {
        name: 'home',
        url: 'http://localhost:8000',
        default: true,
        vuex: {},
        namespaces: {},
      },
    ],
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'fr',
      name: 'TaxiDriver',
      theme_color: '#424242',
      short_name: 'TaxiDriver',
      background_color: '#424242',
      useWebmanifestExtension: false,
    },
  },

  toast: {
    position: 'bottom-left',
  },

  // Content module configuration: https://go.nuxtjs.dev/config-content
  content: {},

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  loading: {
    color: '#424242',
    height: '5px',
    continuous: true,
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: [/^vue2-google-maps($|\/)/],
  },

  generate: {
    fallback: '404.html',
  },

  server: {
    host: '0.0.0.0',
  },
}
