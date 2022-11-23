<template>
  <div>
    <div class="sep-div">
      <MovieCard/>
      <a href="#app" @click="popReview" class="btn-review hologram-btn">리뷰 작성</a>
      <ReviewCreate v-show="popAva" @pop-exit="popExit"/>
    </div>
    <ReviewList class="sep-div"/>
    <br>
    <router-link to="/movies/" class="back">BACK</router-link>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import ReviewCreate from '@/components/ReviewCreate'
import ReviewList from '@/components/ReviewList'

export default {
  name: 'DetailView',
  components: {
    MovieCard,
    ReviewCreate,
    ReviewList,
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
  data() {
    return {
      popAva: false,
    }
  },
  methods: {
    getOneMovie(movie_id) {
      this.$store.dispatch("getOneMovie", movie_id)
    },
    getMovieReview(movie_id) {
      this.$store.dispatch("getMovieReview", movie_id)
    },
    popReview() {
      this.popAva = true
    },
    popExit() {
      this.popAva = false
    }
  },
  created() {
    this.getOneMovie(this.$route.params.movie_id)
    this.getMovieReview(this.$route.params.movie_id)
  }
}
</script>

<style lang="scss">
body {
  display: flex;
  justify-content: center;
}

.back {
  color: black;
  position: absolute;
  top: 10%;
  right: 10%;
  text-decoration: none;
  border: thick double #908581;
  border-radius: 100%;
  padding: 10px;
  color: #918d8d;
  text-shadow: 1px 1px #908581;
  background-color: rgb(255, 255, 255, 0.4);
}

.back:hover {
  color: #918d8d;
  text-shadow: 1px 1px #908581;
}



.sep-div {
  display: inline-block;
  /* position: relative; */
  text-align: left;
  width: 70%;
  height: auto;
  padding: 20px;
  margin-bottom: 50px;
}
/* .review-create {
  display: inline-block;
  width: 60%;
} */

.btn-review {
  display: inline-block;
  text-align: center;

  text-decoration: none;
  background-color:  rgb(240, 226, 215, 0.7);
  width: 90%;
  margin-left: 5%;
}

.btn-review:hover {
  color: #E6E6E6;
  font-weight: bold;
  background-color: #b2876f;
}

.hologram-btn{
  display: inline-block;
    padding: 1em 2.6em;
    border-radius: 0;
  color: #b2876f;
    margin-top:1rem;
    font-weight: bold;
    font-size: 0.8rem;
    letter-spacing: 1.5px;

    text-decoration: none;
  position: relative;
  transition: all 250ms ease;
  &:before,
  &:after{
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    border: 2px solid;
    transition: .25s;
  }
  &:before{
    transform: translateX(-.25em) translateY(.25em);
  }
  &:after{
    transform: translateX(.25em) translateY(-.25em);
  }
  
  &:hover{
    &:before,
    &:after{
      transform: translateX(0) translateY(0);
    }
  }
}
</style>