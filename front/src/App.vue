<template>
  <div id="app">
    <SideBar @open-side-bar="OpenSideBar"/>
    <div :class="`${pullDiv ? 'is-pulled' : 'is-back'}`">
              <!-- data-aos="fade-right"
        data-aos-offset="100"
        data-aos-duration="1000"
        data-aos-easing="ease-out-sine" -->
      <router-view
      ></router-view>
    </div>

  </div>
</template>

<script>
  import SideBar from '@/components/SideBar.vue'

  export default {
    data() {
      return {
        pullDiv: false,
      }
    },
    components: {
      SideBar,
    },
    methods: {
      getMovies() {
        this.$store.dispatch('getMovies')
      },
      OpenSideBar(open) {
        if (open === true) {
          this.pullDiv = true
        } else {
          this.pullDiv = false
        }
        console.log(this.pullDiv)
      }
    },
    created() {
      this.getMovies()
    }
  }
</script>

<style lang="scss">
@import url("https://use.fontawesome.com/releases/v5.13.0/css/all.css");

@font-face {
  font-family: "Harmond";
  src: local("Harmond"),
    url(./fonts/Harmond-ExtBdItaExp.otf) format("truetype")
}
@import url('https://fonts.googleapis.com/css2?family=Hahmlet:wght@200;300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&display=swap');


html {
  scroll-behavior: initial;
  background-color: rgb(212, 201, 201);
}

html,
body {
  min-height: 100%;
  background-color: rgb(212, 201, 201);
  width: 100vw;
  // overflow-x: hidden;
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

div {
  margin: 0;
  padding-top: 5px;
  font-family: 'Hahmlet', serif;
}

p {
  margin: 0;
}

.is-pulled {
  margin-left: 180px;
  transition: .5s;
}

.is-back {
  margin-left: 0;
  transition: .5s;
  transition-delay: .17s;
}


</style>
