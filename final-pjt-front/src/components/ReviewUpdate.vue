<template>
  <div class="review-create">
    <font-awesome-icon 
    icon="fa-solid fa-xmark" 
    class="x-mark" 
    @click="popExit"
    />
    <h2>리뷰 수정</h2>
    <form @submit.prevent="updateReview">
      <div class="form-in">
        <label for="review-title">제목</label>
        <input type="text" id="review-title" v-model.trim="reviewTitle">
      </div>

      <div class="form-in">
        <label for="review-content">내용</label>
        <textarea name="review-content" id="review-content" cols="70" rows="10" v-model.trim="reviewContent"></textarea>
      </div>
      
      <div class="form-in">
        <label class="input-file-button" for="input-file">이미지 파일 업로드</label>
        <input @change="uploadImg" ref="reviewImg" type="file" accept="image/*" id="input-file">
      </div>
      
      <div class="form-btn">
        <input type="submit" value="수정">
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewUpdate',
  props: {
    review: Object,
  },
  computed: {
    token() {
      return this.$store.state.token
    },
  },
  data() {
    return {
      reviewTitle: this.review.title,
      reviewContent: this.review.content,
      reviewImg: this.review.img
    }
  },
  methods: {
    popExit() {
      this.$emit('pop-exit')
    },
    uploadImg() {
      this.reviewImg = this.$refs.reviewImg.files
    },
    updateReview() {
      const formData = new FormData()
      formData.append('title', this.reviewTitle)
      formData.append('content', this.reviewContent)
      if (this.$refs.reviewImg.files[0]) {
        formData.append('img', this.$refs.reviewImg.files[0])
      }
      const reviewId = this.$route.params.review_id

      axios({
        method: 'put',
        url: `${API_URL}/api/v1/reviews/${reviewId}/`,
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `Token ${this.$store.state.token}`
        },
        data: formData,
      })
        .then((response) => {
          this.$store.dispatch("getOneReview", reviewId)
          this.popExit()
        })
        .catch((error) => {
          console.log(error)
          alert('리뷰를 수정할 수 없습니다.')
        })
    },
  }
}
</script>

<style scoped>
div {
  position: relative;
}
.review-create {
  display: inline-block;
  width: 60vw;
  height: 600px;
  /* object-fit: contain; */
  position: absolute;
  top: 15vh;
  left: 20vw;
  padding-top: 40px;
  padding-left: 5vw;
  padding-right: 5vw;
  border: 1px solid gray;
  box-shadow: 5px 5px 10px 3px rgb(136, 136, 136);
  z-index: 999;
  background-color: rgb(218, 210, 210);
}


.form-in { 
  display: inline-block;
  position: relative;
  width: 50vw;
  display: flex;
  justify-content: space-between;
  margin-top: 2vh;
  /* vertical-align: middle; */
  font-size: 20px;
}

.form-in > input[type="text"] {
  width: 45vw;
  height: 40px;
    border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 10px;
}

.form-in > textarea {
  width: 45vw;
  height: 280px;
    border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 10px;
}

.form-in > input[type="file"] {
  display: none;
}

.input-file-button{
  width: 100%;
  text-align: center;
  padding: 6px 25px;
  background-color: rgb(240, 226, 215, 0.8);
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 30px;
  color: black;
  cursor: pointer;
}

.form-btn {
  display: inline-block;
  position: relative;
  width: 50vw;
  display: flex;
  justify-content: center;
  
  /* margin-top: 2vh; */
}

.form-btn > input[type="submit"] {
  width: 50px;
  height: 35px;
  font-size: 17px;
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 5px;
}

.x-mark {
  position: absolute;
  top: 1.5vh;
  left: 56vw;
  color: white;
  font-size: 25px;
  cursor: pointer;
}
</style>