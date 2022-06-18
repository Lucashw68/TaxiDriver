<template>
  <v-footer padless>
    <v-card
      flat
      tile
      width="100%"
      class="black lighten-1 text-center py-4"
      :class="dark ? 'black lighten-1' : 'grey'"
    >
      <v-container fluid>
        <v-row justify="center" align="center">
          <v-btn
            v-if="status !== 'stopped'"
            class="mx-1"
            fab
            @click="playing() ? requestStop() : requestPlay()"
          >
            <v-icon :color="playing() ? 'red' : 'green'">{{
              playing() ? 'mdi-stop' : 'mdi-play'
            }}</v-icon>
          </v-btn>

          <v-btn
            v-if="status === 'waiting' && status !== 'stopped'"
            class="mx-1"
            fab
            @click="requestStep()"
          >
            <v-icon color="purple">mdi-step-forward</v-icon>
          </v-btn>

          <v-btn class="mx-1" fab @click="requestReset()">
            <v-icon :color="dark ? 'white' : 'black'">mdi-refresh</v-icon>
          </v-btn>

          <input-button
            icon="mdi-cog"
            :top="true"
            @seed="requestReset()"
            @refresh="updateRefreshTime()"
          />

          <select-button
            title="Algorithm"
            :items="algorithms"
            :selected="algorithm"
            :top="true"
            @update:selected="updateAlgorithm($event)"
          />

          <v-btn
            class="mx-1"
            rounded
            x-large
            height="56"
            @click="$router.push({ path: localePath('results') })"
          >
            <v-icon class="pr-4">mdi-trophy</v-icon>
            Results
          </v-btn>

          <!-- <v-btn fab right>
              <v-icon>mdi-map</v-icon>
            </v-btn> -->
        </v-row>
      </v-container>
    </v-card>
  </v-footer>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  name: 'CoreFooter',

  components: {
    SelectButton: () => import('~/components/material/SelectButton'),
    InputButton: () => import('~/components/material/InputButton'),
  },

  data: () => ({
    runLoop: null,
  }),

  computed: {
    ...mapState('play', [
      'mode',
      'modes',
      'algorithm',
      'algorithms',
      'step',
      'status',
      'refreshTime',
      'seed',
      'done',
      'finalReward',
    ]),
    dark() {
      return this.$vuetify.theme.dark
    },
  },

  methods: {
    ...mapMutations('play', [
      'setMode',
      'setAlgorithm',
      'setStep',
      'setLastAction',
      'setState',
      'setReward',
      'setStatus',
      'setDone',
      'setFinalReward',
    ]),
    addResult() {
      this.$root.socket.emit('result', {
        steps: this.step,
        reward: this.finalReward,
      })
    },
    updateMode(mode) {
      this.setMode(mode)
      this.$root.socket.emit('mode', mode)
    },
    updateAlgorithm(algorithm) {
      this.setAlgorithm(algorithm)
      this.$root.socket.emit('algorithm', algorithm)
    },
    updateRefreshTime() {
      if (this.status === 'running') {
        clearInterval(this.runLoop)
        this.runLoop = setInterval(this.requestStep, this.refreshTime)
      }
    },
    requestPlay() {
      this.runLoop = setInterval(this.requestStep, this.refreshTime)
      this.setStatus('running')
    },
    requestStop() {
      clearInterval(this.runLoop)
      this.setStatus('stopped')
    },
    requestStep() {
      this.$root.socket.emit('step')
      this.setStep(this.step + 1)
    },
    requestReset() {
      this.requestStop()
      this.$root.socket.emit('reset', this.seed)
      this.setStep(0)
      this.setState(0)
      this.setReward(0)
      this.setFinalReward(0)

      this.setStatus('waiting')
      this.setLastAction('None')
    },
    playing() {
      return this.status === 'running' && this.status !== 'waiting'
    },
  },

  watch: {
    done(val) {
      console.log('=== Done changed')
      if (val) {
        this.requestStop()
        this.addResult()
      }
    },
  },
}
</script>

<style lang="css" scoped></style>
