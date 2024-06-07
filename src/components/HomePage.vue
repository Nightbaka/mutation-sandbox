<!-- src/components/HomePage.vue -->
<template>
    <div class="home-page">
      <button @click="navigateTo('Registration')">Sign Up</button>
      <button @click="navigateTo('Login')">Sign In</button>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  function navigateTo(routeName) {
    router.push({ name: routeName });
  }
  </script>
  
  <style scoped>
  .home-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 50px;
  }
  
  button {
    margin: 10px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  </style>
  