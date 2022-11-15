<template>
  <div id="app">
    <font-awesome-icon icon="fa-regular fa-bell" />
    <SideBar/>
    <!-- <div class="side-bar">
      <b-button v-b-toggle.sidebar-1>사이드바</b-button>
      <b-sidebar id="sidebar-1" title="Sidebar" shadow>
        <div class="px-3 py-2">
          <font-awesome-icon icon="fa-regular fa-bell" />
          <p>
            사이드바에 넣을 내용들
          </p>
          <b-img src="https://i.pinimg.com/736x/e1/9f/47/e19f4768a10c3f399fd5ba92fc4186eb.jpg" fluid thumbnail></b-img>
        </div>
      </b-sidebar>
    </div> -->
    <div class="content" :class="{'shrink':showNav}" @click="showNav = false">
      <router-view>
        <div id="navigation-icon">
          <i class="fas fa-bars" @click.stop="showNav = true"></i>
        </div>
      </router-view>
    </div>    
  </div>
</template>

<script>
  import SideBar from '@/components/SideBar.vue'

  export default {
    name: 'App',
    data() {
      return {
        showNav: false,
      }
    },
    components: {
      SideBar,
    },
    watch: {
      $route() {
        this.showNav = false;      
      },
    }
  }
</script>

<style>
@import url("https://use.fontawesome.com/releases/v5.13.0/css/all.css");

@font-face {
  font-family: "Harmond";
  src: local("Harmond"),
    url(./fonts/Harmond-ExtBdItaExp.otf) format("truetype")
}
@import url('https://fonts.googleapis.com/css2?family=Hahmlet:wght@200;300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&display=swap');

* {
  box-sizing: border-box;
}


html {
  scroll-behavior: initial;
  background-color: rgb(212, 201, 201);
}

html,
body {
  min-height: 100%;
  /* background-color: #03754f; */
  width: 100vw;
  overflow-x: hidden;
}

#app {
  margin: 0;
  font-family: 'Hahmlet', serif;
  font-family: 'Cinzel', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: rgb(212, 201, 201);
  color: black;
}

.home {
  position: absolute;
  justify-content: center;
  width: 100%;
}

.top-image {
  height: 30rem;
  z-index: 1;
  /* position: relative; */
  top: 0px;
}

.home>img {
  /* -webkit-transform: rotate(90deg);  */
  margin: 0;
  padding: 0;
  /* display: inline-block; */
  position: relative;
  height: 30rem;
  /* width: rem; */
  object-fit: contain;
  top: 100px;
}

@keyframes ball {
  0% {
    top:0px;
  }
  95% {
    width: 100px;
  }
  to {
    top:300px;
    width:115px;
    /* height:90px */
  } 
}

.ball {
  position:relative;
  left: 100px;
  top:0;
  width:100px;
  height:100px;
  border-radius:50%;
  background:rgb(228, 212, 212);
  animation:ball 1s ease-in Infinite Alternate;
}

.home>div>h1 {
  font-size: 5rem;
  z-index: 2;
  position: relative;
  font-family: Harmond;
  margin: 0;
  top: 50px;
}

.side-bar {
  text-align: left;
}

#navigation-icon > i {
    cursor: pointer;
    font-size: 2rem;
    padding: 4px;
    color: black;
  }
  .content {
    position: absolute;
    top: 0;
    width: 100vw;
    min-height: 100vh;
    padding: 16px;
    background-color: #fff;
    transition: .3s all ease-in-out;
  }
  .shrink {
    transform: scale(.9) translateX(250px);
    border-radius: 20px;    
    height: 100vh;
    overflow: hidden;
    box-shadow: -5px 5px 20px #333;
    cursor: pointer;
  }

</style>
