<template>
  <div class="auth-div">
    <h2>로그인</h2>
    <form @submit.prevent="LogIn">

      <label for="username-login">아이디</label>
      <input type="text" id="username-login" v-model="username">
      <br>
      <label for="password-login">비밀번호</label>
      <input type="password" id="password-login" v-model="password">
      <br>
      <input type="submit">
    </form>
    <p @click="signUp">회원가입</p>
    <SignUp v-if="signUpAva"/>
  </div>
</template>

<!-- 
  팝업으로 띄울까 고민 중
  https://lusaxweb.github.io/vuesax/components/popup.html#default -->

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

      this.$route.push({name: 'main'})
    },
    signUp() {
      this.signUpAva = true
    }
  }
}
</script>

<style>


</style>