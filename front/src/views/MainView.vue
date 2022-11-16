<template>
  <div>
    <h1>Hello,{{ username }}</h1>
    <p>Today is Sunny day :)</p>
    <BannerComp/>
    <UserRecommend/>
    <GenreRecommend/>
    <NowWeather/>
  </div>
</template>

<script>
import BannerComp from '@/components/BannerComp'
import UserRecommend from '@/components/UserRecommend'
import GenreRecommend from '@/components/GenreRecommend'
import NowWeather from '@/components/NowWeather'

export default {
  name: 'MainView',
  components: {
    BannerComp,
    UserRecommend,
    GenreRecommend,
    NowWeather,
  },
  computed: {
    username() {
      return this.$store.state.username
    }
  }
}
</script>

<style>

</style>