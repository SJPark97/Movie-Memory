<template>
  <div class="signup-div">
    <font-awesome-icon 
      icon="fa-solid fa-xmark" 
      class="x-mark" 
      @click="popExit"
    />
    <h2>회원가입</h2>
    <form @submit.prevent="SignUp">
      <div class="signup-input">
        <label for="username">아이디</label>
        <input type="text" id="username" v-model="username">
      </div>

      <div class="signup-input">
        <label for="password1">비밀번호</label>
        <input type="password" id="password1" v-model="password1">
      </div>

      <div class="signup-input">
        <label for="password2">비밀번호 확인</label>
        <input type="password" id="password2" v-model="password2">
      </div>

      <input type="submit" class="input-btn" value="다음">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    SignUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('SignUp', payload)
    },
    popExit() {
      this.$emit('pop-exit')
    }
  }
}
</script>

<style scoped>
.signup-div {
  display: inline-block;
  width: 550px;
  height: 330px;
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

.signup-div > h2 {
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