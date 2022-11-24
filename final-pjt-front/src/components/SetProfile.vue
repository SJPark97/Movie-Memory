<template>
  <div class="profile-div">
    <form @submit.prevent="setUserInfo">
      <h2>프로필 작성</h2>
      <div class="form-in">
        <div>
          <label for="age">나이</label>
          <input type="number" id="age" v-model="age" min="10" max="100" class="age-input"/>
        </div>

        <div>
          <label for="gender">성별</label>
          <select name="gender" id="gender" v-model="gender">
            <option value="" selected="selected">선택안함</option>
            <option value="male">남성</option>
            <option value="female">여성</option>
          </select>
        </div>
      </div>

      <div class="form-in">
        <label for="nickname">닉네임</label>
        <input type="text" id="nickname" v-model="nickname" maxlength="10"/>
      </div>

      <div class="form-in">
        <label for="intro">자기소개</label>
        <textarea
          name="intro"
          id="intro"
          cols="30"
          rows="3"
          v-model="intro"
          maxlength="60"
        ></textarea>
      </div>

      <div class="img-btn">
        <label class="input-file-button" for="img" v-if="!image">프로필 사진 <font-awesome-icon icon="fa-solid fa-image" /></label>
        <label class="input-file-button selected" for="img" v-else>프로필 사진 선택됨</label>
        <input @change="uploadImg" id="img" ref="image" type="file" accept="image/*"/>
      </div>

      <div class="genre-select">
        <p>영화 추천을 위한 장르를 선택해주세요</p>
        <input type="checkbox" v-model="genres" value="action" id="action"/>
        <label for="action" class="check-label">액션</label>

        <input type="checkbox" v-model="genres" value="adventure" id="adventure"/>
        <label for="adventure" class="check-label">모험</label>

        <input type="checkbox" v-model="genres" value="animation" id="animation"/>
        <label for="animation" class="check-label">애니메이션</label>

        <input type="checkbox" v-model="genres" value="comedy" id="comedy"/>
        <label for="comedy" class="check-label">코미디</label>

        <input type="checkbox" v-model="genres" value="crime" id="crime"/>
        <label for="crime" class="check-label">범죄</label>

        <input type="checkbox" v-model="genres" value="documentary" id="documentary"/>
        <label for="documentary" class="check-label">다큐멘터리</label>

        <input type="checkbox" v-model="genres" value="drama" id="drama"/>
        <label for="drama" class="check-label">드라마</label>

        <input type="checkbox" v-model="genres" value="family" id="family"/>
        <label for="family" class="check-label">가족</label>

        <input type="checkbox" v-model="genres" value="fantasy" id="fantasy"/>
        <label for="fantasy" class="check-label">판타지</label>

        <input type="checkbox" v-model="genres" value="history" id="history"/>
        <label for="history" class="check-label">역사</label>

        <input type="checkbox" v-model="genres" value="horror" id="horror"/>
        <label for="horror" class="check-label">공포</label>

        <input type="checkbox" v-model="genres" value="music" id="music"/>
        <label for="music" class="check-label">음악</label>

        <input type="checkbox" v-model="genres" value="mystery" id="mystery"/>
        <label for="mystery" class="check-label">미스터리</label>

        <input type="checkbox" v-model="genres" value="romance" id="romance"/>
        <label for="romance" class="check-label">로맨스</label>

        <input type="checkbox" v-model="genres" value="science" id="science"/>
        <label for="science" class="check-label">공상과학</label>

        <input type="checkbox" v-model="genres" value="tv" id="tv"/>
        <label for="tv" class="check-label">TV영화</label>

        <input type="checkbox" v-model="genres" value="thriller" id="thriller"/>
        <label for="thriller" class="check-label">스릴러</label>

        
        <input type="checkbox" v-model="genres" value="war" id="war"/>
        <label for="war" class="check-label">전쟁</label>

        <input type="checkbox" v-model="genres" value="western" id="western"/>
        <label for="western" class="check-label">서부</label>
      </div>


      <div class="form-btn">
        <input type="submit" class="input-btn" value="완료" />
      </div>

    </form>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "SetProfile",
  data() {
    return {
      nickname: null,
      image: null,
      age: null,
      gender: null,
      genres: [],
      intro: null,
    };
  },
  methods: {
    uploadImg() {
      this.image = this.$refs.image.files
    },
    setUserInfo() {
      const formData = new FormData();
      formData.append("age", this.age);
      formData.append("gender", this.gender);
      formData.append("nick_name", this.nickname);
      if (this.$refs.image.files[0] != undefined) {
        formData.append("img", this.$refs.image.files[0]);
      }
      formData.append("self_introduction", this.intro);

      for (const genre of this.genres) {
        formData.append(`${genre}`, 1);
      }

      axios({
        method: "post",
        url: `${API_URL}/accounts/user/myprofile/`,
        headers: {
          "Content-Type": "multipart/form-data",
          "Authorization": `Token ${this.$store.state.token}`,
        },
        data: formData,
      })
        .then((response) => {
          this.$router.push({ name: "main" });
        })
        .catch((error) => {
          console.log(error);
          alert("모든 항목을 입력해주세요");
        });
    },
  },
};
</script>

<style scoped>

.genre-select {
  /* width: 500px; */
  background-color: #f7f4ef5b;
  border-radius: 15px;
  padding: 10px 0px 10px 0px;
  margin-top: 25px;
}

.genre-select > p {
  text-decoration-line: underline;
}



.profile-div {
  display: inline-block;
  width: 550px;
  height: 730px;
  position: absolute;
  top: 70px;
  left: 200px;
  padding-top: 20px;
  padding-left: 30px;
  padding-right: 30px;
  border: 1px solid gray;
  box-shadow: 5px 5px 10px 3px rgb(136, 136, 136);
  z-index: 999;
  background-color: rgb(218, 210, 210);
}


.profile-div > form > h2 {
  margin-bottom: 20px;
}
.profile-div > div > p {
  margin: 0;
}

.check-label {
  display: inline-block;
  width: 80px;
  height: 25px;
  /* box-shadow: 1px 1px gray; */
  background-color:  #F7F4EF;
  border-radius: 10px;
  margin: 5px;
  font-size: 15px;
}

.check-label:hover {
  transform: scale(1.1);
}

input[type="checkbox"]:checked + .check-label {
  background-color: #b94a1760;
}

input[type="checkbox"] {
  display: none;
}


.form-in { 
  display: inline-block;
  position: relative;
  width: 450px;
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
  /* vertical-align: middle; */
  font-size: 20px;
}

.form-in > label {
  display: inline-block;
  width: 100px;
}

.form-in > input[type="text"] {
  padding-left: 15px;
  width: 320px;
  height: 40px;
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 10px;
}

.form-in > textarea {
  padding-left: 15px;
  width: 320px;
  height: 150px;
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 10px;
}
.form-in > div > label {
  margin-left: 30px;
  margin-right: 20px;

}
.form-in > div > input[type="number"] {
  width: 110px;
  height: 40px;
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 10px;
  padding-left: 15px;
  margin-left: 43px;
}

.form-in > div > select {
  width: 110px;
  height: 40px;
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 10px;
  padding-left: 15px;
}

div > input[type="file"] {
  display: none;
}


.input-file-button{
  width: 80%;
  padding: 0;
  padding-top: 5px;
  padding-bottom: 5px;
  background-color: rgb(240, 226, 215, 0.7);
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 30px;
  color: black;
  font-size: 20px;
}

.selected {
  font-weight: bold;
  background-color: rgb(240, 226, 215, 0.8);
}

.form-btn {
  display: inline-block;
  position: relative;
  /* width: 50vw; */
  display: flex;
  justify-content: center;
  
  margin-top: 10px;
}

.form-btn > input[type="submit"] {
  margin-top: 10px;
  width: 50px;
  height: 35px;
  font-size: 17px;
  border: 0.5px solid rgb(128, 128, 128, 0.5);
  border-radius: 5px;
}


</style>