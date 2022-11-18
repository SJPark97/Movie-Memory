<template>
  <div class="review-list">
    <hr>
    <h1>REVIEWS</h1>
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
img {
  object-fit: cover;
  width: 130px;
  height: 100px;
}

h1 {
  text-align: left;
  margin-top: 30px;
  margin-bottom: 30px;
}

.review-div {
  display: flex;
  justify-content: left;
  margin-bottom: 30px;
}

.review-img {
  display: inline-block;
  width: 130px;
  height: 100px;
  margin-right: 30px;
}
.review-overview {
  height: 100px;
  text-align: left;
  text-overflow: ellipsis;
  overflow: hidden;
}
.title {
  font-size: 18px;
  font-weight: bold;
}

.content {
  font-size: 15px;
}
</style>