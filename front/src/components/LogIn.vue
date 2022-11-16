<template>
  <div>
    <form @submit.prevent="LogIn">

      <label for="username-login">아이디</label>
      <input type="text" id="username-login" v-model="username">

      <label for="password-login">비밀번호</label>
      <input type="password" id="password-login" v-model="password">
      
      <input type="submit">
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
    }
  }
}
</script>

<style>

</style>