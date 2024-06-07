<script setup>
import { decodeCredential } from 'vue3-google-login'
import axios from 'axios'
const callback = (response) => {
  
  const userData = decodeCredential(response.credential)
  console.log("Handle the userData", userData)

  sendUserDataToBackend(userData)
};

function sendUserDataToBackend(userData) {
  axios.post('http://localhost:8000/auth/register', userData)
    .then(response => {
      console.log('User data saved:', response.data);
      // Handle response from the backend (e.g., navigate to another page)
    })
    .catch(error => {
      console.error('Failed to save user data:', error);
      // Handle errors here
    });
}
</script>

<template>
  <GoogleLogin :callback="callback" prompt/>
</template>