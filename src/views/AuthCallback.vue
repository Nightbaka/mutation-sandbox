// src/views/AuthCallback.vue
<template>
  <div>
    <h1>Authentication Callback</h1>
    <p>Processing...</p>
  </div>
</template>

<script>
import { onMounted } from 'vue';
import axios from 'axios';

export default {
  setup() {
    onMounted(() => {
      const code = new URL(window.location.href).searchParams.get('code');
      if (code) {
        axios.post('http://localhost:8000/api/token/', {
          code,
          redirect_uri: 'http://localhost:8080/auth/callback'
        })
        .then(response => {
          console.log('Token received:', response.data);
          // Handle storing the token, setting authentication state, etc.
        })
        .catch(error => {
          console.error('Error exchanging code for token:', error);
        });
      }
    });
  }
}
</script>
