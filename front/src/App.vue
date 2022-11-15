<template>
  <div id="app">
    <div class="side-bar">
      <b-button v-b-toggle.sidebar-1>사이드바</b-button>
      <b-sidebar id="sidebar-1" title="Sidebar" shadow>
        <div class="px-3 py-2">
          <p>
            사이드바에 넣을 내용들
          </p>
          <b-img src="https://i.pinimg.com/736x/e1/9f/47/e19f4768a10c3f399fd5ba92fc4186eb.jpg" fluid thumbnail></b-img>
        </div>
      </b-sidebar>
    </div>
    <router-view/>
  </div>
</template>

<style>

html {
  scroll-behavior: initial;
  background-color: rgb(212, 201, 201);
}

html,
body {
  width: 100%;
  min-height: 100%;
}

#app {
  margin: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: rgb(212, 201, 201);
}

.home {
  color: black;
  /* text-shadow: 2px 2px 3px rgb(161, 139, 139); */
  position: absolute;
  text-align: center;
}

.home>img {
  /* width: 20rem; */
  height: 30rem;
  z-index: 1;
  position: relative;
}
.home>div>h1 {
  font-size: 5rem;
  z-index: 2;
  position: relative;
}

.side-bar {
  text-align: left;
}


/* nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
} */


</style>


// <script>
//   AOS.init();
// </script>