<template>
  <div>
    <section class="profile-info">
      <div class="profile-img">
        <img :src="`http://127.0.0.1:8000${user.img}`" alt="#">
      </div>
      <div class="profile-text">
        <h1>{{ user.username }}</h1>
        <h3>{{ user.nick_name }}</h3>
        <p> {{ user.self_introduction }}</p>
        <button v-show="this.$store.state.userId === user.id" @click="updateInfo">회원 정보 수정</button>
        <UpdateUserInfo v-show="updataAva"/>
      </div>
      <div class="follow">
        <h3>팔로우</h3>
        <h3>팔로잉</h3>
      </div>
    </section>
    <!-- https://bootstrap-vue.org/docs/components/tabs -->
    <b-card no-body class="storage">
      <b-tabs 
        card 
        content-class="mt-3 bg-transparent" 
        align="center"
        active-nav-item-class="bg-transparent border-bottom-0"
        active-tab-class="font-weight-bold success"
      >
        <b-tab avtive>
          <template v-slot:title>
            <span>
            <font-awesome-icon icon="fa-solid fa-pen"/>
            </span>
          </template>
          <b-card-text>
            <MyReview/>
          </b-card-text>
        </b-tab>
        <b-tab >
          <template v-slot:title>
            <span>
            <font-awesome-icon icon="fa-solid fa-clapperboard" />
            </span>
          </template>
          <b-card-text>
            <MyMovie/>
          </b-card-text>
        </b-tab>
        <b-tab >
          <template v-slot:title>
            <span>
            <font-awesome-icon icon="fa-solid fa-heart" />
            </span>
          </template>
          <b-card-text>
            <LikedReview/>
          </b-card-text>
        </b-tab>
      </b-tabs>
    </b-card>
  </div>
</template>



<script>
import MyReview from '@/components/MyReview'
import MyMovie from '@/components/MyMovie'
import LikedReview from '@/components/LikedReview'
import UpdateUserInfo from '@/components/UpdateUserInfo'

export default {
  name: 'ProfileView',
  components: {
    MyReview,
    MyMovie,
    LikedReview,
    UpdateUserInfo,
  },
  computed: {
    user(){
      return this.$store.state.user
    }
  },
  data() {
    return {
      updataAva: false,
    }
  },
  methods: {
    getUserReviews() {
      this.$store.dispatch('getUserReviews', this.$store.state.username)
    },
    updateInfo() {
      this.updataAva = true
    }
  },
  created() {
    this.$store.dispatch('getProfile', this.$route.params.userId)
    this.$store.dispatch('userLikedMovie', this.$route.params.userId)
    this.$store.dispatch('userLikedReview', this.$route.params.userId)
  },
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
  display: inline-block;
  width: 20vw;
}

.card-header-pills {
  background-color: rgb(221, 221, 221);
}

.storage {
  position: relative;
  bottom: 100px;
  display: flex;
  width: 70%;
  margin-top: 15%;
  margin-left: 15%;
  // margin-right: 15%;
  padding-bottom: 10vh;
  background-color: rgb(221, 221, 221);
  border: none;
  box-shadow: 1px 1px 1px 1px rgb(196, 196, 196);
  /* height: 80%; */
}

/* i태그 */
svg {
  text-decoration: none;
  color: black;
  text-shadow: 2px 2px gray;
}
svg:focus-within {
  color: red
}

span {
  font-size: 130%;
}

</style>