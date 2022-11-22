<template>
  <div class="signup-div">
    <form @submit.prevent="setUserInfo">

      <div>
        <input type="checkbox" v-model="genres" value="action">액션
        <input type="checkbox" v-model="genres" value="adventure">모험
        <input type="checkbox" v-model="genres" value="animation">애니메이션
        <input type="checkbox" v-model="genres" value="comedy">코미디
        <input type="checkbox" v-model="genres" value="crime">범죄
        <input type="checkbox" v-model="genres" value="documentary">다큐멘터리
        <input type="checkbox" v-model="genres" value="drama">드라마
        <input type="checkbox" v-model="genres" value="family">가족
        <input type="checkbox" v-model="genres" value="fantasy">판타지
        <input type="checkbox" v-model="genres" value="history">역사
        <input type="checkbox" v-model="genres" value="horror">공포
        <input type="checkbox" v-model="genres" value="music">음악
        <input type="checkbox" v-model="genres" value="mystery">미스터리
        <input type="checkbox" v-model="genres" value="romance">로맨스
        <input type="checkbox" v-model="genres" value="science">공상과학
        <input type="checkbox" v-model="genres" value="tv">TV영화
        <input type="checkbox" v-model="genres" value="thriller">스릴러
        <input type="checkbox" v-model="genres" value="war">전쟁
        <input type="checkbox" v-model="genres" value="western">서부
      </div>
      
      <div>
        <label for="nickname">닉네임</label>
        <input type="text" id="nickname" v-model="nickname">
      </div>

      <div>
        <label for="age">나이</label>
        <input type="number" id="age" v-model="age" min="0" max="100">
      </div>

      <div>
        <label for="gender">성별</label>
        <select name="gender" id="gender" v-model="gender">
          <option value="" selected="selected">선택안함</option>
          <option value="male">남성</option>
          <option value="female">여성</option>
        </select>
      </div>

      <div>
        <label for="img">프로필 사진</label>
        <input id="img" ref="image" type="file" accept="image/*">
      </div>
      
      <div>
        <label for="intro">자기소개</label>
        <textarea name="intro" id="intro" cols="30" rows="3" v-model="intro"></textarea>
      </div>
      <input type="submit" class="input-btn">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SetProfile',
  data() {
    return {
      nickname: null,
      image: null,
      age: null,
      gender: null,
      genres: [],
      intro: null,
    }
  },
  methods: {
    setUserInfo() {
      const formData = new FormData()
      formData.append('age', this.age)
      formData.append('gender', this.gender)
      formData.append('nick_name', this.nickname)
      formData.append('img', this.$refs.image.files[0])
      formData.append('self_introduction', this.intro)

      for(const genre of this.genres) {
        formData.append(`${genre}`, 1)
      }

      axios({
        method: 'post',
        url: `${API_URL}/accounts/user/myprofile/`,
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization' : `Token ${this.$store.state.token}`
        },
        data: formData,
      })
        .then((response) => {
          console.log(response)
          this.$router.push({name: 'main'})
        })
        .catch((error) => {
          console.log(error)
          alert('다른 이미지를 선택해주세요.')
        })
    },
  }
}
</script>

<style>

</style>