<template>
  <div id="app">
    <TopNavbar />
    <router-view />
  </div>
</template>

<script setup>
import TopNavbar from './components/TopNavbar.vue';
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
