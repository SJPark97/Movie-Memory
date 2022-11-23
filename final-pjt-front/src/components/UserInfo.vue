<template>
  <div class="profile-info">
      <div class="profile-img">
        <img :src="`http://127.0.0.1:8000${user.img}`" alt="#">


      </div>
      <div class="profile-text">
        <h1>{{ user?.nick_name }}</h1>
        <h4>{{ user?.username }}</h4>
        <p v-if="user.self_introduction !== 'null'"> {{ user?.self_introduction }}</p>
      </div>

      <div class="follow-count">
        <div>
          <p>팔로우</p>
          <h5>{{ followers }}</h5>
        </div>
        <div>
          <p>팔로잉</p>
          <h5>{{ followings }}</h5>
        </div>

        
        <!-- 회원 정보 수정은 나만 가능 -->
        <span v-if="user.id === this.$store.state.userId">
          <button @click="updateInfo" class="update-info">회원 정보 수정</button>
          <UpdateUserInfo :user="user" v-show="updateAva" @pop-exit="popExit"/>
        </span>

        <!-- 내가 아닐 때만 팔로우/언팔로우 가능 -->
        <span v-else>
          <button @click="follow" class="follow" v-show="!is_followed">팔로우</button>
          <button @click="follow" class="following" v-show="is_followed">팔로잉</button>
        </span>

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
    },
  },
  data(){
    return {
      updateAva: false,
    }
  },
  methods: {
    follow() {
      this.$store.dispatch('follow', this.$route.params.userId)
    },
    updateInfo() {
      this.updateAva = !this.updateAva
    },
    popExit() {
      this.updateAva = false
    }
  },
  created() {
    this.$store.dispatch('FirstFollow', this.$route.params.userId)
  }
}
</script>

<style lang="scss" scoped>

.profile-info {
  position: relative;
  display: flex;
  justify-content: space-between;
  width: 70%;
  height: 30%;
  margin-top: 5%;
  margin-bottom: 5%;
  margin-left: 15%;
  margin-right: 15%
}

.profile-info > p {
  font-size: 2vw;
}
.profile-img {
  display: inline-block;
  height: 18vw;
  width: 15vw;
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
  width: 50%;
  margin-left: 5%;
}

.profile-text > h1 {
  font-size: 4vw;
  margin-bottom: 2vw;
}

.profile-text > h4 {
  font-size: 2.5vw;
  margin-bottom: 1vw;
  // font-weight: bold;
}

.profile-text > p {
  font-size: 1.5vw;
}

.profile-text > div > button {
  width: 25vw;
  margin: 0;
  font-size: 2vw;
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


.follow-count {
  display: inline-block;
  width: 30%;
}

.follow-count > div {
  display: inline-block;
  width: 40%;
  height: auto;
  text-align: center;
  vertical-align: middle;
  margin-top: 10px;
  // border: 1px solid gray;
  background-color: #E6E6E6;
  border-radius: 10px;
  margin-left: 5px;
  padding: 0px;
  box-shadow: 1px 1px gray;
}

.follow-count > div > p {
  margin-bottom: 0px;
  font-size: 1.5vw;
  margin-top: 1vw
}

.follow-count > div > h5 {
  margin-bottom: 1vw;
  font-size: 2vw;
}

.follow-count > span > button {
  width: 15vw;
  margin-top: 20px;
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 0px;
  padding-right: 0px;
  font-size: 1.2vw;
  font-weight: bold;
  border: 0.5px solid rgb(128, 128, 128, 0.5);
}

.update-info {
  background-color:  rgba(199, 199, 199, 0.795);
}
.follow {
  background-color: rgb(219, 227, 230);
}

.following {
  color: green;
  background-color: rgb(194, 219, 211);
}
</style>