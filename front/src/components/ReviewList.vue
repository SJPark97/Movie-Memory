<template>
  <div class="review-list">
    <h1 style="margin-bottom: 500px">리뷰리스트가 들어갈 자리^^</h1>
    <div v-for="review in reviews" :key="review.id">
      <img :src="review?.img" alt="">
      <h1>{{ review?.title }}</h1>
      <p>작성일시 : {{ review?.created_at }}</p>
      <p>수정일시 : {{ review?.updated_at }}</p>
      <p>{{ review.content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewList',
  computed: {
    reviews() {
      return this.$store.state.reviews
    }
  },
  data() {
    return {
      thisMovieReview: [],
    }
  },
  methods: {
    // getMovieReview() {
    //   for (const review of this.reviews) {
    //     if (review.movie)
    //   }
    // }
  }
}
</script>

<style>

</style>