<template>
  <div>
    <SearchBar/>
    <div>
      <b-form-group v-slot="{ ariaDescribedby }">
        <b-form-radio v-model="selected" :aria-describedby="ariaDescribedby" name="some-radios" value="A">인기순</b-form-radio>
        <b-form-radio v-model="selected" :aria-describedby="ariaDescribedby" name="some-radios" value="B">최신순</b-form-radio>
      </b-form-group>
    </div>

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
  },
  data() {
    return {
      selected: null,
    }
  }
}
</script>

<style>
</style>