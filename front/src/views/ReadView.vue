<template>
  <div >
    <SearchBar @search-movie="searchMovie"/>
    <span class="sort-selector">
      <b-form-group v-slot="{ ariaDescribedby }">
        <b-form-radio  @change="SortFamous" v-model="selected" value="A" :aria-describedby="ariaDescribedby" name="some-radios" >인기순</b-form-radio>
        <b-form-radio  @change="SortCurrent" v-model="selected" value="B" :aria-describedby="ariaDescribedby" name="some-radios" >최신순</b-form-radio>
      </b-form-group>
    </span>
    <MovieList :movies="movieList"/>
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
    SortFamous() {
      if (! this.searchYes) {
        this.movieList = this.movies
      } 
      this.movieList.sort((a, b) => {
        return b.popularity - a.popularity
      })
    },
    SortCurrent() {
      if (!this.searchYes) {
        this.movieList = this.movies
      }
      this.movieList.sort((a, b) => {
        return b.release_date.localeCompare(a.release_date)
      })
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
    this.SortFamous()
  }
}
</script>

<style>

.search-bar {
  /* display: inline-block; */
  margin-bottom: 3px;
  /* width: 30%; */
  /* height: 50px; */
  /* display: flex;
  justify-content: center; */
}

.search-bar>input[type=text] {
  display: inline-block;
  width: calc(50% - 10px * 3);
  padding-left: 30px;
  height: 50px;
  font-size: 20px;
  border-radius: 30px;
  border-style: solid;
  border-width: 1px;
  box-shadow: 1px 1px 1px 0px gray;
}

.sort-selector {
  display: inline-block;
  /* text-align: center; */
  width: 100px;
  height: 50px;
  font-size: 1.5rem;
}
</style>