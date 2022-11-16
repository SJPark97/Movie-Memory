<template>
  <div>
    <div class="movie-list">
      <b-card
        v-for="movie in movies" :key="movie.id"
        :img-src="movie.poster_URL"
        img-alt="Image"
        img-top
        img-size
        tag="article"
        class="movie-card"
        @click="goToDetail(movie.id)"
      >
    </b-card>
    </div>
  </div>
</template>

<script>
// import _ from 'lodash'

export default {
  name: 'MovieList',
  props: {
    movies: Array,
  },
  methods: {
    goToDetail(id) {
      this.$router.push({ name: 'movie_detail', params: {movie_id: id}})
    }
  }
}
</script>

<style lang="scss" scoped>
.movie-list {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin-left: 10%;
  margin-right: 10%;
  position: absolute;
}

.movie-card {
  display: inline-block;
  padding: 0;
  height: 15rem;
  width: 10rem;
  font-size: 5px;
  margin-top: 15px;
  margin-bottom: 15px;
  margin-left: 1%;
  margin-right: 1%;
  // border: 1px solid gray;
  box-shadow: 2px 2px 5px 0px rgb(27, 26, 26);
  transition: transform .2s;
}

.movie-card:hover {
  cursor: pointer;
  transform: scale(1.3);
  z-index: 1 !important;

}

.movie-card>img {
  height: 100%;
}




</style>