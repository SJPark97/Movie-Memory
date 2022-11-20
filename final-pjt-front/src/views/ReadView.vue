<template>
  <div>
    <header>
      <SearchBar @search-movie="searchMovie" class="search-bar" />
      <span class="sort-selector">
        <button @click="selectA" :class="{'select-on': selected === 'A'}">인기</button>
        <button @click="selectB" :class="{'select-on': selected === 'B'}">최신</button>
      </span>
    </header>
    <MovieList
      :movies="movieList"
    />
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar";
import MovieList from "@/components/MovieList";

export default {
  name: "ReadView",
  components: {
    SearchBar,
    MovieList,
  },
  data() {
    return {
      selected: "A",
      searchYes: false,
      movieList: [],
    };
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
  },
  methods: {
    selectA() {
      this.selected = 'A'
      this.sortMovies()
    },
    selectB() {
      this.selected = 'B'
      this.sortMovies();
    },
    sortMovies() {
      if (this.selected === "A") {
        if (!this.searchYes) {
          this.movieList = this.movies;
        }
        this.movieList.sort((a, b) => {
          return b.popularity - a.popularity;
        });
      } else {
        if (!this.searchYes) {
          this.movieList = this.movies;
        }
        this.movieList.sort((a, b) => {
          return b.release_date.localeCompare(a.release_date);
        });
      }
    },
    searchMovie(keyword) {
      const movies = this.movies.filter((movie) => {
        return movie.title.includes(keyword);
      });
      if (movies) {
        this.movieList = movies;
        this.searchYes = true;
      }
    },
  },
  created() {
    this.sortMovies();
  },
};
</script>

<style lang="scss" scoped>
// body {
//   padding-top: 100px;
//   justify-content: center;
// }

header {
  // position: fixed;
  top: 0;
  left: 0;
  right: 0;
  padding: 1rem;
}

.search-bar {
  /* display: inline-block; */
  margin-bottom: 3px;
  /* width: 30%; */
  /* height: 50px; */
}

.sort-selector {
  display: inline-block;
  /* text-align: center; */
  width: 130px;
  height: 50px;
  font-size: 1.5rem;
}

button {
  display: inline-block;
  font-size: 15px;
  width: 45px;
  height: 40px;
  margin-right: 3px;
  box-shadow: 1px 1px #908581;
  border: 1px solid rgb(204, 204, 204);
  border-radius: 100px;
  background-color: #E6E6E6;
}

.select-on { 
  background-color: #F0E2D7;
  font-weight: bold;
}


</style>