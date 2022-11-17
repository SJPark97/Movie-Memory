<template>
  <div class="auth-div">
    <h2>로그인</h2>
    <form @submit.prevent="LogIn">
      <div class="login-input">
        <label for="username-login">아이디</label>
        <input type="text" id="username-login" v-model="username">
      </div>
      
      <div class="login-input">
        <label for="password-login">비밀번호</label>
        <input type="password" id="password-login" v-model="password">
      </div>
        
      <input type="submit" class="input-btn">
    </form>
  </div>
</template>


<script>

export default {
  name: 'LogIn',
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
  }
}
</script>

<style scoped>

h2 {
  margin-bottom: 20px;
}

.login-input { 
  display: inline-block;
  width: 370px;
  display: flex;
  justify-content: space-between;
  margin-top: 5px;
}

.login-input > input {
  width: 280px
}

.input-btn {
  margin-top: 20px;
}

</style>