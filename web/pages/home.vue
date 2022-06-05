<template>
  <span id="home">
    <home-taxi id="taxi" />
  </span>
</template>

<script>
export default {
  name: 'Home',
  auth: false,

  components: {
    HomeTaxi: () => import('~/components/views/home/HomeTaxi'),
  },

  transition: 'intro',

  computed: {
    desktop() {
      return this.$vuetify.breakpoint.mdAndUp
    },
  },
}
</script>

<style scoped></style>
