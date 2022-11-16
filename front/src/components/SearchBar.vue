<template>
  <span class="search-bar">
    <input type="text" v-model="keyword" @input="searchMovie">
  </span>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      keyword: null,
    }
  },
  methods: {
    searchMovie(event) {
      this.$emit('search-movie', event.target.value)
    }
  }
}
</script>

<style>

</style>