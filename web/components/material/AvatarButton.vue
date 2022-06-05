<template>
  <v-tooltip right>
    <template #activator="{ on, attrs }">
      <v-avatar
        v-ripple
        v-bind="attrs"
        class="action"
        :size="size"
        :color="dark ? 'white' : '#E0E0E0'"
        v-on="on"
        @click="$emit('clicked', !active ? null : name)"
      >
        <v-icon :color="dark ? 'black' : undefined" :size="iconSize">{{
          active ? icon : 'mdi-close'
        }}</v-icon>
      </v-avatar>
    </template>
    <span>{{ active ? tooltip : 'Cancel' }}</span>
  </v-tooltip>
</template>

<script>
export default {
  name: 'AvatarButton',

  props: {
    name: {
      type: String,
      default: null,
    },
    tooltip: {
      type: String,
      default: '',
    },
    size: {
      type: Number,
      default: 100,
    },
    iconSize: {
      type: Number,
      default: 32,
    },
    icon: {
      type: String,
      default: 'mdi-info',
    },
    active: {
      type: Boolean,
      default: false,
    },
  },

  computed: {
    dark() {
      return this.$vuetify.theme.dark
    },
    desktop() {
      return this.$vuetify.breakpoint.mdAndUp
    },
  },
}
</script>

<style lang="css" scoped>
.action {
  transition: all 0.5s;
}
.action:hover {
  transition: all 0.5s;
  cursor: pointer;
  transform: scale(1.1);
}
</style>
