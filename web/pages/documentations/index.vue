<template>
  <v-container fluid fill-height>
    <v-row justify="center">
      <v-col cols="12" md="10" lg="10">
        <transition name="fade">
          <content-timeline
            v-if="contents.length > 0"
            context="documentations"
            :contents="contents"
          />
        </transition>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'Contents',
  auth: false,

  components: {
    ContentTimeline: () =>
      import('~/components/views/contents/ContentTimeline'),
  },

  data: () => ({
    contents: [],
  }),

  async fetch() {
    this.contents = await this.$content('documentations')
      .only(['title', 'description', 'img', 'slug', 'author', 'createdAt'])
      .sortBy('createdAt', 'desc')
      .fetch()
  },

  mounted() {
    this.$fetch()
  },
}
</script>

<style scoped></style>
