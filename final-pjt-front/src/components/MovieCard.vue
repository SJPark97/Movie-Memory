<template>
  <div class="movie-card">
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
  props: {
    movie: Object,
  }
}
</script>

<style>
img {
  width: 300px;
}
</style>