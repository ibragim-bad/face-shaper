import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    photo: null,
    suggestion: null,
    loading: false,
    error: null,
    rotate: {
      rotateDeg: 0,
    }
  },
  getters: {
    photo(state) {
      return state.photo
    },
    isPhoto(state) {
      return !!state.photo
    },
    rotateDeg(state) {
      return state.rotate.rotateDeg
    },
    loading(state) {
      return state.loading
    },
    error(state) {
      return state.error
    },
    suggestion(state) {
      return state.suggestion
    },
    isSuggestion(state) {
      return !!state.suggestion
    },
  },
  mutations: {
    setPhoto(state, payload) {
      state.photo = payload
    },
    setSuggestion(state, payload) {
      state.suggestion = payload
    },
    setLoading(state, payload) {
      state.loading = payload
    },
    setError(state, payload) {
      state.error = payload
    },
    setRotateDeg(state, payload) {
      state.rotate.rotateDeg = payload
    },
  },
  actions: {
    setRotateDeg({commit}, payload) {
      commit('setRotateDeg', payload)
    },
    setPhoto({commit}, payload) {
      commit('setPhoto', payload)
    },
    setSuggestion({commit}, payload) {
      commit('setSuggestion', payload)
    },
    setLoading({commit}, payload) {
      commit('setLoading', payload)
    },
    setError({commit}, payload) {
      commit('setError', payload)
    },
    sendPhoto({dispatch, getters}, formData) {
      const URL = "api/upload"
      formData.append("rotate", getters.rotateDeg)
      const options = {
        method: "POST",
        body: formData
      }
      dispatch('setError', null)
      dispatch('setLoading', true)
      return fetch(URL, options)
      .then(response => {
        // console.log(response)
        // alert(response.status)
        // alert(response.statusText)
        // alert(response.url)
        return response.json()
      })
      .then(response => {
          dispatch('setLoading', false)
          dispatch('setSuggestion', response)
          dispatch('setPhoto', null)
        })
        .catch(error => {
          console.log(error)
          dispatch('setLoading', false)
          dispatch('setError', error)
        })
    }
  }
})
