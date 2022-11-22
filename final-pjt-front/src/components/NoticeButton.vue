<template>
  <a class="button" @click="moveToReview">{{ notice.content }}</a>
</template>

<script>
export default {
  name: 'NoticeButton',
  method: {
    moveToReview() {
      this.$router.push({name: 'review_detail', params: {review_id: notice.review_id}})
    }
  }
}
</script>

<style>
.button {
  background-color: #1d303313;
  color: rgb(26, 22, 22);
  padding: 15px 32px;
  margin: 3px;
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
</style>