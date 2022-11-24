<template>
  <span>
    <input type="text" v-model="keyword" @input="searchMovie" />
    <font-awesome-icon class="search-icon" icon="fa-solid fa-magnifying-glass" />
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

<style scoped>
.search-bar {
  position: relative;
}
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

.search-icon {
  position: absolute;
  left: calc(100% - 10px * 4);
  top: 1px;
  font-size: 23px;
  color: rgb(87, 86, 86);
}
</style>