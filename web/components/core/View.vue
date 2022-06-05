<template>
  <v-main>
    <div
      id="core-view"
      :style="`background-color: ${dark ? 'black' : 'white'}`"
    >
      <nuxt />
    </div>
  </v-main>
</template>

<script>
export default {
  name: 'CoreView',

  computed: {
    dark() {
      return this.$vuetify.theme.dark
    },
  },
}
</script>

<style scoped>
#core-view {
  height: 100%;
}
</style>
