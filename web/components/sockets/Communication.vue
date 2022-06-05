<template>
  <span />
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  name: 'SocketCommunication',

  mounted() {
    if (this.connection && this.$root.socket) {
      this.initEvents()
      this.getMap()
      this.getSeed()
      this.getModes()
      this.getAlgorithms()
      this.getResults()
      this.setStatus('waiting')
    } else {
      this.$router.push({ path: this.localePath('home') })
    }
  },

  computed: {
    ...mapState('app', ['connection']),
  },

  methods: {
    ...mapMutations('play', ['setStatus']),

    initEvents() {
      this.$root.socket.on('map', (data) => {
        this.$emit('map', data)
      })

      this.$root.socket.on('seed', (data) => {
        this.$emit('seed', data)
      })

      this.$root.socket.on('step', (data) => {
        this.$emit('step', data)
      })

      this.$root.socket.on('modes', (data) => {
        this.$emit('modes', data)
      })

      this.$root.socket.on('algorithms', (data) => {
        this.$emit('algorithms', data)
      })

      this.$root.socket.on('results', (data) => {
        this.$emit('results', data)
      })
    },

    getMap() {
      this.$root.socket.emit('map')
    },

    getSeed() {
      this.$root.socket.emit('seed')
    },

    getModes() {
      this.$root.socket.emit('modes')
    },

    getAlgorithms() {
      this.$root.socket.emit('algorithms')
    },

    getResults() {
      this.$root.socket.emit('results')
    },
  },
}
</script>

<style lang="css" scoped></style>
