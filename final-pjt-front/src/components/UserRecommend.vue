<template>
  <div>
    <p>널 위해 준비했어</p>
    <div class="all-movie">
      <transition-group name="fade" class="movie-size">
        <div class="movie" v-for="movie in showMovies" :key="movie.id">
          <img :src="movie.poster_URL" alt="">
        </div>
      </transition-group>
    </div>
    <button @click="toBefore"><font-awesome-icon icon="fa-solid fa-chevron-left" /></button>
    <button @click="toNext"><font-awesome-icon icon="fa-solid fa-chevron-right" /></button>
    <p>{{num}}</p>
  </div>
</template>



<script>

export default {
  name: 'UserRecommend',
  computed: {
    showMovies() {
      return this.$store.state.movies.slice(this.num, this.num + 5)
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
img {
  width: 100%;
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

.all-movie {
  display: flex;
}

.movie-size {
  display: inline-block;
  width: 100%;
}
.movie {
  position: relative;
  /* padding-top: 100%; */
  overflow: hidden;
  display: inline-block;
  width: 15%;
}
</style>