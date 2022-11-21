<template>
  <div class="movie-card">
    <img :src="movie?.poster_URL" alt="#">
    <div class="content">
      <h1>{{ movie?.title }}</h1>
      <!-- 좋아요 수 -->
      <span @click="likeUnlike">
        <font-awesome-icon icon="fa-solid fa-heart" v-show="is_liked"/>
        <font-awesome-icon icon="fa-regular fa-heart"  v-show="!is_liked"/>
      </span>
      {{ like_users_count }}
      <!-- {{ like_count }} -->
      <p>{{ movie?.overview }}</p>
      <span v-for="(genre, index) in movie?.genres" :key="index">
        <span>{{ genre.name }} </span>
      </span>
      <p>{{ movie?.popularity }}</p>
      <p>{{ movie?.release_date }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieCard',
  computed: {
    movie() {
      return this.$store.state.movie
    },
  },
  data(){
    return {
      is_liked: false,
      like_users_count: null,
    }
  },
  methods: {
    getMovieLike(movie_id) {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${movie_id}/likes/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        }
      })
        .then((response) => {
          this.is_liked = response.data.is_liked
          this.like_users_count = response.data.like_users_count
          // const is_liked = this.is_liked
          // const like_users = this.movie.like_users
          // if (like_users.includes(this.$store.state.userId)) {
          //   const index = like_users.indexOf(this.$store.state.userId)
          //   like_users.splice(index, 1)
          // } else {
          //   like_users.push(this.$store.state.userId)
          // }
          // const payload = {
          //   is_liked, like_users
          // }
          this.$store.dispatch('getOneMovie', movie_id)
        })
        .catch((error) => {
          console.log(error)
        })
      },
    likeUnlike() {
      this.getMovieLike(this.$route.params.movie_id)
    },
  },
  created() {
    while (true) {
      if (this.$store.state.movie != null) {
        this.like_users_count = this.$store.state.movie.like_users.length
        this.like_users = this.$store.state.movie.like_users
        if (this.like_users.includes(this.$store.state.userId)) {
          this.is_liked = true
        }
        return
      }
    }
  }
}
</script>


<style scoped>


.movie-card {
  /* margin-top: 30px;
  display: inline-block;
  position: relative;
  vertical-align: top;
  justify-content: center;
  text-align: left;
  width: 100%;
  vertical-align: top; */
  display: inline-block;
  position: relative;
  text-align: left;
  width: 70%;
  height: auto;
  padding: 20px;
}

.movie-card > img {
  display: inline-block;
  width: 300px;
  margin-right: 50px;
}
/* .content {
  display: inline-block;
  width: 80%;
  margin-left: 30px;
  margin-right: 30px;

} */


.content > h1 {
  margin-bottom: 30px;
}
</style>