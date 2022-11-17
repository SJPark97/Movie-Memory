<template>
  <span>
    <input type="text" v-model="keyword" @input="searchMovie" />
  </span>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      keyword: null,
    };
  },
  methods: {
    searchMovie(event) {
      this.$emit("search-movie", event.target.value);
    },
  },
};
</script>

<style>
.search-bar > input[type="text"] {
  display: inline-block;
  width: calc(50% - 10px * 4);
  padding-left: 30px;
  height: 50px;
  font-size: 20px;
  border-radius: 30px;
  border-style: solid;
  border-width: 1px;
  box-shadow: 1px 1px 1px 0px gray;
}
</style>