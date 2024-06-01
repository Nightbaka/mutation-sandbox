<template>
    <div>
      <button @click="login">Login with Google</button>
    </div>
  </template>
  
  <script setup>
  import userManager from '@/services/userManager';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  function login() {
    userManager.signIn().then(() => {
      const redirect = router.currentRoute.value.query.redirect || '/';
      router.push(redirect);
    }).catch(error => {
      console.error('Login failed:', error);
    });
  }
  </script>
  