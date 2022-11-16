import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

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
  },
  getters: {
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
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
          console.log(response)
          context.commit('SAVE_TOKEN', response.data.key)
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
          console.log(response)
          context.commit('SAVE_TOKEN', response.data.key)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMovies(context) {
      axios({
        mathod: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((response) => {
          console.log(response, context)
          context.commit('GET_MOVIES', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // createReview(context, payload) {
    //   const moviePk = payload.moviePk
    //   const title = payload.title
    //   const content = payload.content
    //   const imgFile = payload.imgFile

    //   newReview = {
    //     title, content, imgFile
    //   }

    //   this.$commit('CREATE_REVIEW')
    // }
  },
  modules: {
  }
})
