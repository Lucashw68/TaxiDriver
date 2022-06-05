<template>
  <v-timeline
    :light="!dark"
    align-top
    reverse
    :dense="$vuetify.breakpoint.smAndDown"
  >
    <v-timeline-item
      v-for="(content, index) in contents"
      :key="index"
      :color="getColor(index)"
      fill-dot
      large
    >
      <template #opposite>
        <span
          :class="dark ? 'white--text' : 'black--text'"
          class="font-weight-bold"
          style="font-family: 'Montserrat alternates'; font-size: 1.5em"
          v-text="formatDate(content.createdAt)"
        />
      </template>
      <v-card :color="getColor(index)" flat dark>
        <v-card-title class="overline text-h5">
          {{ content.title }}
        </v-card-title>
        <v-card-text class="white text--primary">
          <p class="black--text pt-4">
            {{ content.description }}
          </p>
          <v-btn
            :color="getColor(index)"
            class="mx-0"
            outlined
            @click="
              $router.push({
                name: `${context}-slug___` + $i18n.locale,
                params: { slug: content.slug },
              })
            "
          >
            {{ $t('contents.read') }}
          </v-btn>
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>

<script>
export default {
  name: 'ContentTimeline',

  props: {
    contents: {
      type: Array,
      default: () => [],
    },
    context: {
      type: String,
      default: 'documentations',
    },
  },

  data: () => ({
    colors: [
      'black',
      'red lighten-2',
      'purple darken-1',
      'green lighten-1',
      'indigo',
    ],
  }),

  computed: {
    dark() {
      return this.$vuetify.theme.dark
    },
  },

  methods: {
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' }
      return new Date(date).toLocaleDateString(this.$i18n.locale, options)
    },
    getColor(index) {
      return this.dark
        ? this.colors.slice(1)[index % (this.colors.length - 1)]
        : this.colors[index % this.colors.length]
    },
  },
}
</script>

<style scoped>
h1,
h2,
h3,
h4 {
  color: black;
}
</style>
