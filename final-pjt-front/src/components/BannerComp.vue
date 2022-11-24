<template>
  <div>
    <div class="slide">

      <b-carousel
        id="carousel-no-animation"
        no-animation
        indicators
        controls
        v-model="slide"
        :interval="4000"
        img-width="256"
        img-height="120"
        class="display-1"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <b-carousel-slide
          :img-src="require(`@/assets/winter-shadow.png`)"
          
          >
          <h2 class="winter">WINTER</h2>
        </b-carousel-slide>

        <b-carousel-slide
          :img-src="require(`@/assets/sunny-shadow.png`)"
        >
        <h2 class="sunny">SUNNY</h2>
        </b-carousel-slide>

        <b-carousel-slide
          :img-src="require(`@/assets/cloudy-shadow.png`)"
        >
        <h2 class="cloudy">CLOUDY</h2>
        </b-carousel-slide>

        <b-carousel-slide
          :img-src="require(`@/assets/rainy-shadow.png`)"
        >
        <h2 class="rainy">RAINY</h2>
        </b-carousel-slide>

        <b-carousel-slide
          :img-src="require(`@/assets/snow-shadow.png`)"
        >
        <h2 class="snow">SNOW</h2>
        </b-carousel-slide>

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

div {
  margin-bottom: 70px;
}
.slide {
  position: relative;
  display: inline-block;
  width: 80vw;
  height: 30vw;
}

h2 { 
  display: inline-block;
  text-align: left;
  position: absolute;
  top: -35vw;
  left: -5vw;
  font-size: 10vw;
  font-family: Harmond;
  color: white;
  text-shadow: 2px 2px #764E03;
}

.winter {
  top: -35vw;
  left: 5vw;
  color: rgb(255, 255, 255, 0.85);
  text-shadow: 2px 2px #764E03;
}

.sunny {
  font-size: 11vw;
  top: -33vw;
  left: -5vw;
  color: rgb(255, 255, 255, 0.9);
  text-shadow: 2.5px 2px  #5e1819a2;
}

.cloudy {
  font-size: 9.5vw;
  top: -10vw;
  left: -8vw;
  color: rgb(180, 186, 210, 0.8);
  text-shadow: 2px 2px rgba(218, 72, 53, 0.774);
}


.rainy {
  font-size: 10.5vw;
  top: -10vw;
  left: 25vw;
  color: rgb(233, 179, 193, 0.8);
  text-shadow: 2px 2px rgb(177, 168, 168, 0.8);
}

.snow {
  top: -10vw;
  left: 9vw;
  color: rgba(143, 93, 150, 0.651) ;
  text-shadow: 2px 2px #eed4eed3;
}





</style>