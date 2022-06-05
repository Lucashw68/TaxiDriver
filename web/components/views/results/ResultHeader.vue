<template>
  <!-- <v-card flat color="white" class="pa-4 py-8 rounded-xl"> -->
  <v-row align="center" justify="center" class="mt-2">
    <v-col cols="12" md="2" lg="2">
      <v-row align="center" justify="center">
        <span
          class="headline text-center text-capitalize font-weight-light px-4 white--text"
          >Rank
        </span>
      </v-row>
    </v-col>

    <v-col cols="12" md="4" lg="4">
      <v-row align="center" justify="center">
        <span
          class="headline text-center text-capitalize font-weight-light px-4 white--text"
        >
          Algorithm
        </span>
      </v-row>
    </v-col>

    <v-col cols="12" md="2" lg="2">
      <v-row align="center" justify="center">
        <v-btn
          rounded
          :color="getColorSortButton('seed')"
          @click="handleSelection('seed')"
        >
          <v-icon v-if="selected === 'seed'">mdi-circle</v-icon>
          <span
            class="headline text-capitalize text-center font-weight-light px-4 white--text"
            >Seed
          </span>
        </v-btn>
      </v-row>
    </v-col>

    <v-col cols="12" md="2" lg="2">
      <v-row align="center" justify="center">
        <v-btn
          rounded
          :color="getColorSortButton('steps')"
          @click="handleSelection('steps')"
        >
          <v-icon v-if="selected === 'steps'">mdi-circle</v-icon>
          <span
            class="headline text-capitalize text-center font-weight-light px-4 white--text"
            >Steps
          </span>
        </v-btn>
      </v-row>
    </v-col>

    <v-col cols="12" md="2" lg="2">
      <v-row align="center" justify="center">
        <v-btn
          rounded
          :color="getColorSortButton('reward')"
          @click="handleSelection('reward')"
        >
          <v-icon v-if="selected === 'reward'">mdi-circle</v-icon>
          <span
            class="headline text-capitalize text-center font-weight-light px-4 white--text"
            >Reward
          </span>
        </v-btn>
      </v-row>
    </v-col>

    <v-spacer />
  </v-row>
  <!-- </v-card> -->
</template>

<script>
export default {
  name: 'ResultHeader',

  data: () => ({
    selected: 'seed',
    order: true,
  }),

  computed: {
    dark() {
      return this.$vuetify.theme.dark
    },
  },

  watch: {
    selected(val) {
      console.log('Selected: ', val)
      this.order = true
      this.$emit('sort', { key: val, order: 'asc' })
    },
  },

  methods: {
    handleSelection(selection) {
      if (selection === this.selected) {
        this.order = !this.order
        this.$emit('sort', {
          key: selection,
          order: this.order ? 'asc' : 'desc',
        })
      }
      this.selected = selection
    },
    getColorSortButton(sortBy) {
      if (this.selected === sortBy) {
        return 'undefined'
      }
      return 'black'
    },
  },
}
</script>

<style lang="css" scoped></style>
