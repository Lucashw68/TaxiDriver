<template>
  <v-app :dark="dark">
    <v-main>
      <nuxt />
    </v-main>
  </v-app>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data: () => ({}),

  mounted() {
    this.$nextTick(() => {
      this.$nuxt.$loading.start()
      setTimeout(() => {
        this.$nuxt.$loading.finish()
      }, 500)
    })
  },

  computed: {
    ...mapState('app', ['dark']),
  },
}
</script>
