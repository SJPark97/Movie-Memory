<template>
  <span>
    <div class="comment-list" v-for="comment in comments" :key="comment.id">
      <CommentCard :comment="comment" @change-comments="changeComments" @active="getOneComment()"/>
    </div>
  </span>
</template>

<script>
import CommentCard from '@/components/CommentCard'

export default {
  name: 'CommentList',
  components: {
    CommentCard,
  },
  computed: {
    comments() {
      return this.$store.state.reviewComments
    }
  },
  methods: {
    changeComments() {
      this.$store.dispatch('getReviewComment', this.$route.params.review_id)
    }
  }
}
</script>

<style scoped>


.comment-list {
  display: inline-block;
  width: 90%;
  text-align: left;
  margin-left: 30px;
  margin-right: 30px;
  /* background-image: url(); */
  /* border: 1px solid brown; */
  margin-bottom:3px;
  border-radius:  0 15px 15px 0  ;
  background:#27100d3e;
  padding-left: 10px;
  padding-bottom: 10px;
}
</style>