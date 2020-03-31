<template>
  <div id="app">
    <!-- <hello></hello> -->
    <main-guide />
    <br>
    <router-view />
  </div>
</template>
<script>
import hello from "./views/Hello";
import MainGuide from "./components/guide/MainGuide";

export default {
  name: "App",
  components: {
    hello,
    MainGuide
  }
};
</script>
<style>
</style>
