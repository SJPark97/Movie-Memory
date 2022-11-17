<template>
  <div class="review-list">
    <h1>리뷰 리스트😋</h1>
    <div v-for="review in thisMovieReview" :key="review.id">
      <img :src="`http://127.0.0.1:8000${review?.img}`" alt="">
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
  props: {
    reviews: Array,
  },
}
</script>

<style>

</style>