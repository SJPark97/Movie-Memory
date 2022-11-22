<template>
  <div class="recommend">
    <div class="movie-text">
      <h3>{{ this.$store.state.nickname }}님이 선호하는 장르의 영화</h3>
    </div>

    <div class="all-movie">
      <button @click="toBefore">
        <font-awesome-icon icon="fa-solid fa-chevron-left" />
      </button>
      <transition-group name="fade">
        <div class="movie" v-for="movie in myGenreMovies" :key="movie.id">
          <img
            @click="goToDetail(movie.id)"
            :src="movie.poster_URL"
            alt=""
            class="animate__animated animate__fadeIn"
          />
        </div>
      </transition-group>
      <button @click="toNext">
        <font-awesome-icon icon="fa-solid fa-chevron-right" />
      </button>
    </div>
  </div>
</template>



<script>
export default {
  name: "UserRecommend",
  computed: {
    myGenreMovies() {
      return this.$store.state.myGenreMovies.slice(this.num, this.num + 5);
    },
  },
  data() {
    return {
      showLink: true,
      num: 0,
    };
  },
  methods: {
    toBefore() {
      if (this.num > 0) {
        this.num = this.num - 1;
      }
    },
    toNext() {
      if (this.num < 15) {
        this.num = this.num + 1;
      }
    },
    goToDetail(id) {
      this.$router.push({ name: "movie_detail", params: { movie_id: id } });
    },
  },
};
</script>

<style scoped>
h3 {
  /* text-align: left; */
}

button {
  border: none;
  background-color: transparent;
}

svg {
  font-size: 50px;
  opacity: 0.8;
  text-decoration: none;
  color: white;
  text-shadow: 2px 2px gray;
}

.movie-text {
  /* display: inline-block;
  width: 1200px;
  background-color: rgba(255, 255, 255, 0.4); */
}

.movie {
  display: inline-block;
  width: 15%;
  position: relative;
  text-align: left;
  padding: 0;
  margin: 2px;
}

.movie:after {
  content: "";
  display: block;
  padding-bottom: 100%;
}

.movie > img {
  position: absolute;
  width: 100%;
  height: 150%;
  border: 2px solid #e6e6e6;
  border-radius: 10px;
  object-fit: cover;
  box-shadow: 2px 2px 5px 0px rgb(44, 44, 44);
  transition: transform 0.4s;
}

.movie > img:hover {
  cursor: pointer;
  transform: scale(1.1);
  z-index: 1 !important;
}

.actions {
  position: absolute;
  bottom: 25px;
  left: 50%;
  transform: translateX(-50%);
}

.animate__fadeIn {
  /* animation-delay: 0.2s; */
  animation-duration: 1s;
}
</style>