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
  // methods: {
  //   getUserInfo() {
  //     this.$store.dispatch("getUserInfo")
  //   }
  // },
  created() {
    this.$store.dispatch("getUserInfo")
    this.$store.dispatch("getMyGenreMovie")
  }
}
</script>

<style>

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