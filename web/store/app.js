import { set } from '@/config/store'

export const state = () => ({
  url: 'http://localhost:8000',
  connection: false,
  dark: true,
})

export const mutations = {
  setUrl: set('url'),
  setConnection: set('connection'),
  setDark: set('dark'),
}
