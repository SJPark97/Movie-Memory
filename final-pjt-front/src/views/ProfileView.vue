<template>
  <div>
    <div class="profile-img">이미지</div>
    <section>
      아이디 [프로필 편집 버튼] / 닉네임 / 자기소개
      <UpdateUserInfo/>
    </section>
    <!-- https://bootstrap-vue.org/docs/components/tabs -->
    <b-card no-body class="storage">
      <b-tabs pills card content-class="mt-3" align="center">
        <b-tab avtive>
          <template v-slot:title>
            <span>
            <font-awesome-icon icon="fa-solid fa-pen" />
            </span>
          </template>
          <b-card-text>
            <MyStorage/>
          </b-card-text>
        </b-tab>
        <b-tab active>
          <template v-slot:title>
            <span>
            <font-awesome-icon icon="fa-solid fa-clapperboard" />
            </span>
          </template>
          <b-card-text>
            <MyStorage/>
          </b-card-text>
        </b-tab>
        <b-tab active>
          <template v-slot:title>
            <span>
            <font-awesome-icon icon="fa-solid fa-heart" />
            </span>
          </template>
          <b-card-text>
            <MyStorage/>
          </b-card-text>
        </b-tab>
      </b-tabs>
    </b-card>
  </div>
</template>



<script>
import MyStorage from '@/components/MyStorage'
import UpdateUserInfo from '@/components/UpdateUserInfo'

export default {
  name: 'ProfileView',
  components: {
    MyStorage,
    UpdateUserInfo,
  },
  methods: {
    getUserInfo() {
      this.$store.dispatch('getUserInfo')
    },
    getUserReviews() {
      this.$store.dispatch('getUserReviews', this.$store.state.username)
    }
  },
  // created() {
  //   this.getUserInfo()
  // }
}
</script>

<style scoped lang="scss">
// @import "../../global.scss"

.profile-img {
  display: inline-block;
  width: 20%;
  position: relative;
}

.card-header-pills {
  background-color: rgb(221, 221, 221);
}
.storage {
  display: inline-block;
  width: 80%;
  background-color: rgb(221, 221, 221);
  border: none;
  box-shadow: 1px 1px 1px 1px rgb(196, 196, 196);
  /* height: 80%; */
}

/* i태그 */
svg {
  text-decoration: none;
  color: white;
  text-shadow: 2px 2px gray;
}


span {
  font-size: 130%;
}

</style>