<template>
  <div class="update-div">
    <form @submit.prevent="setUserInfo">
      <h2>회원 정보 수정</h2>
      <font-awesome-icon 
        icon="fa-solid fa-xmark" 
        class="x-mark" 
        @click="popExit"
      />
      <div class="form-in">
        <label for="nickname">닉네임</label>
        <input type="text" id="nickname" v-model="nickname" maxlength="10">
      </div>
      
      <div class="form-in">
        <label for="intro">자기소개</label>
        <textarea name="intro" id="intro" cols="30" rows="3" v-model="intro" maxlength="60"></textarea>
      </div>
      
      <div class="form-in input-file-button">
        <label for="img" v-if="this.user.img === image">프로필 사진 <font-awesome-icon icon="fa-solid fa-image" /></label>
        <label for="img" class="selected" v-else>사진 선택됨</label>
        <input @change="uploadImg" id="img" ref="image" type="file" accept="image/*">
      </div>
      <p>새로운 이미지를 등록하지 않으면 기존의 이미지가 저장됩니다.</p>

      <div class="form-btn">
        <input type="submit" class="input-btn">
      </div>

    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdateUserInfo',
  props: {
    user: Object,
  },
  data() {
    return {
      nickname: this.user.nick_name,
      image: this.user.img,
      intro: this.user.self_introduction,
    }
  },
  methods: {
    uploadImg() {
      this.image = this.$refs.image.files
    },
    popExit() {
      this.$emit('pop-exit')
    },
    setUserInfo() {
      const formData = new FormData()
      formData.append('nick_name', this.nickname)
      formData.append('self_introduction', this.intro)
      if (this.$refs.image.files[0]) {
        formData.append('img', this.$refs.image.files[0])
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
          this.$store.dispatch('getProfile', this.$route.params.userId)
          this.popExit()
        })
    },
  }
}
</script>


<style>
.update-div {
  display: inline-block;
  width: 500px;
  height: 400px;
  position: absolute;
  top: -10px;
  left: 0px;
  padding-top: 20px;
  padding-left: 30px;
  padding-right: 30px;
  border: 1px solid gray;
  box-shadow: 5px 5px 10px 3px rgb(136, 136, 136);
  z-index: 999;
  background-color: rgb(218, 210, 210);
}

.update-div > form > h2 {
  font-size: 25px;
  margin-bottom: 15px;
}

.update-div > form > p {
  font-size: 10px;
  margin-bottom: 15px;
}

.form-in { 
  /* display: inline-block; */
  position: relative;
  width: 440px;
  display: flex;
  justify-content: space-between;

  /* inline-size: auto;
  writing-mode: horizontal-tb; */

  margin-top: 10px;
  /* vertical-align: middle; */
  font-size: 15px;

}


.form-in > label {
  padding-top: 5px;
  vertical-align: baseline;
}

.form-in > input[type="text"] {
  padding-left: 10px;
  width: 360px;
  height: 40px;
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 10px;
}

.form-in > textarea {
  padding-left: 10px;
  padding-top: 5px;
  width: 360px;
  height: 100px;
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 10px;
}

.form-in > input[type="file"] {
  display: none;
}

.input-file-button{
  width: 100%;
  text-align: center;
  margin-top: 20px;
  text-align: center;
  padding: 5px 170px;
  color: black;
  background-color: rgb(240, 226, 215, 0.7);
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 30px;
}


.form-btn {
  display: inline-block;
  position: relative;
  width: 100%;
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

.selected {
  font-weight: bold;
  background-color: rgb(240, 226, 215, 0.8);
}

.x-mark {
  position: absolute;
  top: 15px;
  left: 460px;
  color: white;
  font-size: 25px;
}
</style>