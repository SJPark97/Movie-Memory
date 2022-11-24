<template>
  <div class="auth-div">
    <h2>로그인</h2>
    <form @submit.prevent="LogIn">
      <div class="login-input">
        <label for="username-login">아이디</label>
        <input type="text" id="username-login" v-model="username" placeholder="ID">
      </div>
      
      <div class="login-input">
        <label for="password-login">비밀번호</label>
        <input type="password" id="password-login" v-model="password" placeholder="Password">
      </div>
        
      <input type="submit" class="input-btn">
      <p @click="popSignup">SIGNUP</p>
      <SignUp v-show="signUpAva" @pop-exit="popExit"/>
    </form>
  </div>
</template>


<script>
import SignUp from "@/components/SignUp";

export default {
  name: 'LogIn',
  components: {
    SignUp,
  },
  data() {
    return {
      username: null,
      password: null,
      signUpAva: false,
    }
  },
  computed: {
    token() {
      return this.$store.state.token
    }
  },
  methods: {
    LogIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      this.$store.dispatch('logIn', payload)
      this.username = null
      this.password = null
    },
    popSignup() {
      this.signUpAva = true
    },
    popExit() {
      this.signUpAva = false
    }
  }
}
</script>

<style scoped>

h2 {
  margin-bottom: 20px;
}


.auth-div {
  display: inline-block;
  width: 500px;
  height: 300px;
  position: absolute;
  /* object-fit: contain; */
  top: 70px;
  left: 200px;
  padding-top: 40px;
  padding-left: 60px;
  padding-right: 60px;
  border: 1px solid gray;
  box-shadow: 5px 5px 10px 3px rgb(136, 136, 136);
  z-index: 999;
  background-color: rgb(218, 210, 210);
}

.login-input { 
  display: inline-block;
  width: 370px;
  display: flex;
  justify-content: space-between;
  margin-top: 5px;
}

.login-input > label { 
  display: inline-block;
  width: 100px;
  text-align: center;
}

.login-input > input {
  width: 280px;
  height: 33px;
  border: 1px solid gray;
  border-radius: 8px;
  padding-left: 10px;
}

.input-btn {
  margin-top: 20px;
  margin-bottom: 20px;
}

</style>