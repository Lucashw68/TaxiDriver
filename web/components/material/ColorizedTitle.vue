<template>
  <span id="colorizedTitle">
    <span
      :class="`${startColor}--text`"
      style="font-family: 'Fredoka One', cursive"
      :style="desktop ? 'font-size: 4em;' : 'font-size: 2em'"
    >
      {{ startText }}
    </span>
    <span
      :class="`${endColor}--text`"
      class="text-capitalize"
      style="font-family: 'Fredoka One', cursive"
      :style="desktop ? 'font-size: 4em;' : 'font-size: 2em'"
    >
      {{ endText }}
    </span>
  </span>
</template>

<script>
export default {
  name: 'ColorizedTitle',

  props: {
    startText: {
      type: String,
      default: 'Start',
    },
    endText: {
      type: String,
      default: 'End',
    },
    startColor: {
      type: String,
      default: 'white',
    },
    endColor: {
      type: String,
      default: 'red',
    },
  },

  data: () => ({}),

  computed: {
    desktop() {
      return this.$vuetify.breakpoint.xlAndUp
    },
  },
}
</script>

<style lang="css" scoped></style>
