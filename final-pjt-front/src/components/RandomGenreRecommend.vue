<template>
  <div class="recommend">

    <div class="movie-text">  
      <h3>랜덤 장르 추천 : {{ randomGenre }}</h3>
    </div>

    <div class="all-movie">
      <button @click="toBefore"><font-awesome-icon icon="fa-solid fa-chevron-left" /></button>
      
      <transition-group name="fade">
        <div class="movie" v-for="movie in randomGenreMovies" :key="movie.id">
          <img 
            @click="goToDetail(movie.id)"
            :src="movie.poster_URL" 
            alt="" 
            class="animate__animated animate__fadeIn"
          >
        </div>
      </transition-group>

      <button @click="toNext"><font-awesome-icon icon="fa-solid fa-chevron-right" /></button>
    </div>
    
  </div>
</template>



<script>

export default {
  name: 'RandomGenreRecommend',
  computed: {
    randomGenreMovies() {
      return this.$store.state.randomGenreMovies.slice(this.num, this.num + 5)
    },
    randomGenre() {
      return this.$store.state.randomGenre
    },
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
      if (this.num < 5) {
        this.num = this.num + 1
      }
    },
    goToDetail(id) {
      this.$router.push({ name: "movie_detail", params: { movie_id: id } });
    },
  }
}
</script>

<style scoped>


button {
  border: none;
  background-color: transparent ;
}

svg {
  font-size: 50px;
  opacity: 0.8;
  text-decoration: none;
  color: white;
  text-shadow: 2px 2px gray;
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

.movie>img {
  position: absolute;
  width: 100%;
  height: 150%;
  border: 2px solid  #E6E6E6;
  border-radius: 10px;
  object-fit: cover;
  box-shadow: 2px 2px 5px 0px rgb(44, 44, 44);
  transition: transform .4s;
}

.movie>img:hover {
  transform: scale(1.1);
  z-index: 1 !important;
}

</style>