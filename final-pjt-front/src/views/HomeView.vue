<template>
  <div class="home">
    <!-- <div 
      data-aos="slide-up" 
      data-aos-easing="ease-out-sine" 
      data-aos-offset="100"  
      data-aos-delay="1000" 
      data-aos-duration="3000"
      data-aos-anchor-placement="bottom-center" 
      data-aos-once="false"> -->

    <div>
      <h1>MOVIE</h1>
    </div>  
    <!-- <div class="ball" @click="logIn">
    </div> -->
    <div class="box">
      <img src="https://i.pinimg.com/564x/83/33/9d/83339d35fe78f3560079301346164b42.jpg" alt="">
      <div class="loader" @animationend="popDiv"></div>
      <LogIn class="login-pop animate__animated animate__fadeIn"/>
    </div>

  </div>
</template>


<script src="bower_components/aos/dist/aos.js"></script>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
// var AOS = require('aos');
AOS.init();

import LogIn from "@/components/LogIn";

export default {
  name: "HomeView",
  components: {
    LogIn,
  },
  data() {
    return {
      popLogin: false,
    };
  },
  methods: {
    popDiv() {
      this.popLogin = true;
    },
  },
};
</script>



<style scoped>
@import url(https://fonts.googleapis.com/css?family=Lato:300);

.home {
  position: relative;
  justify-content: center;
  width: 100vw;
  height: 100vh;
  vertical-align: center;
}

.box {
  display: inline-block;
  position: relative;
  margin-top: 60px;
  height: 90vh;
  width: 800px;
}

img {
  padding: 0;
  width: 800px;
}

.home > div > h1 {
  font-size: 8rem;
  z-index: 3;
  position: absolute;
  font-family: Harmond;
  margin: 0;
  top: 80px;
  color: #E6C628;
  text-shadow: 3px 3px #764E03;
  /* background-color: black; */
  width: 100%;
}
.loader{
  position: absolute;
  width: 800px;
  height: 30px;

  left: 0;
  background-color: rgba(255,255,255,0.2);
}

.loader:before{
  content: "";
  position: absolute;
  background-color: #fff;
  top: 0px;
  left: 0;
  height: 30px;
  width: 0px;
  z-index: 0;
  opacity: 1;
  -webkit-transform-origin:  100% 0%;
      transform-origin:  100% 0% ;
  -webkit-animation: loader 10s ease-in-out forwards;
      animation: loader 10s ease-in-out forwards;
}

.loader:after{
  content: "LOADING ...";
  color: #fff;
  font-family:  Lato,"Helvetica Neue" ;
  font-weight: 200;
  font-size: 20px;
  position: absolute;
  width: 100%;
  height: 30px;
  line-height: 30px;
  left: 0;
  top: 0;
}

@-webkit-keyframes loader{
    0%{width: 0px;}
    70%{width: 100%; opacity: 1;}
    90%{opacity: 1; width: 100%;}
    100%{opacity: 1;width: 100%;}
}

@keyframes loader{
    0%{width: 0px;}
    70%{width: 100%; opacity: 1;}
    90%{opacity: 1; width: 100%;}
    100%{opacity: 1;width: 100%;}
}


@keyframes ball {
  0% {
    top: 0px;
  }
  95% {
    width: 100px;
  }
  to {
    top: 300px;
    width: 115px;
    /* height:90px */
  }
}

.login-pop {
  /* animation-delay: 6.7s; */
}
.ball {
  position: relative;
  left: 200px;
  top: 0;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: rgb(228, 212, 212);
  animation: ball 1s ease-in Infinite Alternate;
}

</style>