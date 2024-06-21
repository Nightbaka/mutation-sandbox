<template>
  <div>
    <GoogleLogin :callback="callback" prompt />
    <div v-if="errorMessage" class="error-message">
      <p>{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { decodeCredential } from 'vue3-google-login';
import axios from 'axios';

const errorMessage = ref('');

const callback = (response) => {
  const userData = decodeCredential(response.credential);
  console.log("Handle the userData", userData);

  sendUserDataToBackend(userData);
};

function sendUserDataToBackend(userData) {
  axios.post('http://localhost:8000/auth/register', userData)
    .then(response => {
      console.log('User data saved:', response.data);
      // Handle response from the backend (e.g., navigate to another page)
    })
    .catch(error => {
      console.error('Failed to save user data:', error);
      errorMessage.value = 'Failed to save user data. Try logging in instead.'; // Set the error message
    });
}
</script>

<style>
.error-message {
  color: red;
}
</style>
