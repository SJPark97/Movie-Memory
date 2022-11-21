<template>
  <div class="notice">
    <font-awesome-icon icon="fa-solid fa-xmark" class="x-mark" @click="popExit" />
    <h2>새 알림</h2>
    <h2>오래된 알림</h2>
  </div>
</template>

<script>
// import axios from 'axios'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Notice',
  data() {
    return {
      newNotice: null,
      oldNotice: null,
    }
  },
  computed: {
    notice() {
      const notices = this.$store.state.notices
      const newNotice = []
      const oldNotice = []
      for (const notice of notices) {
        if (notice.is_checked === False) {
          newNotice.push(notice)
        } else {
          oldNotice.push(notice)
        }
      }
    },
    token() {
      return this.$store.state.token
    }
  },
  methods: {
    popExit() {
      this.$emit('pop-exit')
    },
  }
}
</script>

<style scoped>
.notice {
  display: inline-block;
  width: 500px;
  height: 300px;
  position: absolute;
  /* object-fit: contain; */
  top: 100px;
  left: 180px;
  padding-top: 40px;
  padding-left: 60px;
  padding-right: 60px;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 1px rgb(136, 136, 136);
  z-index: 999;
  background-color: rgb(218, 210, 210);
}

.x-mark {
  position: absolute;
  top: 20px;
  left: 455px;
  color: white;
  font-size: 25px;
  cursor: pointer;
}
</style>