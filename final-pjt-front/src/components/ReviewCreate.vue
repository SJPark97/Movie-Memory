<template>
  <div class="review-create">
    <font-awesome-icon 
    icon="fa-solid fa-xmark" 
    class="x-mark" 
    @click="popExit"
    />
    <h2>리뷰 작성</h2>
    <form @submit.prevent="createReview">
      <label for="review-title">제목</label>
      <input type="text" id="review-title" v-model.trim="reviewTitle">
      <br>
      <label for="review-content">내용</label>
      <textarea name="review-content" id="review-content" cols="70" rows="10" v-model.trim="reviewContent"></textarea>
      <br>
      <input @change="uploadImg" ref="reviewImg" type="file" accept="image/*">
      <br>
      <input type="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewCreate',
  data() {
    return {
      reviewTitle: null,
      reviewContent: null,
      reviewImg: null,
    }
  },
  computed: {
    token() {
      return this.$store.state.token
    }
  },
  methods: {
    popExit() {
      this.$emit('pop-exit')
    },
    uploadImg() {
      this.reviewImg = this.$refs.reviewImg.files
    },
    createReview() {
      const formData = new FormData()
      formData.append('title', this.reviewTitle)
      formData.append('content', this.reviewContent)
      formData.append('img', this.$refs.reviewImg.files[0])
      const moviePk = this.$route.params.movie_id

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${moviePk}/reviews/`,
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization' : `Token ${this.token}`
        },
        data: formData,
      })
        .then((response) => {
          this.$router.push({name: 'review_detail', params: {review_id: response.data.id}})
        })
        .catch((error) => {
          console.log(error)
          alert('리뷰를 작성할 수 없습니다')
        })
    } 
  }
}
</script>

<style scoped>
div {
  position: relative;
}
.review-create {
  display: inline-block;
  width: 800px;
  height: 500px;
  position: absolute;
  /* object-fit: contain; */
  top: 100px;
  left: 180px;
  padding-top: 40px;
  padding-left: 60px;
  padding-right: 60px;
  border: 1px solid gray;
  box-shadow: 5px 5px 10px 3px rgb(136, 136, 136);
  z-index: 999;
  background-color: rgb(218, 210, 210);
}

.x-mark {
  position: absolute;
  top: 20px;
  left: 750px;
  color: white;
  font-size: 25px;
  cursor: pointer;
}
</style>