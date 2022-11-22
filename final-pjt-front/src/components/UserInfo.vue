<template>
  <div class="profile-info">
      <div class="profile-img">
        <img :src="`http://127.0.0.1:8000${user.img}`" alt="#">
        <button @click="follow" class="follow" v-show="!is_followed">팔로우</button>
        <button @click="follow" class="following" v-show="is_followed">팔로잉</button>
      </div>
      <div class="profile-text">
        <h1>{{ user.username }}</h1>
        <h3>{{ user.nick_name }}</h3>
        <p> {{ user.self_introduction }}</p>
        <button v-show="this.$store.state.userId === user.id" @click="updateInfo">회원 정보 수정</button>
        <UpdateUserInfo v-show="updataAva"/>
      </div>

      <div class="follow-count">
        <div>
          <h3>팔로우</h3>
          <h3>{{ followers }}</h3>
        </div>
        <div>
          <h3>팔로잉</h3>
          <h3>{{ followings }}</h3>
        </div>
      </div>

    </div>
</template>

<script>
import UpdateUserInfo from '@/components/UpdateUserInfo'

export default {
  name: 'UserInfo',
  components: {
    UpdateUserInfo,
  },
  computed: {
    user(){
      return this.$store.state.user
    },
    is_followed() {
      return this.$store.state.is_followed
    },
    followers() {
      return this.$store.state.followers
    },
    followings() {
      return this.$store.state.followings
    }
  },
  methods: {
    follow() {
      this.$store.dispatch('follow', this.$route.params.userId)
    }
  }
}
</script>

<style lang="scss" scoped>

.profile-info {
  display: flex;
  justify-content: space-between;
  width: 70vw;
  margin-top: 5%;
  margin-left: 15%;
  margin-right: 15%
}

.profile-info > p {
  font-size: 2vw;
}
.profile-img {
  display: inline-block;
  height: 15vw;
  width: 15vw;
  margin-left: 10%;
  // padding: 1px;
  // border: 1px solid gray;
  // position: relative;
  border-radius: 100%;
}

.profile-img > img {
  height: 15vw;
  width: 15vw;
  padding: 0.5vw;
  object-fit: cover;
  border: 2px solid #E6E6E6;
  // box-shadow: 1px 1px gray;
  border-radius: 100%;
}

.profile-text {
  display: inline-block;
  text-align: left;
  width: 25vw;
  margin-right: 10%;
}

.profile-text > h1 {
  font-size: 4vw;
  margin-bottom: 1vw;
}

.profile-text > h3 {
  font-size: 3vw;
  margin-bottom: 1vw;
  // font-weight: bold;
}

.profile-text > p {
  font-size: 1.5vw;
}

button {
  background-color: #E6E6E6;
  border: 1px solid #908581;
  border-radius: 10px;
  padding-left: 4vw;
  padding-right: 4vw;
  padding-top: 0.5vw;
  padding-bottom: 0.5vw;
}

// @media (max-width: 800px) {
//   .profile-text {
//     width: 50vw;
//   }
//   .follow  {
//     width: 50vw;
//   }
// }

.follow {
  background-color: skyblue;
  font-weight: bold;
}

.following {
  color: green;
  font-weight: bold;
}

.follow-count {
  display: inline-block;
  width: 20vw;
}

.follow-count > div {
  display: inline-block;
  width: 9vw;
}
</style>