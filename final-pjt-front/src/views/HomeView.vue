<template>
  <div class="home">
    
    <!-- 영화 명언 -->
    <h5>{{ famousLine }}</h5>

    <div>
      <h1>MOVIE</h1>
    </div>  
    <div class="box">
      <img src="https://i.pinimg.com/564x/83/33/9d/83339d35fe78f3560079301346164b42.jpg" alt="">
      <div class="loader" @animationend="popDiv"></div>
      <LogIn class="login-pop animate__animated animate__fadeIn" v-show="!this.$store.state.username"/>
    </div>
    <!-- <div  @click="goToHome" class="move animate__animated animate__fadeIn">
      <p>move</p>
    </div> -->
    <SetProfile v-show="this.$store.state.token && !this.$store.state.userId"/>
    <!-- <SetProfile /> -->
  </div>
</template>


<script>
import LogIn from "@/components/LogIn";
import SetProfile from "@/components/SetProfile";
import _ from 'lodash'

const famousLines = [
  "나는 매 순간을 꽉 차게 느끼며 살아갈 거야", 
  "치열하기 살던가, 죽기만을 기다리던가",
  "자신의 존재는 잊어도 인생이 준 최고의 선물은 잊지 마",
  "우리 모두 어둠을 밝히려는 길 잃은 별들이 아닐까요?",
  "인생은 미로 같고 사랑은 수수께끼 같죠",
  "내 인생은 비극인 줄 알았는데 코미디였어",
  "잊히지 않을 것 같은 무더운 여름 뒤엔 가을도 온다 분명히",
  "내일은 내일의 해가 뜬다",
  "우리가 두려워할 것은 두려움뿐이죠",
  "꿈은 도망가지 않아, 도망가는 것은 언제나 나 자신이야",
  "난 가고 싶은 곳에 가기 위해 뛰었는데 그게 삶의 기회가 될 줄은 몰랐어요"
]

export default {
  name: "HomeView",
  components: {
    LogIn,
    SetProfile,
  },
  data() {
    return {
      popLogin: false,
    };
  },
  computed: {
    famousLine() {
      return _.sample(famousLines)
    }
  },
  methods: {
    popDiv() {
      this.popLogin = true;
    },
    goToHome() {
      this.$router.push({ name : 'main'})
    }
  },
};
</script>



<style scoped>
@import url(https://fonts.googleapis.com/css?family=Lato:300);
@import url('https://webfontworld.github.io/Rebecca/Rebecca.css');

h5 {
  font-family: 'Rebecca';
  color: #58504e;
  text-shadow: 1px 1px  #F0E2D7;
}

.home {
  position: relative;
  justify-content: center;
  width: 100vw;
  height: 100vh;
  vertical-align: center;
  padding-top: 20px;
}

/* .box {
  display: inline-block;
  position: relative;
  margin-top: 60px;
  height: 90vh;
  width: 800px;
} */
.box {
  display: inline-block;
  /* position: absolute; */
  /* justify-content: center; */
  width: 80%;
  margin-top: 0px;
}

img {
  padding: 0;
  width: 80%;
}

.home > div > h1 {
  font-size: 10vw;
  z-index: 3;
  position: absolute;
  font-family: Harmond;
  margin: 0;
  top: 110px;
  color: #E6C628;
  text-shadow: 3px 3px #764E03;
  /* background-color: black; */
  width: 100%;
}
.loader{
  position: absolute;
  width: 64%;
  height: 30px;
  left: 18%;
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
  animation-delay: 6.7s;
}
.move {
  font-size: 3vw;
  z-index: 3;
  position: absolute;
  margin: 0;
  top: 25%;
  width: 16%;
  left: 42%;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 100%;
  text-align: center;
}

.signup-div {
  display: inline-block;
  width: 550px;
  height: 500px;
  position: absolute;
  /* object-fit: contain; */
  top: 100px;
  left: 200px;
  padding-top: 40px;
  padding-left: 60px;
  padding-right: 60px;
  border: 1px solid gray;
  box-shadow: 5px 5px 10px 3px rgb(136, 136, 136);
  z-index: 999;
  background-color: rgb(218, 210, 210);
}
.signup-div > h2 {
  margin-bottom: 20px;
}

.signup-input { 
  display: inline-block;
  position: relative;
  width: 430px;
  display: flex;
  justify-content: space-between;
  margin-top: 5px;
}


.signup-input > input {
  width: 300px;
  height: 33px;
  border: 1px solid gray;
  border-radius: 8px;
}

.input-btn {
  margin-top: 20px;
  margin-bottom: 20px;
}

</style>