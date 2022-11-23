<template>
  <div class="inside">
    <p v-if="newNotices.length === 0" class="no-notice">알림이 없습니다</p>
    <div v-for="notice in newNotices" :key="notice.id">
      <p class="button" @click="moveToReview(notice.review, notice.id)">{{ notice.content }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'NoticeNew',
  computed: {
    newNotices() {
      return this.$store.state.newNotices
    },
  },
  methods: {
    moveToReview(reviewId, noticeId) {
      this.$store.dispatch('visitNoti', noticeId)
      this.$store.dispatch('getNotice')
      this.$router.push({name: 'review_detail', params: {review_id: reviewId}})
      this.$emit('close-notice')
    }
  },
}
</script>

<style>
.button {
  background-color: #1d303313;
  color: rgb(26, 22, 22);
  padding: 15px 32px;
  border: none;
  border-radius: 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  padding-top: 5%;
  font-size: 16px;
  width: 90%;
  height: 50px;
  white-space: nowrap;
  text-overflow: ellipsis;
  padding-right: 10%;
  overflow: hidden;
}
.button:hover {
  cursor: pointer;
  transform: scale(1.03);
  color: rgb(184, 159, 159);
  font-weight: bold;
}

.inside {
  position: absolute;
  top: 70px;
  left: 0px;
  width: 280px;
  height: 355px;
  overflow: auto;
}

.inside::-webkit-scrollbar {
  display: none;
}

.no-notice{
  position: absolute;
  top: 50px;
  left: 80px;
}
</style>