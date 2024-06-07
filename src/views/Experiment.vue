<template>
    <div class="user-profile">
      <h1>{{ username }}</h1>
      <p>{{ bio }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserProfile',
    data() {
      return {
        username: '***Experiments***'
      };
    }
  }
  </script>
  
  <style scoped>
  .user-profile h1 {
    color: navy;
  }
  .user-profile p {
    font-size: 16px;
  }
  </style>
  