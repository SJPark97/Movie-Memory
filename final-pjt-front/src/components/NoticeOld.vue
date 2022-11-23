<template>
  <div>
    <p @click="deleteCheckedNotices" class="delete-all-notices">삭제</p>
    <div class="inside">
      <p v-if="oldNotices == false" class="no-notice">새 알림이 없습니다</p>
      <div v-for="notice in oldNotices" :key="notice.id">
        <p class="button" @click="moveToReview(notice.review, notice.id)">{{ notice.content }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'NoticeNew',
  computed: {
    oldNotices() {
      return this.$store.state.oldNotices
    },
  },
  methods: {
    moveToReview(reviewId, noticeId) {
      this.$store.dispatch('visitNoti', noticeId)
      this.$store.dispatch('getNotice')
      this.$router.push({name: 'review_detail', params: {review_id: reviewId}})
      this.$emit('close-notice')
    },
    deleteCheckedNotices() {
      axios({
        method: 'delete',
        url: 'http://127.0.0.1:8000/accounts/user/delete_checked_notice/',
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        }
      })
        .then((response) => {
          this.$store.dispatch('getNotice')
        })
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

.delete-all-notices {
  position: absolute;
  z-index: 999!important;
  top: 27px;
  left: 230px;
  color: red;
  font-size: 15px;
}
.delete-all-notices:hover{
  cursor: pointer;
}
</style>