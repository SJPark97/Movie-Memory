<template>
  <div>
    <h1>Hello,{{ $store.state.username }}</h1>
    <h1 class="animate__animated animate__fadeInUp">An animated element</h1>
    <NowWeather/>
    <BannerComp/>
    <UserRecommend/>
    <GenreRecommend/>
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
}
</script>

<style>
</style>