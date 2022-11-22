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
  margin-left: 4%;
}


.feed {
  display: inline-block;
  width: 30%;
  margin: 2px;
  margin: 5px;
}

.feed:after {
  content: "";
  display: block;
  padding-bottom: 100%;
}

.feed > img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>