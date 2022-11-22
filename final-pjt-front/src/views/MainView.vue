<template>
  <div>
    <h1>Hello,{{ $store.state.username }}</h1>
    <h1 class="animate__animated animate__fadeInUp">An animated element</h1>
    <NowWeather />
    <BannerComp />
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
import NowWeather from "@/components/NowWeather";

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
    NowWeather,
  },
  // methods: {
  //   getUserInfo() {
  //     this.$store.dispatch("getUserInfo")
  //   }
  // },
  created() {
    this.$store.dispatch("getUserInfo");
    this.$store.dispatch("getMyGenreMovie");
    this.$store.dispatch("getRandomGenreMovie");
    this.$store.dispatch("getNewKindGenreMovie");
    this.$store.dispatch("getWeatherGenreMovie");
    this.$store.dispatch("getSeasonGenreMovie");
  },
};
</script>

<style>


.recommend {
  display: inline-block;
  width: 100%;
  position: relative;
  text-align: left;
  padding: 0;
  margin: 2px;
}

.recommend:after {
  content: "";
  display: block;
  padding-bottom: 10%;
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