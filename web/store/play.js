import { set } from '@/config/store'

export const state = () => ({
  mode: '',
  modes: [],
  algorithm: '',
  algorithms: [],
  seed: 42,

  step: 0,
  reward: 0,
  state: 0,
  lastAction: 'None',

  refreshTime: 500,
  status: 'waiting',
  done: false,

  results: [],
})

export const mutations = {
  setMode: set('mode'),
  setModes: set('modes'),
  setAlgorithm: set('algorithm'),
  setAlgorithms: set('algorithms'),
  setSeed: set('seed'),

  setStep: set('step'),
  setLastAction: set('lastAction'),
  setReward: set('reward'),
  setState: set('state'),

  setRefreshTime: set('refreshTime'),
  setStatus: set('status'),
  setDone: set('done'),

  setResults: set('results'),
}
