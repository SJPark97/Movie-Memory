<template>
  <div>
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
  }
}
</script>

<style>

</style>