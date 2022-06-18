<template>
  <v-container fluid>
    <v-row justify="center">
      <v-icon class="pr-4" color="#fbae3c" size="6em">mdi-trophy</v-icon>
      <span
        :class="dark ? 'white--text' : 'black--text'"
        class="text-capitalize"
        :style="`font-size: ${desktop ? '6em' : '3em'}`"
        style="font-family: 'Fredoka One', cursive"
        >{{ 'Results' }}</span
      >
    </v-row>

    <v-row justify="center" class="pb-4">
      <select-button
        title="Algorithm"
        :items="['all'].concat(algorithms)"
        :selected="algorithm"
        :bottom="true"
        icon="mdi-filter-variant"
        @update:selected="updateAlgorithm($event)"
      />
      <seed-info
        v-if="seed"
        :title="seed.toString()"
        :bottom="true"
        icon="mdi-sprout"
        @remove="seed = null"
      />

      <v-btn
        fab
        class="mx-1"
        @click="$router.push({ path: localePath('play') })"
      >
        <v-icon color="green">mdi-play</v-icon>
      </v-btn>
    </v-row>

    <v-row justify="center">
      <v-col cols="12" md="10" lg="6">
        <result-header
          v-if="displayResults.length > 0"
          @sort="sortBy($event)"
        />
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="12" md="10" lg="6">
        <result
          v-for="(item, index) in displayResults"
          :key="index"
          class="mb-4"
          :color="getResultColor(index)"
          :algorithm="item.algorithm"
          :seed="item.seed"
          :steps="item.steps"
          :reward="item.reward"
          @seed="seed = item.seed"
        />
        <v-card
          v-if="displayResults.length === 0"
          flat
          color="white"
          class="pa-4 py-8 rounded-xl"
        >
          <v-row align="center" justify="center">
            <v-icon color="black">mdi-google-downasaur</v-icon>
            <span
              class="headline text-center text-capitalize font-weight-light px-4 black--text"
            >
              No results
            </span>
          </v-row>
        </v-card>
      </v-col>
    </v-row>

    <socket-communication
      @algorithms="storeAlgorithms($event)"
      @results="storeResults($event)"
    />
  </v-container>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  name: 'Results',

  components: {
    SelectButton: () => import('~/components/material/SelectButton'),
    Result: () => import('~/components/views/results/Result'),
    ResultHeader: () => import('~/components/views/results/ResultHeader'),
    SeedInfo: () => import('~/components/views/results/SeedInfo'),
    SocketCommunication: () => import('~/components/sockets/Communication'),
  },

  data: () => ({
    seed: null,
    algorithm: 'all',
    displayResults: [],
  }),

  computed: {
    ...mapState('app', ['connection']),
    ...mapState('play', ['algorithms', 'mode', 'modes', 'results']),
    desktop() {
      return this.$vuetify.breakpoint.mdAndUp
    },
    dark() {
      return this.$vuetify.theme.dark
    },
  },

  methods: {
    ...mapMutations('play', ['setMode', 'setResults', 'setAlgorithms']),

    storeResults(results) {
      this.setResults(results)
    },
    storeAlgorithms(algorithms) {
      this.setAlgorithms(algorithms)
    },
    parseResults(data) {
      return data.results
    },
    seedFilter() {
      this.displayResults = this.parseResults(this.results).filter(
        (item) => item.seed === this.seed
      )
    },
    algoFilter() {
      this.displayResults = this.parseResults(this.results).filter(
        (item) => item.algorithm === this.algorithm
      )
    },
    sortBy(sort) {
      this.displayResults.sort(this.compareValues(sort.key, sort.order))
    },
    compareValues(key, order) {
      return function innerSort(a, b) {
        if (
          !Object.prototype.hasOwnProperty.call(a, key) ||
          !Object.prototype.hasOwnProperty.call(b, key)
        ) {
          return 0
        }
        const varA = typeof a[key] === 'string' ? a[key].toUpperCase() : a[key]
        const varB = typeof b[key] === 'string' ? b[key].toUpperCase() : b[key]

        let comparison = 0
        if (varA > varB) {
          comparison = 1
        } else if (varA < varB) {
          comparison = -1
        }
        return order === 'desc' ? comparison * -1 : comparison
      }
    },
    getResultColor(index) {
      const colors = ['#fbae3c', '#DCDCDC', '#CD7F32']
      const defaultColor = 'black'
      if (index < 3) {
        return colors[index]
      } else {
        return defaultColor
      }
    },
    updateAlgorithm(algorithm) {
      this.algorithm = algorithm
    },
  },

  watch: {
    results(val) {
      this.displayResults = [...this.parseResults(this.results)]
    },
    seed(val) {
      if (val) {
        this.seedFilter()
      } else {
        this.displayResults = [...this.parseResults(this.results)]
      }
    },
    algorithm(val) {
      if (val === 'all') {
        this.displayResults = [...this.parseResults(this.results)]
      } else {
        this.algoFilter()
      }
    },
  },
}
</script>

<style lang="css" scoped></style>
