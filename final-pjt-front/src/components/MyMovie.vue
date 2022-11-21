<template>
  <div>
    <div 
      class="feed"
      v-for="movie in movies" 
      :key="movie.id"
      @click="moveToMovie(movie.id)"
    >
      <img :src="`${movie?.poster_URL}`" alt="">
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyMovie',
  computed: {
    movies() {
      return this.$store.state.likedMovies
    }
  },
  methods: {
    moveToMovie(movieId) {
      this.$router.push({name: 'movie_detail', params: {movie_id: movieId}})
    }
  },
}
</script>

<style scoped>
div {
  text-align: left;
  position: relative;
}


.feed {
  display: inline-block;
  width: 30%;
  margin: 2px;
  padding-left: 5%;
}
.feed > img {
  width: 19vw;
  height: 19vw;
  object-fit: cover;
}
</style>