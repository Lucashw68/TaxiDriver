<template>
  <v-card flat color="white" class="pa-4 py-8 rounded-xl">
    <v-row align="center" justify="center">
      <v-col cols="12" md="2" lg="2">
        <v-row align="center" justify="center">
          <v-avatar>
            <v-icon :color="color">{{ icon }}</v-icon>
          </v-avatar>
        </v-row>
      </v-col>

      <v-col cols="12" md="4" lg="4">
        <v-row align="center" justify="center">
          <span
            class="headline text-center text-capitalize font-weight-light px-4 black--text"
            >{{ `${algorithm} algorithm` }}
          </span>
        </v-row>
      </v-col>

      <v-col cols="12" md="2" lg="2">
        <v-row align="center" justify="center">
          <v-btn rounded @click="$emit('seed')">
            <span
              class="headline text-center font-weight-light px-4 white--text"
              >{{ seed }}
            </span>
          </v-btn>
        </v-row>
      </v-col>

      <v-col cols="12" md="2" lg="2">
        <v-row align="center" justify="center">
          <span class="headline text-center font-weight-light px-4 black--text"
            >{{ steps }}
          </span>
        </v-row>
      </v-col>

      <v-col cols="12" md="2" lg="2">
        <v-row align="center" justify="center">
          <span class="headline text-center font-weight-light px-4 black--text"
            >{{ reward }}
          </span>
        </v-row>
      </v-col>

      <v-spacer />
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: 'Result',

  props: {
    icon: {
      type: String,
      default: 'mdi-trophy',
    },
    color: {
      type: String,
      default: 'black',
    },
    algorithm: {
      type: String,
      default: 'None',
    },
    seed: {
      type: Number,
      default: 0,
    },
    steps: {
      type: Number,
      default: 0,
    },
    reward: {
      type: Number,
      default: 0,
    },
  },
}
</script>

<style lang="css" scoped></style>
