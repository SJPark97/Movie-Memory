import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    movies: [],
    reviews: [],
    username: null,
  },
  getters: {
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name: 'main'})
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
    LogIn(state, username) {
      state.username = username
    },
    LOGOUT(state) {
      state.token = null
      state.username = null
    }
  },
  actions: {
    SignUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((response) => {
          context.commit('SAVE_TOKEN', response.data.key)
          context.commit('LogIn', username)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((response) => {
          context.commit('SAVE_TOKEN', response.data.key)
          context.commit('LogIn', username)
        })
        .catch((error) => {
          console.log(error)
          alert('응 돌아가~')
        })
    },
    getMovies(context) {
      axios({
        mathod: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((response) => {
          context.commit('GET_MOVIES', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getReviews(context) {
      axios({
        mathod: 'get',
        url: `${API_URL}/api/v1/reviews`,
      })
        .then((response) => {
          context.commit('GET_REVIEWS', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  modules: {
  }
})
