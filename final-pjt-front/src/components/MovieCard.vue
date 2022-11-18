<template>
  <div class="movie-card">
    <h1>{{ movie?.title }}</h1>
    <img :src="movie?.poster_URL" alt="">
    <p>{{ movie?.overview }}</p>
    <div v-for="(genre, index) in movie?.genres" :key="index">
      <span>{{ genre.name }}</span>
    </div>
    <p>{{ movie?.popularity }}</p>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  computed: {
    movie() {
      return this.$store.state.movie
    }
  }
}
</script>

<style>
img {
  width: 300px;
}
</style>