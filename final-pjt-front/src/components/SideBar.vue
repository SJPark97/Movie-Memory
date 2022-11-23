<template>
  <div class="container" :class="{'show': showSidebar}">
    <div class="control">
      <i class="fas fa-angle-double-right" @click="showNav"></i>
    </div>
    <div class="navigation-links">
      <!-- 유저 로그인 시 -->
      <transition-group name="fade" v-if="this.$store.state.username">
          <div @click="goToMy" v-show="showLink" key="1"><router-link :to="`/${userId}`"><img :src="`http://127.0.0.1:8000${this.$store.state.userImg}`" alt="#"></router-link></div>
          <div v-show="showLink" key="2"><h4>{{ this.$store.state.nickname }}</h4></div>
          <div v-show="showLink" key="3"><router-link to="/main">Home</router-link></div>
          <div v-show="showLink" key="4"><router-link to="/movies">Movies</router-link></div>
          <div @click="goToMy" v-show="showLink" key="5"><router-link :to="`/${userId}`">Profile</router-link></div>
        <div v-show="showLink" key="6">
          <p @click="popReview">
            <font-awesome-icon icon="fa-solid fa-bell" v-if="noti" class="bell"/>
            <font-awesome-icon icon="fa-regular fa-bell" v-else class="bell"/>
          </p>
          <Notice v-show="popAva" @pop-exit="popExit" @close-notice="closeNotice"/>
        </div>
        <div v-show="showLink && this.$store.state.token" key="7"><button @click="logOut" class="logout">LOGOUT</button></div>
      </transition-group>

      <!-- 로그인 안 했을 때 -->
      <transition-group v-else>
        <div v-show="showLink" key="1" class="alert-message"> 로그인이 필요한 서비스입니다. </div>
      </transition-group>
    </div>
    <!-- <i class="fas fa-music"></i> -->
  </div>
</template>

<script>
import Notice from '@/components/Notice'

  export default {
    name: 'SideBar',
    components: {
      Notice,
    },
    computed: {
      username() {
        return this.$store.state.username
      },
      userId() {
        return this.$store.state.userId
      },
      user() {
        return this.$store.state.user
      },
      noti() {
        return this.$store.state.noti
      },
    },
    data: () => {
      return {
        showSidebar: false,
        showLink: false,
        popAva: false,
      }
    },
    methods: {
      popReview() {
        this.popAva = true
        this.$store.dispatch('getNotice')
      },
      popExit() {
        this.popAva = false
        this.$store.dispatch('getNotice')
      },
      showNav() {
        if(this.showSidebar) {
          this.showLink = false;
          setTimeout(() => {
            this.showSidebar = false;
          }, 50);
          this.$emit('open-side-bar', this.showLink)
          this.popAva = false
        }
        else {
          this.showSidebar = true;
          setTimeout(() => {
            this.showLink = true;
          }, 500);
          this.$emit('open-side-bar', this.showSidebar)
          this.$store.dispatch('getNotice')
        }
      },
      logOut() {
        this.$store.commit('LOGOUT')
        window.localStorage.clear()
        this.$router.push({name: 'home'})
        
        this.showLink = false;
        setTimeout(() => {
          this.showSidebar = false;
        }, 50);
        this.$emit('open-side-bar', this.showLink)
        this.popAva = false
      },
      goToMy() {
        this.$store.dispatch('getProfile', this.userId)
      },
      closeNotice() {
        this.popAva = false
      }
    }
  }
</script>

<style lang="scss" scoped>
// router-link는 a태그로 인식됨
a {
  text-decoration: none;
  margin-left: 0;
}

button {
  border-radius: 5px;
}

img {
  height: 65px;
  width: 65px;
  object-fit: cover;
  border: 2px solid #E6E6E6;
  // box-shadow: 1px 1px gray;
  border-radius: 100%;
}

h4 {
  display: inline-block;
  margin-bottom: 30px;
  width: 160px;
  white-space: wrap;
  font-size: 120%;
}

.bell {
  margin-top: 15px;
  margin-bottom: 10px;
  color: rgb(254, 181, 68, 0.6);
  font-size: 40px;
  cursor: pointer;
}

.alert-message {
  font-size: 20px;
  margin-top: 50px;
}
.container {
  position: fixed;
  top: 0;
  left: 0;
  width: 0px;
  height: 100vh;
  padding: 0px;
  min-height: calc(100vh - 20px);
  background-color: rgba($color: #E6E6E6, $alpha: .8);
  // border: solid #fff;
  // border-width: 0 1px 0 0;
  box-shadow: 0 3px #908581;
  z-index: 999;
  transition: all .5s ease-in-out;
  .control {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50px;
    margin-bottom: 10px;
    i {
      color: beige;
      font-size: 2.5rem;
      margin-left: 10px;
      cursor: pointer;
      transition: all .5s ease-in-out;
    }
  }
  &.show {
    width: 180px;
    height: 100vh;
    padding: 10px;
    .control > i {
      color: #fff;
      transform: rotateZ(-180deg);
    }
    .navigation-icons {
      color: #fff;
    }
  }
  .navigation-links {
    padding-top: 14px;
    float: left;
    div a {
      color: black;
      font-size: 2rem;
      // padding-left: 10px;
      margin-bottom: 30px;
      cursor: pointer;
      &:hover {
        color: #fff;
      }
    }
  }
}
@mixin nav-childs($values...) {
  @each $var in $values {
    &:nth-child(#{$var}) {
      transition: transform linear calc(.05s * #{$var}), display .5s;
    }
  }
}
.fade-enter-active, .fade-leave-active {
  @include nav-childs(1,2,3,4,5,6,7);
}
.fade-enter, .fade-leave-to {
  transform: scale(0);
}


.logout {
  border: none;
  background-color: rgb(200, 195, 191);
}
</style>