<template>
  <div>
    <p>오늘의 날씨는?</p>
    <p>{{ weather }}</p>

  </div>
</template>


<!-- VUE_APP_WEATHER_API_KEY=4fb4e5763cb97001341a93c1a5bd0b20 -->
<script>

// import _ from 'lodash'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_WEATHER_API_KEY

export default {
  name: 'NowWeather',
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  data() {
    return {
      weatherMovieList: null,
      weather: null,
    }
  },
  methods: {
    weatherPick() {
      axios({
        method: 'get',
        url: 'https://api.openweathermap.org/data/2.5/weather',
        params: {
          q: 'Seoul,kor',
          APPID: API_KEY,
        }
      })
        .then((response) => {
          this.weather = response.data.weather[0].description
        })
    },
    weatherMovies() {
      if (this.weather === 'clear sky') {
        const sunny = this.movies.filter((movie) => {
          return movie.weather === 1
        })
        this.weatherMovieList = sunny
      } else if (this.weather in ['few clouds', 'scattered clouds', 'broken clouds']) {
        const cloudy = this.movies.filter((movie) => {
          return movie.weather === 2
        })
        this.weatherMovieList = cloudy
      } else if (this.weather in  ['shower rain','rain', 'thunderstorm', 'mist']) {
        const rainy = this.movies.filter((movie) => {
          return movie.weather === 3
        })
        this.weatherMovieList = rainy
      } else if (this.weather === 'snow') {
        const snow = this.movies.filter((movie) => {
          return movie.weather === 4
        })
        this.weatherMovieList = snow
      }
    }
  },
  created() {
    this.weatherPick()
    this.weatherMovies()
  }
}
</script>

<style>
</style>