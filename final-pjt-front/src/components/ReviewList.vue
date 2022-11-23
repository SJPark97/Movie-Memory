<template>
  <div>
    <hr>
    <h1>REVIEWS</h1>
    <p v-if="reviews">{{ reviews.length }}개의 리뷰가 있습니다. </p>
    <p v-else>리뷰가 아직 없습니다.</p>
    <div 
      v-for="review in reviews" 
      :key="review.id" 
      class="review-div"
      @click="ReviewDetail(review.id)"
    >
      <div class="review-img">
        <img :src="`http://127.0.0.1:8000${review?.img}`" alt="">
      </div>
      <div class="review-overview">
        <span class="title">{{ review?.title }}</span><br>
        <span class="content">{{ review?.content }}</span><br>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'ReviewList',
  computed: {
    reviews() {
      return this.$store.state.movieReviews
    }
  },
  methods: {
    ReviewDetail(id) {
      this.$router.push({name: 'review_detail', params: {review_id: id}})
    }
  }
}
</script>

<style scoped>


h1 {
  font-family: Harmond;
  color: black;
  text-shadow: 1px 1px #908581;
  font-size: 3vw;

  text-align: left;
  margin-top: 30px;
  margin-bottom: 30px;
}

p {
  font-size: 1.3vw;
}


.review-div {
  display: flex;
  justify-content: left;
  margin-bottom: 5px;
  height: 10vw;
}

.review-img {
  display: inline-block;
  width: 11vw;
  height: 8vw;
  margin-right: 30px;
}


img {
  object-fit: cover;
  width: 11vw;
  height: 8vw;
}

.review-overview {
  height: 8vw;
  text-align: left;
  white-space: nowrap;
  text-overflow: ellipsis;
  padding-right: 5%;
  overflow: hidden;
}
.title {
  padding-top: 0.5vh;
  display: inline-block;
  font-size: 1.7vw;
  font-weight: bold;
}

.content {
  font-size: 1.3vw;
}
</style>