<template>
  <div id="app">
    <h1 id="title">SORT VISUALISER</h1>
    <Body
      :clickEventObj="clickEventObj"
      :sortingSpeed="sortingSpeed"
      @isSorting="(state) => (sortingState = state)"
    />
    <Navbar
      :sortingState="sortingState"
      @clickEventObject="(object) => (clickEventObj = object)"
      @speed="speed = sortingSpeed"
    />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      clickEventObj: {},
      sortingState: false,
      sortingSpeed: 1,
    };
  },
  components: {
    Navbar: () => import("./components/Navbar.vue"),
    Body: () => import("./components/Body.vue"),
  },
};
</script>

<style>
body {
  margin: 0px;
  padding: 0px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #1f3b97;
  height: 98vh;
  margin: 0;
  padding: 0;
  overflow: hidden;
}
#title {
  margin: 0px;
  margin: 50px 0;
  font-size: 50px;
}
</style>
