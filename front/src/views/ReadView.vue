<template>
  <div>
    <SearchBar/>
    <MovieList/>
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
  }
}
</script>

<style>

</style>