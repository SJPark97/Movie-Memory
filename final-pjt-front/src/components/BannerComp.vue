<template>
  <div>
    <div class="slide">
      <!-- https://bootstrap-vue.org/docs/components/carousel -->
      <b-carousel
        id="carousel-no-animation"
        style="text-shadow: 1px 1px 2px #333;"
        no-animation
        controls
        indicators
        v-model="slide"
        :interval="4000"
        img-width="256"
        img-height="120"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <b-carousel-slide
          caption="겨울이다...춥다..."
          img-src="https://picsum.photos/1024/480/?image=10"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="오늘 날씨가 참 좋네요"
          img-src="https://picsum.photos/1024/480/?image=12"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="이런 영화 좋아하시죠?"
          img-src="https://picsum.photos/1024/480/?image=22"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="아니면 이거?"
          img-src="https://picsum.photos/1024/480/?image=23"
        ></b-carousel-slide>
      </b-carousel>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';


export default {
  name: 'BannerComp',
  computed: {
    // 근데 현재 날씨에 맞는 추천 영화가 들어가면 좋음 (계절도 마찬가지)
    weatherMovie() {
      return _.sample(this.$store.state.weatherMovies)
    },
    seasonMovie() {
      return _.sample(this.$store.state.seasonMovies)
    }
  },
  data() {
    return {
      slide: 0,
      sliding: null
    }
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true
    },
    onSlideEnd(slide) {
      this.sliding = false
    }
  }
  
}
</script>

<style scoped>
.slide {
  display: inline-block;
  width: 80%;
  margin-bottom: 50px;
}
</style>