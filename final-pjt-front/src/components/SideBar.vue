<template>
  <div class="container" :class="{'show': showSidebar}">
    <div class="control">
      <i class="fas fa-angle-double-right" @click="showNav"></i>
    </div>
    <div class="navigation-links">
      <transition-group name="fade">

        <div v-show="showLink" key="1"><h4>Hi,{{ username }}</h4></div>
        <div v-show="showLink" key="2"><input type="text" class="search">검색</div>
        <div v-show="showLink" key="3"><router-link to="/main">Home</router-link></div>
        <div v-show="showLink" key="4"><router-link to="/movies">Movies</router-link></div>
        <div v-show="showLink" key="5"><router-link :to="`/${username}`">Profile</router-link></div>
        <div v-show="showLink" key="6">알림</div>
        <div v-show="showLink && this.$store.state.token" key="7"><button @click="logOut" class="logout">LOGOUT</button></div>

      </transition-group>
    </div>
    <!-- <i class="fas fa-music"></i> -->
  </div>
</template>

<script>
  export default {
    name: 'SideBar',
    computed: {
      username() {
        return this.$store.state.username
      }
    },
    data: () => {
      return {
        showSidebar: false,
        showLink: false,
      }
    },
    methods: {
      showNav() {
        if(this.showSidebar) {
          this.showLink = false;
          setTimeout(() => {
            this.showSidebar = false;
          }, 50);
          this.$emit('open-side-bar', this.showLink)
        }
        else {
          this.showSidebar = true;
          setTimeout(() => {
            this.showLink = true;
          }, 500);
          this.$emit('open-side-bar', this.showSidebar)
        }
      },
      logOut() {
        this.$store.commit('LOGOUT')
        window.localStorage.clear()
      }
    }
  }
</script>

<style lang="scss" scoped>
// router-link는 a태그로 인식됨
a {
  text-decoration: none;
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
      padding: 20px;
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
        padding-left: 10px;
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


.search {
  width: 140px;
}
.logout {
  border: none;
  background-color: rgb(200, 195, 191);
}
</style>