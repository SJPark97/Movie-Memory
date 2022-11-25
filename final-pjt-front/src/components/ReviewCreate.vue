<template>
  <div class="review-create">
    <font-awesome-icon 
    icon="fa-solid fa-xmark" 
    class="x-mark" 
    @click="popExit"
    />
    <h2>리뷰 작성</h2>
    <form @submit.prevent="createReview">
      <div class="form-in">
        <label for="review-title">제목</label>
        <input type="text" id="review-title" v-model.trim="reviewTitle" maxlength="50">
      </div>

      <div class="form-in">
        <label for="review-content">내용</label>
        <textarea name="review-content" id="review-content" cols="70" rows="10" v-model.trim="reviewContent" maxlength="500"></textarea>
      </div>
      
      <div class="form-in">
        <label class="input-file-button" for="input-file" v-if="!reviewImg">이미지 파일 업로드</label>
        <label class="input-file-button selected" for="input-file" v-else>이미지 파일 선택됨</label>
        <input @change="uploadImg" ref="reviewImg" type="file" accept="image/*" id="input-file">
      </div>
      
      <div class="form-btn">
        <input type="submit" class="input-btn" value="작성">
      </div>
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
      if (!this.$refs.reviewImg.files[0]) {
        alert('이미지를 선택하세요')
        return
      }
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
  text-align: center;
  padding: 6px 25px;
  background-color: rgb(240, 226, 215, 0.7);
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 30px;
  color: black;
}

.selected {
  font-weight: bold;
  background-color: rgb(240, 226, 215, 0.8);
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

/* form > input[type="text"] {
  width: 40vw;
  height: 3vh;
} */
.x-mark {
  position: absolute;
  top: 1.5vh;
  left: 56vw;
  color: white;
  font-size: 25px;
}

</style>