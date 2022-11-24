<template>
  <div class="all-movies">
      <b-card
        v-for="movie in movies" :key="movie.id"
        :img-src="movie.poster_URL"
        img-alt="Image"
        img-top
        img-size
        tag="article"
        class="movie-card"
        @click="goToDetail(movie.id)"
        scrollable
      >
      </b-card>
  </div>
</template>

<script>
// import _ from 'lodash'

export default {
  name: 'MovieList',
  props: {
    movies: Array,
  },
  data() {
    return {
      topicData: [],
      limit: 0,
    }
  },
  computed: {
    rows() {
        return this.movies.length
      }
  },
  methods: {
    goToDetail(id) {
      this.$router.push({ name: 'movie_detail', params: {movie_id: id}})
      .then((() =>window.scrollTo(0,0) ))
    }
  },
}
</script>

<style lang="scss" scoped>

.all-movies {
  padding-left: 50px;
  padding-right: 50px;
}
.movie-list {
  // background-color: rgba(255, 255, 255, 0.2);
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
  flex-grow: 1;
  flex-shrink: 0;
  margin-top: 100px;
  margin-left: 15%;
  margin-right: 15%;
  // position: fixed;
  // width: 80%;
  height: auto;
  overflow-y: auto;
}

.movie-card {
  display: inline-block;
  flex: 1 1 1 30%;
  padding: 0;
  height: 15rem;
  width: 10rem;
  font-size: 5px;
  margin-top: 15px;
  margin-bottom: 15px;
  margin-left: 20px;
  margin-right: 20px;
  // border: 1px solid gray;
  box-shadow: 2px 2px 5px 0px rgb(44, 44, 44);
  transition: transform .2s;
}

.movie-card:hover {
  transform: scale(1.2);
  z-index: 1 !important;
}

.movie-card>img {
  height: 100%;
}


</style>