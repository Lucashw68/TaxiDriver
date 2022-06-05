<template>
  <v-app :dark="dark">
    <client-only>
      <core-toolbar />
      <core-view />
      <core-footer />
    </client-only>
  </v-app>
</template>

<script>
import { mapState } from 'vuex'
export default {
  components: {
    CoreView: () => import('~/components/core/View.vue'),
    CoreToolbar: () => import('~/components/core/Toolbar.vue'),
    CoreFooter: () => import('~/components/core/Footer.vue'),
  },
  data: () => ({}),

  computed: {
    ...mapState('app', ['dark']),
  },

  mounted() {
    this.$vuetify.theme.dark = this.dark
  },
}
</script>
