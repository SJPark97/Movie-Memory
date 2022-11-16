<template>
  <div class="home">
    <div 
      data-aos="slide-up" 
      data-aos-easing="ease-out-sine" 
      data-aos-offset="100"  
      data-aos-delay="1000" 
      data-aos-duration="3000"
      data-aos-anchor-placement="bottom-center" 
      data-aos-once="false">
      <h1>MOVIE</h1>
    </div>
    <article class="accordion">
      <section id="acc1">
        <h2><a href="#acc1">LOGIN</a></h2>
        <LogIn/>
      </section>
      <section id="acc2">
        <h2><a href="#acc2">SIGNUP</a></h2>
        <SignUp/>
      </section>
    </article>
    <div class="ball" @click="logIn">
      <p>로그인</p>
    </div>
    <!-- <img class="top-image" src="https://i.pinimg.com/564x/59/ec/f6/59ecf6b1014140e645931a27ee9e0869.jpg" alt=""> -->
    <!-- <img class="top-image" src="https://i.pinimg.com/736x/14/7a/ec/147aec9f1bb6c4586b718a0ace9121ca.jpg" alt=""> -->
    <!-- <img class="top-image" src="https://i.pinimg.com/564x/8c/53/fe/8c53fe970d55bdbd6835032d504ce3b6.jpg" alt=""> -->
  </div>
</template>


<script src="bower_components/aos/dist/aos.js"></script>
<script>
import AOS from 'aos';
import 'aos/dist/aos.css';
// var AOS = require('aos');
AOS.init();

import LogIn from '@/components/LogIn'
import SignUp from '@/components/SignUp'

export default {
  name: 'HomeView',
  components: {
    LogIn,
    SignUp,
  },
  data() {
    return {
      formAva: false,
    }
  },
  methods: {
    logIn() {
      this.formAva = true
    }
  }
}
</script>



<style>

.home {
  position: relative;
  justify-content: center;
  width: 100%;
}

.top-image {
  height: 10rem;
  z-index: 2;
  /* position: relative; */
  top: 0px;
}

.home>img {
  /* -webkit-transform: rotate(90deg);  */
  margin: 0;
  padding: 0;
  /* display: inline-block; */
  position: relative;
  height: 800px;
  width: 400px;
  object-fit: contain;
  top: 0;
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
  left: 200px;
  top:0;
  width:100px;
  height:100px;
  border-radius:50%;
  background:rgb(228, 212, 212);
  animation:ball 1s ease-in Infinite Alternate;
}

.home>div>h1 {
  font-size: 5rem;
  z-index: 3;
  position: relative;
  font-family: Harmond;
  margin: 0;
  top: 50px;
}

.auth-div {
  display: inline-block;
  width: 500px;
  height: 300px;
  position: absolute;
  /* object-fit: contain; */
  top: 100px;
  left:100px;
  padding: 50px;
  border: 1px solid gray;
  box-shadow: 5px 5px 10px 3px rgb(136, 136, 136);
  z-index: 999; 
  background-color: rgb(218, 210, 210);
}

.auth-div>form>input {
  margin-bottom: 10px;
}

article.accordion
{
    display: block;
    width: 50em;
    margin: 0 auto;
    background-color:rgb(212, 201, 201);
    overflow: auto;
    border-radius: 5px;
    /* box-shadow: 0 3px 3px rgba(0,0,0,0.3); */
}
article.accordion section
{
    position: relative;
    display: block;
    float: left;
    width: 2em;
    height: 25em;
    margin: 0.5em 0 0.5em 0.5em;
    color: rgb(107, 55, 55);
    background-color: rgb(207, 191, 191);
    overflow: hidden;
    border-radius: 3px;
}
article.accordion section h2
{
    position: absolute;
    font-size: 1.2em;
    font-weight: bold;
    width: 12em;
    height: 2em;
    top: 15em;
    left: 0;
    text-indent: 1em;
    padding: 0;
    margin: 0;
    color: rgb(0, 0, 0);
    -webkit-transform-origin: 0 0;
    -moz-transform-origin: 0 0;
    -ms-transform-origin: 0 0;
    -o-transform-origin: 0 0;
    transform-origin: 0 0;
    -webkit-transform: rotate(-90deg);
    -moz-transform: rotate(-90deg);
    -ms-transform: rotate(-90deg);
    -o-transform: rotate(-90deg);
    transform: rotate(-90deg);
}
article.accordion section h2 a
{
    display: block;
    width: 100%;
    line-height: 2em;
    text-decoration: none;
    color: inherit;
    outline: 0 none;
}
article.accordion section:target
{
    width: 40rem;
    padding: 0 1em;
    color: rgb(196, 164, 164);
    background-color: #fff;
}
article.accordion section:target h2
{
    position: static;
    font-size: 2em;
    text-indent: 0;
    color: #333;
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
}
article.accordion section,
article.accordion section h2
{
    -webkit-transition: all 1s ease;
    -moz-transition: all 1s ease;
    -ms-transition: all 1s ease;
    -o-transition: all 1s ease;
    transition: all 1s ease;
}

</style>