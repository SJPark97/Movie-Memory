<template>
  <div>
    <!-- 최신 리뷰가 가장 위에 뜨도록 =>  .slice().reverse() -->
    <!--back에서 반대로 받아옴..-->
    <p v-if="reviews == false  && this.$route.params.userId == this.$store.state.userId">리뷰를 작성해보세요</p>
    <p v-else-if="reviews == false && this.$route.params.userId !== this.$store.state.userId">아직 작성한 리뷰가 없습니다.</p>
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