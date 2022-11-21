<template>
  <div class="update-div">
    <!-- <form @submit.prevent="setUserInfo">

      <p>선호하는 장르 선택</p>
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
    </form> -->
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdateUserInfo',
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  // data() {
  //   return {
  //     nickname: this.user.nick_name,
  //     image: this.user.img,
  //     age: this.user.age,
  //     gender: this.user.gender,
  //     genres: this.user.genres,
  //     intro: this.user.intro,
  //   }
  // },
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
        method: 'put',
        url: `${API_URL}/accounts/user/myprofile/`,
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization' : `Token ${this.$store.state.token}`
        },
        data: formData,
      })
        .then((response) => {
          console.log(response)
          this.$router.push({name: 'profile', params: {userId: this.$store.state.userId}})
        })
        .catch((error) => {
          console.log(error)
        })
    },
  }
}
</script>


<style>
.update-div {
  display: inline-block;
  width: 550px;
  height: 500px;
  position: absolute;
  /* object-fit: contain; */
  top: -10px;
  left: -20px;
  padding-top: 40px;
  padding-left: 60px;
  padding-right: 60px;
  border: 1px solid gray;
  box-shadow: 5px 5px 10px 3px rgb(136, 136, 136);
  z-index: 999;
  background-color: rgb(218, 210, 210);
}
.update-div > h2 {
  margin-bottom: 20px;
}

.signup-input { 
  display: inline-block;
  position: relative;
  width: 430px;
  display: flex;
  justify-content: space-between;
  margin-top: 5px;
}


.signup-input > input {
  width: 300px;
  height: 33px;
  border: 1px solid gray;
  border-radius: 8px;
}

.input-btn {
  margin-top: 20px;
  margin-bottom: 20px;
}


.x-mark {
  position: absolute;
  top: 15px;
  left: 510px;
  color: white;
  font-size: 25px;
  cursor: pointer;
}
</style>