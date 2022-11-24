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
    userImg: null,
    nickname: null,
    myReviews: [],
    likedReviews: [],
    likedMovies: [],
    noti: false,
    myGenreMovies: [],
    randomGenreMovies: [],
    randomGenre: null,
    newKindGenreMovies: [],
    weatherMovies: [],
    weatherGenre: null,
    seasonMovies: [],
    seasonGenre: null,
    is_followed: false,
    followers: 0,
    followings: 0,
    newNotices: [],
    oldNotices: [],
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
      state.review = null
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
      state.userImg = null
      state.nickname = null
      state.myReviews = []
      state.likedReviews = []
      state.likedMovies = []
      state.noti = false
      state.myGenreMovies = []
      state.randomGenreMovies = []
      state.randomGenre = null
      state.newKindGenreMovies = []
      state.weatherMovies = []
      state.weatherGenre = null
      state.seasonMovies = []
      state.seasonGenre = null
      state.is_followed = false
      state.followers = 0
      state.followings = 0
      state.newNotices = []
      state.oldNotices = []
    },
    GET_USER_INFO(state, data) {
      state.userId = data.user
      state.userImg = data.img
      state.nickname = data.nick_name
    },
    MY_REVIEWS(state, reviews) {
      state.myReviews = reviews
    },
    GET_PROFILE(state, user) {
      state.user = user
    },
    USER_LIKED_MOVIE(state, movies) {
      state.likedMovies = movies
    },
    USER_LIKED_REVIEW(state, reviews) {
      state.likedReviews = reviews
    },
    GET_NOTICE(state, payload) {
      state.newNotices = payload.newNotice
      state.oldNotices = payload.oldNotice
      if (payload.newNotice == false) {
        state.noti = false
      } else {
        state.noti = true
      }
    },
    GET_MY_GENRE_MOVIE(state, movies) {
      state.myGenreMovies = movies
    },
    FIRST_FOLLOW(state, data) {
      state.is_followed = data.is_followed
      state.followers = data.followers_count
      state.followings = data.followings_count
    },
    FOLLOW(state, data) {
      state.is_followed = data.is_followed
      state.followers = data.followers_count
      state.followings = data.followings_count
    },
    GET_RANDOM_GENRE_MOVIE(state, movies) {
      state.randomGenreMovies = movies
    },
    RANDOM_MOVIE_GENRE(state, genre) {
      state.randomGenre = genre
    },
    GET_NEW_KIND_GENRE_MOVIE(state, movies) {
      state.newKindGenreMovies = movies
    },
    GET_WEATHER_MOVIE(state, movies) {
      state.weatherMovies = movies
    },
    WEATHER_MOVIE_GENRE(state, genre) {
      state.weatherGenre = genre
    },
    GET_SEASON_MOVIE(state, movies) {
      state.seasonMovies = movies
    },
    SEASON_MOVIE_GENRE(state, genre) {
      state.seasonGenre = genre
    },
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
          alert('아이디 또는 비밀번호를 잘못 입력했습니다')
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
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          // console.log(response)
          context.commit('GET_USER_INFO', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    MyReviews(context, userId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/user/${userId}/reviews/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
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
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('GET_PROFILE', response.data)
          context.dispatch('getUserInfo')
        })
        .catch((error) => {
          console.log(error)
        })
    },
    userLikedMovie(context, userId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${userId}/like_movies/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('USER_LIKED_MOVIE', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    userLikedReview(context, userId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/reviews/${userId}/like_reviews/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('USER_LIKED_REVIEW', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getNotice(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/my_notice/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          const newNotice = []
          const oldNotice = []
          for (const notice of response.data) {
            if (notice.is_checked === false) {
              newNotice.push(notice)
            } else {
              oldNotice.push(notice)
            }
          }
          const payload = {
            newNotice,
            oldNotice,
          }
          context.commit('GET_NOTICE', payload)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    visitNoti(context, id) {
      axios({
        method: 'put',
        url: `${API_URL}/accounts/user/${id}/change_notice/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.dispatch('getNotice')
        })
    },
    getMyGenreMovie(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/genres_movies/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('GET_MY_GENRE_MOVIE', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getRandomGenreMovie(context) {
      const genres = { 28: '액션', 12: '모험', 16: '애니메이션', 35: '코미디', 80: '범죄', 99: '다큐멘터리', 18: '드라마', 10751: '가족', 14: '판타지', 36: '역사', 27: '공포', 10402: '음악', 9648: '미스터리', 10749: '로맨스', 878: '공상과학', 10770: 'TV영화', 53: '스릴러', 10752: '전쟁', 37: '서부' }
      const index = [28, 12, 16, 35, 80, 99, 18, 10751, 14, 36, 27, 10402, 9648, 10749, 878, 10770, 53, 10752, 37]
      const num = Math.floor(Math.random() * 19);
      const genre = genres[index[num]]
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/genres/${index[num]}/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('GET_RANDOM_GENRE_MOVIE', response.data)
          context.commit('RANDOM_MOVIE_GENRE', genre)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getNewKindGenreMovie(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/new_kind_movies/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('GET_NEW_KIND_GENRE_MOVIE', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getWeatherGenreMovie(context) {
      const weather = { 1: '화창한', 2: '흐린', 3: '비오는', 4: '눈오는' }
      const num = Math.ceil(Math.random() * 4);
      const weather_info = weather[num]
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/weather/${num}/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('GET_WEATHER_MOVIE', response.data)
          context.commit('WEATHER_MOVIE_GENRE', weather_info)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getSeasonGenreMovie(context) {
      const season = { 1: '봄', 2: '여름', 3: '가을', 4: '겨울' }
      const num = Math.ceil(Math.random() * 4);
      const season_info = season[num]
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/season/${num}/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('GET_SEASON_MOVIE', response.data)
          context.commit('SEASON_MOVIE_GENRE', season_info)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    FirstFollow(context, userId) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/${userId}/profile/follow/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('FIRST_FOLLOW', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    follow(context, userId) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/user/${userId}/profile/follow/`,
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('FOLLOW', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  modules: {
  }
})
