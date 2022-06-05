<template>
  <v-menu
    open-on-hover
    :top="top"
    :bottom="bottom"
    offset-y
    :rounded="styleMenu()"
  >
    <template #activator="{ on, attrs }">
      <v-btn
        class="mx-1 select-transition"
        :class="styleButton(attrs)"
        x-large
        height="56"
        v-bind="attrs"
        v-on="on"
      >
        <v-icon class="pr-4">{{
          icon
            ? icon
            : top
            ? 'mdi-arrow-up-drop-circle'
            : 'mdi-arrow-down-drop-circle'
        }}</v-icon>
        {{ title }}
      </v-btn>
    </template>
    <v-list class="py-0">
      <v-list-item
        v-for="item in items"
        :key="item"
        @click.stop="selection = item"
      >
        <v-row justify="center" align="center">
          <span class="text-capitalize">{{ item }}</span>
          <v-icon v-if="selection === item" class="pl-4" color="green"
            >mdi-check</v-icon
          >
        </v-row>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  name: 'SelectButton',

  props: {
    title: {
      type: String,
      default: 'Button',
    },
    icon: {
      type: String,
      default: 'mdi-arrow-up-drop-circle',
    },
    items: {
      type: Array,
      default: () => {},
    },
    selected: {
      type: String,
      default: '',
    },
    top: {
      type: Boolean,
      default: false,
    },
    bottom: {
      type: Boolean,
      default: false,
    },
  },

  computed: {
    selection: {
      get() {
        return this.$props.selected
      },
      set(val) {
        this.$emit('update:selected', val)
      },
    },
  },

  methods: {
    styleButton(attrs) {
      const expanded = JSON.parse(attrs['aria-expanded'])
      if (!expanded) {
        return 'rounded-xl'
      } else if (this.$props.top) {
        return 'rounded-b-xl rounded-t-0'
      } else if (this.$props.bottom) {
        return 'rounded-t-xl rounded-b-0'
      }
    },
    styleMenu() {
      if (this.$props.top) {
        return 't-xl b-0'
      } else if (this.$props.bottom) {
        return 'b-xl t-0'
      }
      return false
    },
  },
}
</script>

<style lang="css">
.select-transition {
  transition: border-radius 0.5s;
}
.select-transition:hover {
  transition: border-radius 0.5s;
}
</style>
