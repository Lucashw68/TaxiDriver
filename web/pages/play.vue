<template>
  <v-container fluid fill-height>
    <v-row justify="center" align="center">
      <v-container fluid>
        <v-row justify="center">
          <span class="text-h5">{{ `#${seed}` }}</span>
        </v-row>

        <v-row justify="center" class="mb-4">
          <v-col cols="12" md="10" lg="10">
            <v-row justify="center">
              <v-col cols="12" md="6" lg="6">
                <v-card
                  tile
                  color="grey"
                  :class="`status-${status}`"
                  class="rounded-t-xl box"
                >
                  <v-container>
                    <v-row justify="center">
                      <span
                        class="text-capitalize white--text"
                        :style="`font-size: ${desktop ? '2em' : '1em'}`"
                        style="font-family: 'Montserrat Alternates', cursive"
                        >{{ `${status}...` }}</span
                      >
                    </v-row>
                  </v-container>
                </v-card>
              </v-col>
            </v-row>
          </v-col>
        </v-row>

        <v-row justify="center" class="mb-8">
          <v-col cols="12" md="5" lg="5">
            <v-row justify="center">
              <v-col
                v-for="(info, index) in infos"
                :key="`${index}`"
                cols="12"
                md="6"
                lg="6"
              >
                <v-card tile color="grey" class="box">
                  <v-container>
                    <v-row justify="center">
                      <span
                        class="white--text"
                        :style="`font-size: ${desktop ? '2em' : '1em'}`"
                        style="font-family: 'Montserrat Alternates', cursive"
                        >{{ `${info.title}: ${info.value}` }}</span
                      >
                    </v-row>
                  </v-container>
                </v-card>
              </v-col>
            </v-row>
          </v-col>
        </v-row>

        <v-row justify="center" align="center">
          <grid :map="map" />
        </v-row>
      </v-container>
    </v-row>

    <socket-communication
      @map="map = $event"
      @seed="storeSeed($event)"
      @modes="storeModes($event)"
      @algorithms="storeAlgorithms($event)"
      @step="storeStep($event)"
      @results="storeResults($event)"
    />
  </v-container>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  name: 'Play',

  components: {
    Grid: () => import('~/components/views/play/Grid'),
    SocketCommunication: () => import('~/components/sockets/Communication'),
  },
  layout: 'play',
  auth: false,
  transition: 'intro',

  data: () => ({
    map: null,
  }),

  computed: {
    ...mapState('app', ['connection']),
    ...mapState('play', [
      'step',
      'lastAction',
      'state',
      'reward',
      'status',
      'done',
      'seed',
    ]),
    desktop() {
      return this.$vuetify.breakpoint.mdAndUp
    },
    dark() {
      return this.$vuetify.theme.dark
    },
    infos() {
      return [
        { title: 'Action', value: this.lastAction },
        { title: 'Step', value: this.step },
        { title: 'Reward', value: this.reward },
        { title: 'State', value: this.state },
      ]
    },
  },

  methods: {
    ...mapMutations('play', [
      'setMode',
      'setModes',
      'setAlgorithm',
      'setAlgorithms',
      'setReward',
      'setState',
      'setDone',
      'setSeed',
      'setResults',
      'setFinalReward',
    ]),
    storeModes(modes) {
      this.setMode(modes[0])
      this.setModes(modes)
    },
    storeAlgorithms(algorithms) {
      this.setAlgorithm(algorithms[0])
      this.setAlgorithms(algorithms)
    },
    storeStep(step) {
      this.setState(step.state)
      this.setFinalReward(this.reward + step.reward)
      this.setReward(step.reward)
      this.setDone(step.done)
    },
    storeSeed(seed) {
      this.setSeed(seed)
    },
    storeResults(results) {
      this.setResults(results)
    },
  },
}
</script>

<style scoped>
.status-waiting {
  background-color: grey;
}
.status-running {
  background-color: purple;
  animation: blink 1.5s linear 0s infinite alternate;
}
.status-stopped {
  background-color: firebrick;
}
.status-done {
  background-color: blue;
  animation: blink 1.5s linear 0s infinite alternate;
}
.box {
  box-shadow: rgba(128, 128, 128, 0.4) 0px 5px,
    rgba(128, 128, 128, 0.3) 0px 10px, rgba(128, 128, 128, 0.2) 0px 15px,
    rgba(128, 128, 128, 0.1) 0px 20px, rgba(128, 128, 128, 0.05) 0px 25px !important;
}
@keyframes blink {
  from {
    filter: brightness(1);
  }
  to {
    filter: brightness(1.5);
  }
}
</style>
