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
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';

const userData = ref(null);
const errorMessage = ref('');
const router = useRouter();
const { setUser } = useUserStore();

const callback = (response) => {
  const decodedData = decodeCredential(response.credential);
  console.log("Handle the userData", decodedData);
  sendUserDataToBackend(decodedData);
};

function sendUserDataToBackend(decodedData) {
  axios.post('http://localhost:8000/auth/login', decodedData)
    .then(response => {
      console.log('User data saved:', response.data);
      userData.value = response.data.data;
      console.log('Data?: ', response.data.data);

      setUser(response.data.data);

      router.push('/experiment');
    })
    .catch(error => {
      console.error('Failed to save user data:', error);
      errorMessage.value = 'Something went wrong. Please choose another user, or try registering.';
    });
}
</script>

<style>
.error-message {
  color: red;
}
</style>
