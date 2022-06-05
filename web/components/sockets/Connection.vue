<template>
  <span />
</template>

<script>
import io from 'socket.io-client'
import { mapState, mapMutations } from 'vuex'
export default {
  name: 'SocketConnection',

  watch: {
    url(val) {
      this.setConnection(false)
      this.$root.socket.disconnect()
      this.$root.socket = {}
      this.$toast.info('Try connecting...', { timeout: 2000 })
      this.initSocket()
    },
  },

  mounted() {
    if (!this.connection || !this.$root.socket) this.initSocket()
  },

  computed: {
    ...mapState('app', ['connection', 'url']),
  },

  methods: {
    ...mapMutations('app', ['setSocket', 'setConnection']),

    initSocket() {
      this.$root.socket = io(this.url, {
        autoConnect: true,
        reconnectionDelay: 10000,
        reconnectionDelayMax: 10000,
        randomizationFactor: 1,
      })
      if (!this.$root.socket.connected) this.connect()
      this.initEvents()
    },

    connect() {
      this.$root.socket.io.open((err) => {
        if (err) {
          this.reconnect(1500)
        } else {
          this.$toast.info('Socket opened')
        }
      })
    },

    reconnect(delay) {
      setTimeout(() => {
        this.connect()
      }, delay)
    },

    initEvents() {
      this.$root.socket.on('connect', (data) => {
        this.setConnection(true)
        this.$toast.success('Server connected')
      })

      this.$root.socket.on('disconnect', (data) => {
        this.setConnection(false)
        this.$toast.error('Server disconnected')
      })

      window.onbeforeunload = () => {
        this.$root.socket.emit('disconnected', 'testUser')
      }
    },
  },
}
</script>

<style lang="css" scoped></style>
