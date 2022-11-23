<template>
  <div>
    <div class="sep-div">
      <MovieCard/>
      <a href="#app" @click="popReview" class="btn-review">리뷰 작성</a>
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

<style>
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


.btn-review {
  display: inline-block;
  text-align: center;
  color: black;
  /* border: 1px solid pink; */
  box-shadow: 1px 1px 1px 0px #908581;
  border-radius: 30px;
  padding-bottom: 10px;
  padding-top: 10px;
  text-decoration: none;
  background-color:  rgb(240, 226, 215, 0.7);
  width: 100%;
  /* margin-right: 5%; */
  /* margin-left: 5%; */
  font-size: 1.5vw;
}

.btn-review:hover {
  color: black;
  font-weight: bold;
}



.sep-div {
  display: inline-block;
  /* position: relative; */
  text-align: left;
  width: 80%;
  height: auto;
  padding: 20px;
}

.review-create {
  display: inline-block;
  width: 60%;
}



</style>