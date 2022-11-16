<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <img :src="movie.poster_URL" alt="">
    <p>{{ movie.overview }}</p>
    <p>{{ movie.genres }}</p>
    <p>{{ movie.popularity }}</p>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  data() {
    return {
      movie: null,
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
    }
  },
  created() {
    this.singleMovieDetail(this.$route.params.movie_id)
  }
}
</script>

<style>
img {
  width: 300px;
}
</style>