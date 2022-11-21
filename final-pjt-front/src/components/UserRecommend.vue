<template>
  <div>
    <div class="movie-text">  
      <h3>{{ this.$store.state.username }}님이 선호하는 장르의 영화</h3>
    </div>
    <div class="all-movie">
      <button @click="toBefore"><font-awesome-icon icon="fa-solid fa-chevron-left" /></button>
      <transition-group name="fade" class="movie-size" >
        <div class="movie" v-for="movie in myGenreMovies" :key="movie.id">
          <img :src="movie.poster_URL" alt="" class="animate__animated animate__fadeIn">
        </div>
      </transition-group>
      <button @click="toNext"><font-awesome-icon icon="fa-solid fa-chevron-right" /></button>
    </div>
  </div>
</template>



<script>

export default {
  name: 'UserRecommend',
  computed: {
    myGenreMovies() {
      return this.$store.state.myGenreMovies.slice(this.num, this.num + 5)
    }
  },
  data() {
    return {
      showLink: true,
      num: 0,
    }
  },
  methods: {
    toBefore() {
      if (this.num > 0) {
        this.num = this.num - 1
      }
    },
    toNext() {
      this.num = this.num + 1
    }
  }
}
</script>

<style scoped>

div {
  width: 100%;
}
h3 {
  text-align: left;
}
img {
  width: 100%;
  height: 100%;
  /* height: auto; */
  /* position: absolute;
  top:0;
  left:0;
  right:0;
  bottom:0; */
  object-fit: cover;
}

button {
  border: none;
  background-color: transparent ;
}

svg {
  font-size: 40px;
  opacity: 0.8;
  text-decoration: none;
  color: white;
  text-shadow: 2px 2px gray;
}

.movie-text {
  display: inline-block;
  width: 1200px;
  background-color: rgba(255, 255, 255, 0.4);
}

.all-movie {
  display: flex;
  justify-content: center;
}

.movie-size {
  display: inline-block;
}
.movie {
  /* position: relative; */
  /* padding-top: 100%; */
  /* overflow: hidden; */
  /* display: inline-block; */
  /* width: 15%; */
  display: inline-block;
  flex: 1 1 1 30%;
  padding: 0;
  height: 21rem;
  width: 14rem;
  font-size: 5px;
  margin-top: 15px;
  margin-bottom: 15px;
  margin-left: 10px;
  margin-right: 10px;
  box-shadow: 2px 2px 5px 0px rgb(44, 44, 44);
  transition: transform .4s;
  cursor: pointer;
}

/* .movie:hover {
  cursor: pointer;
  transform: scale(1.2);
  z-index: 1 !important;
} */
.movie>img {
  height: 100%;
}

</style>