<template>
  <div class="movie-card">
    <img :src="movie?.poster_URL" alt="">
    <div class="content">
      <h1>{{ movie?.title }}</h1>
      <p>{{ movie?.overview }}</p>
      <div v-for="(genre, index) in movie?.genres" :key="index">
        <span>{{ genre.name }}</span>
      </div>
      <p>{{ movie?.popularity }}</p>
    </div>
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

<style scoped>
.movie-card {
  display: inline-block;
  text-align: left;
  width: 80%;
  vertical-align: top;
}


.movie-card > img {
  display: inline-block;
  width: 30%;
}

.content {
  display: inline-block;
  width: 50%;
}
</style>