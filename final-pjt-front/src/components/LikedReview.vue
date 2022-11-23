<template>
  <div>
    <p v-show="reviews == false">좋아하는 리뷰를 저장해보세요</p>
    <div 
      class="feed"
      v-for="review in reviews.slice().reverse()" 
      :key="review.id"
      @click="moveToReview(review.id)"
    >
      <img :src="`http://127.0.0.1:8000${review?.img}`" alt="">
    </div>
  </div>
</template>

<script>
export default {
  name: 'LikedReview',
  computed: {
    reviews() {
      return this.$store.state.likedReviews
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
  margin-left: 4%;
}


p {
  display: inline-block;
  text-align: center;
  width: 100%;
}

.feed {
  display: inline-block;
  width: 30%;
  margin: 2px;
  margin: 5px;
}

.feed:after {
  content: "";
  display: block;
  padding-bottom: 100%;
}


.feed > img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>