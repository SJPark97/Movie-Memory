<template>
  <div class="review-create">
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
  // props: {
  //   moviePk: Number,
  // },
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
    uploadImg() {
      this.reviewImg = this.$refs.reviewImg.files
      console.log(this.reviewImg)
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
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
    } 
  }
}
</script>

<style>

</style>