<template>
  <div>
    <div 
      class="feed"
      v-for="review in reviews" 
      :key="review.id"
      @click="moveToReview(review.id)"
    >
      <img :src="`http://127.0.0.1:8000${review?.img}`" alt="">
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyReview',
  computed: {
    reviews() {
      return this.$store.state.myReviews
    }
  },
  methods: {
    moveToReview(reviewId) {
      this.$router.push({name: 'review_detail', params: {review_id: reviewId}})
    }
  },
}
</script>

<style scoped>
div {
  text-align: left;
  position: relative;
}

.feed {
  display: inline-block;
  width: 30%;
  margin: 2px;
  padding-left: 5%;
}
.feed > img {
  width: 20vw;
  height: 20vw;
  object-fit: cover;
}
</style>