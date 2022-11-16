<template>
  <div>
    <SearchBar/>
    <div class="sort-selector">
      <b-form-group v-slot="{ ariaDescribedby }">
        <b-form-radio  @change="SortFamous" v-model="selected" value="A" :aria-describedby="ariaDescribedby" name="some-radios" >인기순</b-form-radio>
        <b-form-radio  @change="SortCurrent" v-model="selected" value="B" :aria-describedby="ariaDescribedby" name="some-radios" >최신순</b-form-radio>
      </b-form-group>
    </div>
    <MovieList :movies="movies"/>
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
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  methods: {
    SortFamous() {
      console.log(this.selected)
      this.movies.sort((a, b) => {
        return b.popularity - a.popularity
      })
    },
    SortCurrent() {
      this.movies.sort((a, b) => {
        return b.release_date.localeCompare(a.release_date)
      })
    }
  },
  created() {
    this.SortFamous()
  }
}
</script>

<style>

.sort-selector {
  display: inline-block;
}

</style>