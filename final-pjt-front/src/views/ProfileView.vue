<template>
  <div>
    <section class="profile-info">
      <div class="profile-img">
        <img :src="`http://127.0.0.1:8000${user.img}`" alt="#">
      </div>
      <p>아이디 : {{ user.username }}</p>
      <p>닉네임 : {{ user.nick_name }}</p>
      <p>자기소개 : </p>
      팔로우
      <UpdateUserInfo/>
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
  methods: {
    // getUserInfo() {
    //   this.$store.dispatch('getUserInfo')
    // },
    getUserReviews() {
      this.$store.dispatch('getUserReviews', this.$store.state.username)
    },
  },
  created() {
    this.$store.dispatch('getProfile', this.$route.params.userId)
  }
}
</script>

<style scoped lang="scss">

.profile-info {
  display: flex;
  justify-content:space-between;
  width: 70%;
  margin-top: 5%;
  margin-left: 15%;
  margin-right: 15%
}

.profile-img {
  display: inline-block;
  width: 100px;
  height: 100px;
  // position: relative;
  border-radius: 100%;
}

.profile-img > img {
  height: 10rem;
  width: 10rem;
  object-fit: cover;
  border: 1px solid rgb(255, 248, 248);
  box-shadow: 1px 1px gray;
  border-radius: 100%;
}

.card-header-pills {
  background-color: rgb(221, 221, 221);
}

.storage {
  display: flex;
  width: 70%;
  margin-top: 15%;
  margin-left: 15%;
  margin-right: 15%;
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