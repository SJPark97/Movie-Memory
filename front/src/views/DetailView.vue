<template>
  <div>
    <MovieCard/>
    <ReviewCreate/>
    <ReviewList/>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import ReviewCreate from '@/components/ReviewCreate'
import ReviewList from '@/components/ReviewList'

export default {
  name: 'DetailView',
  components: {
    MovieCard,
    ReviewCreate,
    ReviewList,
  }
}
</script>

<style>
body {
  display: flex;
  justify-content: center;
}

.movie-card {
  display: inline-block;
  width: 80%;
}

.review-create {
  display: inline-block;
  width: 80%;
}

.review-list {
  display: inline-block;
  width: 80%;
}

</style>