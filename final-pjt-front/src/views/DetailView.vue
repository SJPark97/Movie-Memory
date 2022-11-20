<template>
  <div>
    <MovieCard/>
    <p @click="popReview">리뷰 등록</p>
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

.review-create {
  display: inline-block;
  width: 80%;
}

.review-list {
  display: inline-block;
  width: 80%;
}

</style>