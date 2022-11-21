<template>
  <div>
    <MovieCard/>
    <a href="#app" @click="popReview" class="btn-review">리뷰 작성</a>
    <ReviewCreate v-show="popAva" @pop-exit="popExit"/>
    <ReviewList/>
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

.btn-review {
  color: black;
  /* border: 1px solid pink; */
  box-shadow: 1px 1px 1px 0px #908581;
  border-radius: 100%;
  padding-bottom: 25px;
  padding-top: 25px;
  padding-left: 10px;
  padding-right: 10px;
  text-decoration: none;
  background-color: rgb(218, 210, 210);
}

.review-create {
  display: inline-block;
  width: 80%;
}

.review-list {
  display: inline-block;
  width: 80%;
}

</style>