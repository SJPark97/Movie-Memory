<template>
  <div>
    <UserInfo/>
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
            <span>영화
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
import UserInfo from '@/components/UserInfo'
import MyReview from '@/components/MyReview'
import MyMovie from '@/components/MyMovie'
import LikedReview from '@/components/LikedReview'

export default {
  name: 'ProfileView',
  components: {
    UserInfo,
    MyReview,
    MyMovie,
    LikedReview,
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
    this.$store.dispatch('MyReviews', this.$route.params.userId)
    this.$store.dispatch('userLikedMovie', this.$route.params.userId)
    this.$store.dispatch('userLikedReview', this.$route.params.userId)
  },
}
</script>

<style lang="scss" scoped>


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