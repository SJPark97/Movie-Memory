<template>
  <div class="home">
    <div data-aos="slide-up" data-aos-offset="50"  data-aos-delay="500">
      <h1>Main</h1>
    </div>
    <img src="https://i.pinimg.com/564x/53/a1/8c/53a18cbcee04b60cc8baf57e391b6141.jpg" alt="">
    <LogIn/>
    <SignUp/>
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
  }
}
</script>



<style>


</style>