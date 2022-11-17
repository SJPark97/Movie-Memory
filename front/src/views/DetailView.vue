<template>
  <div>
    <MovieCard :movie="movie"/>
    <ReviewCreate/>
    <ReviewList :reviews="thisMovieReview"/>
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
    reviews() {
      return this.$store.state.reviews
    }
  },
  data() {
    return {
      movie: null,
      thisMovieReview: [],
    }
  },
  methods: {
    singleMovieDetail(id) {
      for (const movie of this.movies) {
        if(movie.id === Number(id)) {
          this.movie = movie
          break
        }
      }
    },
    getMovieReview() {
      const thisReviews = this.reviews.filter((review) => {
        return review.movie === this.movie.id
      })
      this.thisMovieReview = thisReviews
      console.log(this.thisMovieReview)
    }
  },
  created() {
    this.singleMovieDetail(this.$route.params.movie_id)
    this.getMovieReview()
  }
}
</script>

<style>
body {
  display: flex;
  justify-content: center;
}

.movie-card {
  display: inline-block;
  width: 80%;
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