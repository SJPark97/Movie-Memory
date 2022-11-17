<template>
  <div class="container" :class="{'show': showSidebar}">
    <div class="control">
      <i class="fas fa-angle-double-right" @click="showNav"></i>
    </div>
    <!-- <div class="navigation-icons">
      <router-link to="/main"><i class="fas fa-home"></i></router-link>
      <router-link to="/movies"><i class="fas fa-video"></i></router-link>
      <i class="fas fa-bell"></i>
    </div> -->
    <div class="navigation-links">
      <transition-group name="fade">
        <div v-show="showLink" key="1"><router-link to="/main">Home</router-link></div>
        <div v-show="showLink" key="2"><router-link to="/movies">Movies</router-link></div>
        <div v-show="showLink" key="3"><router-link to="/">#</router-link></div>
        <div v-show="showLink" key="4"><router-link to="/">#</router-link></div>
        <div v-show="showLink" key="5"><button @click="logOut">LOGOUT</button></div>

      </transition-group>
    </div>
    <!-- <i class="fas fa-music"></i> -->
  </div>
</template>

<script>
  export default {
    data: () => {
      return {
        showSidebar: false,
        showLink: false
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

  .container {
    position: absolute;
    top: 0;
    left: 0;
    width: 0px;
    padding: 0px;
    min-height: calc(100vh - 20px);
    background-color: rgba($color: rgb(200, 195, 191), $alpha: .8);
    border: solid #fff;
    border-width: 0 1px 0 0;
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
        font-size: 2rem;
        cursor: pointer;
        transition: all .5s ease-in-out;
      }
    }
    &.show {
      width: 180px;
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
    @include nav-childs(1,2,3,4,5);
  }
  .fade-enter, .fade-leave-to {
    transform: scale(0);
  }
</style>