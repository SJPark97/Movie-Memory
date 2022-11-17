<template>
  <div class="auth-div">
    <h2>회원가입</h2>
    <form @submit.prevent="SignUp">

      <label for="username">아이디</label>
      <input type="text" id="username" v-model="username">
      <br>
      <label for="password1">비밀번호</label>
      <input type="password" id="password1" v-model="password1">
      <br>
      <label for="password2">비밀번호 확인</label>
      <input type="password" id="password2" v-model="password2">
      <br>
      <input type="submit">
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
      this.username = null
      this.password1 = null
      this.password2 = null

      this.$router.push({name: 'main'})
    }
  }
}
</script>

<style>

</style>