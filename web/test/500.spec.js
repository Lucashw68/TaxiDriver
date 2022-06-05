import Vue from 'vue'
import vuetify from 'vuetify'
import { shallowMount } from '@vue/test-utils'
import Error500 from '@/components/error/500.vue'

describe('500', () => {
  let wrapper
  beforeEach(() => {
    Vue.use(vuetify)
    wrapper = shallowMount(Error500)
  })
  it('renders a vue instance', () => {
    expect(wrapper.vm).toBeTruthy()
  })
})
