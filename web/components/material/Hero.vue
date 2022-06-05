<template>
  <v-container class="hero" :style="heightStyle" :fill-height="fill" fluid>
    <slot name="content" />
  </v-container>
</template>

<script>
export default {
  name: 'Hero',

  props: {
    first: {
      type: Boolean,
      default: false,
    },
    fill: {
      type: Boolean,
      default: true,
    },
    color: {
      type: String,
      default: 'white',
    },
  },

  computed: {
    heightStyle() {
      return `height: calc(100vh - ${
        this.$props.first ? '100px' : '0px'
      });background-color: ${this.$props.color}`
    },
  },
}
</script>

<style scoped>
.hero {
  transition: background-color 1s;
  /* border: 1px inset black; */
}
</style>
