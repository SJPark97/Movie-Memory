<template>
  <div>
    <MovieCard/>
    <ReviewList/>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import ReviewList from '@/components/ReviewList'

export default {
  name: 'DetailView',
  components: {
    MovieCard,
    ReviewList,
  }
}
</script>

<style>

</style>