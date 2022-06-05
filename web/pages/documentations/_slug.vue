<template>
  <v-container fluid fill-height>
    <v-row justify="center" align="center" class="content pb-8">
      <article style="width: 80%">
        <h1 :class="dark ? 'white--text' : 'black--text'">
          {{ content.title }}
        </h1>
        <h3 :class="dark ? 'white--text' : 'black--text'">
          {{ formatDate(content.createdAt) }}
        </h3>
        <nuxt-content
          :document="content"
          :class="dark ? 'content-dark' : 'content-light'"
        />
      </article>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'DocumentationsSlug',
  transition: 'intro',
  auth: false,

  async asyncData({ $content, params }) {
    const content = await $content('documentations', params.slug).fetch()
    return { content }
  },

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
  },
}
</script>

<style>
.nuxt-content-editor {
  background-color: white;
}
h1 {
  font-size: 4rem;
}
.content-dark {
  .nuxt-content p {
    color: white;
  }
}
.content-dark {
  .nuxt-content p {
    color: black;
  }
}
</style>
