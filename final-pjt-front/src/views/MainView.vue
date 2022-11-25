<template>
  <div>
    <h1 class="top-text">Movie Memory</h1>

    <div class="weather-img">
      <span v-if="weather === 'sunny'">맑음<img :src="require(`@/assets/sun.png`)" alt="#"></span>
      <span v-else-if="weather === 'cloudy'">흐림<img :src="require(`@/assets/cloud.png`)" alt="#"></span>
      <span v-else-if="weather === 'rainy'">비<img :src="require(`@/assets/rain.png`)" alt="#"></span>
      <span v-else>눈<img :src="require(`@/assets/snow.png`)" alt="#"></span>
    </div>

    <!-- <h1 class="animate__animated animate__fadeInUp">An animated element</h1> -->
    <BannerComp :weather="weather"/>
    <UserRecommend />
    <RandomGenreRecommend />
    <NewKindRecommend />
    <WeatherRecommend />
    <SeasonRecommend />
    <GenreRecommend />
  </div>
</template>

<script>
import BannerComp from "@/components/BannerComp";
import UserRecommend from "@/components/UserRecommend";
import GenreRecommend from "@/components/GenreRecommend";
import RandomGenreRecommend from "@/components/RandomGenreRecommend";
import NewKindRecommend from "@/components/NewKindRecommend";
import WeatherRecommend from "@/components/WeatherRecommend";
import SeasonRecommend from "@/components/SeasonRecommend";

import axios from 'axios'

const API_KEY = process.env.VUE_APP_WEATHER_API_KEY


export default {
  name: "MainView",
  components: {
    BannerComp,
    UserRecommend,
    GenreRecommend,
    RandomGenreRecommend,
    NewKindRecommend,
    WeatherRecommend,
    SeasonRecommend,
  },
  data() {
    return {
      weather: null,
    }
  },
  methods: {
    getNotice() {
      this.$store.dispatch('getNotice')
    },
    getWeather() {
      axios({
        method: 'get',
        url: 'https://api.openweathermap.org/data/2.5/weather',
        params: {
          q: 'daejeon,kor',
          APPID: API_KEY,
        }
      })
        .then((response) => {
          console.log(response.data)
          const weather = response.data.weather[0].description
          if (weather ===  'clear sky') {
            this.weather = 'sunny'
          } else if (weather.includes('clouds')) {
            this.weather = 'cloudy'
          } else if (['shower rain','rain', 'thunderstorm', 'mist'].includes(weather)) {
            this.weather = 'rainy'
          } else if (weather === 'snow') {
            this.weather = 'snow'
          }
        })
    }
  },
  created() {
    this.$store.dispatch("getUserInfo");
    this.$store.dispatch("getMyGenreMovie");
    this.$store.dispatch("getRandomGenreMovie");
    this.$store.dispatch("getNewKindGenreMovie");
    this.$store.dispatch("getWeatherGenreMovie");
    this.$store.dispatch("getSeasonGenreMovie");
    setInterval(() => {
      this.getNotice()
    }, 5000);
    this.getWeather()
  },
};
</script>

<style>
.top-text {
  font-family: Harmond;
  color: black;
  text-shadow: 1.5px 1.5px #764E03;
}

.weather-img {
  position: absolute;
  top: 10px;
  right: 30px;
}

.weather-img > span > img {
  height: 50px;
}

.weather-img> span > img:hover {
  transform: scale(3) translate(-10px, 10px);
}

.recommend {
  display: inline-block;
  width: 100%;
  position: relative;
  text-align: center;
  padding: 0;
  margin: 2px;
}

.recommend:after {
  content: "";
  display: block;
  padding-bottom: 12%;
}

.recommend > div {
  text-align: center;
}
.recommend > div > h3 {
  display: inline-block;
  font-family: 'Rebecca';
  width: 70%;
  background-color: rgb(144, 133, 129, 0.5);
  padding: 11px;
  border-radius: 30px;
  font-size: 2.7vw;
}


.slide-up {
  transition: all 0.25s;
}
.slide-up-enter-active {
  transition: all 0.25s ease;
}
.slide-up-leave-active {
  transition: all 0.25s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-up-enter,
.slide-up-leave-active {
  opacity: 0;
  transform: translateY(100%);
}
</style>