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
    movie: null,
    reviews: [],
    movieReviews: [],
    reviewComments: [],
    review: null,
    comment: null,
    username: null,
    user: [],     // 프로필에 사용 -> 유저 아이디마다 바뀌어야 함
    userId: null,
    myReviews: [],
  },
  getters: {
  },
  mutations: {
    SIGNUP_SAVE_TOKEN(state, token) {
      state.token = token
    },
    LOGIN_SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'main' })
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_ONE_MOVIE(state, movie) {
      state.movie = movie
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
    GET_MOVIE_REVIEWS(state, reviews) {
      if (reviews === 'error') {
        state.movieReviews = null
      } else {
        state.movieReviews = reviews
      }
    },
    GET_ONE_REVIEW(state, review) {
      state.review = review
      // state.reviewComments = null
    },
    GET_REVIEW_COMMENTS(state, comments) {
      state.reviewComments = comments
    },
    NO_COMMENTS(state) {
      state.reviewComments = null
    },
    // GET_ONE_COMMENT(state, comment) {
    //   console.log(comment)
    // },
    LogIn(state, username) {
      state.username = username
    },
    LOGOUT(state) {
      state.token = null
      state.username = null
      state.userId = null
    },
    GET_USER_INFO(state, data) {
      state.userId = data.user
    },
    MY_REVIEWS(state, reviews) {
      state.myReviews = reviews
    },
    GET_PROFILE(state, user) {
      state.user = user
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
          context.commit('SIGNUP_SAVE_TOKEN', response.data.key)
          context.commit('LogIn', username)
        })
        .catch((error) => {
          console.log(error)
          alert('사용할 수 없는 아이디입니다.')
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
          context.commit('LOGIN_SAVE_TOKEN', response.data.key)
          context.commit('LogIn', username)
        })
        .catch((error) => {
          console.log(error)
          alert('응 돌아가~')
        })
    },
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((response) => {
          context.commit('GET_MOVIES', response.data)
        })
        .catch((error) => {
          console.log('getMovies', error)
        })
    },
    getOneMovie(context, movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/`,
      })
        .then((response) => {
          context.commit('GET_ONE_MOVIE', response.data)
        })
        .catch((error) => {
          console.log('getOneMovies', error)
        })
    },
    getReviews(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/reviews/`,
      })
        .then((response) => {
          context.commit('GET_REVIEWS', response.data)
        })
        .catch((error) => {
          console.log('getReviews', error)
        })
    },
    getMovieReview(context, movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/reviews/`,
      })
        .then((response) => {
          context.commit('GET_MOVIE_REVIEWS', response.data)
        })
        .catch((error) => {
          console.log('getMovieReviews', error)
          context.commit('GET_MOVIE_REVIEWS', "error")
        })
    },
    getOneReview(context, reviewId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/reviews/${reviewId}/`,
      })
        .then((response) => {
          context.commit('GET_ONE_REVIEW', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getReviewComment(context, reviewId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/reviews/${reviewId}/comments/`,
      })
        .then((response) => {
          context.commit('GET_REVIEW_COMMENTS', response.data)
        })
        .catch((error) => {
          context.commit('NO_COMMENTS')
          console.log(error)
        })
    },
    getOneComment(context, commentId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/comments/${commentId}`,
      })
        .then((response) => {
          context.commit('GET_ONE_COMMENT', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getUserInfo(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/myprofile/`,
        headers: {
          'Authorization' : `Token ${context.state.token}`
        }
      })
        .then((response) => {
          // console.log(response)
          context.commit('GET_USER_INFO', response.data)
        })
        .catch((error) => {
          console.log( error)
        })
    },
    MyReviews(context, userId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/user/${userId}/reviews/`,
        headers: {
          'Authorization' : `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('MY_REVIEWS', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getProfile(context, userId) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/${userId}/profile/`,
        headers: {
          'Authorization' : `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('GET_PROFILE', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  modules: {
  }
})
