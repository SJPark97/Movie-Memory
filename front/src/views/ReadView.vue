<template>
  <div>
    <header>
      <SearchBar @search-movie="searchMovie" class="search-bar"/>
      <span class="sort-selector" >
        <b-form-group v-slot="{ ariaDescribedby }">
          <b-form-radio @change="sortMovies" v-model="selected" value="A" :aria-describedby="ariaDescribedby" name="some-radios" >인기순</b-form-radio>
          <b-form-radio @change="sortMovies" v-model="selected" value="B" :aria-describedby="ariaDescribedby" name="some-radios" >최신순</b-form-radio>
        </b-form-group>
      </span>
    </header>
    <MovieList :movies="movieList" class="animate__animated animate__fadeInUp"/> 

  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import MovieList from '@/components/MovieList'

export default {
  name: 'ReadView',
  components: {
    SearchBar,
    MovieList,
  },
  data() {
    return {
      selected: 'A',
      searchYes: false,
      movieList: [],
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  methods: {
    sortMovies() {
      if (this.selected === 'A') {
        if (! this.searchYes) {
          this.movieList = this.movies
        } 
        this.movieList.sort((a, b) => {
          return b.popularity - a.popularity
        })
      } else { 
        if (!this.searchYes) {
          this.movieList = this.movies
        }
        this.movieList.sort((a, b) => {
          return b.release_date.localeCompare(a.release_date)
      })
      }
    },
    searchMovie(keyword) {
      const movies = this.movies.filter((movie) => {
        return movie.title.includes(keyword)
      })
      if (movies) {
        this.movieList = movies
        this.searchYes = true
      }
    }
  },
  created() {
    this.sortMovies()
  }
}
</script>

<style lang="scss" scoped>

body {
  padding-top: 100px;
  justify-content: center;
  background-color: black;
}

header {
  position: fixed;
  top: 0;
  left:0;
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
  width: 100px;
  height: 50px;
  font-size: 1.5rem;
}
</style>