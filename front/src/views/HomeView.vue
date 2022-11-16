<template>
  <div class="home">
    <div 
      data-aos="slide-up" 
      data-aos-easing="ease-out-sine" 
      data-aos-offset="200"  
      data-aos-delay="1000" 
      data-aos-duration="3000"
      data-aos-anchor-placement="bottom-center" 
      data-aos-once="false">
      <h1>MOODY</h1>
    </div>
    <div class="ball">
      <p>로그인</p>
    </div>
    <SignUp/>
    <hr>
    <LogIn/>
    <!-- <img src="https://i.pinimg.com/564x/9a/5d/63/9a5d639d97a1e32db48e3c99326ccd1e.jpg" alt=""> -->
    <!-- <img class="top-image" src="https://i.pinimg.com/564x/48/32/9b/48329b6a1f27db84fa7fbbce55059557.jpg" alt="">
    <img src="https://i.pinimg.com/736x/99/6e/03/996e037a9b237f9b191981d5f7ef503d.jpg" alt="">
    <img src="https://i.pinimg.com/564x/41/86/4c/41864ca7c48a1e19d4a1c66f7e089773.jpg" alt="">
    <img src="https://i.pinimg.com/564x/47/61/71/4761712df14dd51d38df928db1dafc0f.jpg" alt=""> -->

    <!-- <img src="https://i.pinimg.com/564x/20/ce/63/20ce637e3c64d88a9b03f5417cf5238a.jpg" alt="">
    <img src="https://i.pinimg.com/564x/60/a4/d6/60a4d623da697816d74358349f71f135.jpg" alt="">
    <img src="https://i.pinimg.com/736x/73/29/ae/7329aeb267adb9078deb2000f9f63e75.jpg" alt="">
    <img src="https://i.pinimg.com/564x/51/61/3f/51613f8e421624a07c547f84cc972a53.jpg" alt="">
     -->
    <img src="https://i.pinimg.com/564x/59/ec/f6/59ecf6b1014140e645931a27ee9e0869.jpg" alt="">
    <img src="https://i.pinimg.com/736x/14/7a/ec/147aec9f1bb6c4586b718a0ace9121ca.jpg" alt="">
    <!-- <img src="https://i.pinimg.com/564x/8c/53/fe/8c53fe970d55bdbd6835032d504ce3b6.jpg" alt=""> -->


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
}
</script>



<style>
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


</style>