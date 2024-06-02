<template>
  <div>Logging you in...</div>
</template>

<script setup>
import userManager from '@/services/userManager';
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const router = useRouter();
const route = useRoute();

onMounted(async () => {
  try {
    await userManager.signinRedirectCallback();
    router.push(route.query.redirect || '/');
  } catch (error) {
    console.error('Error handling authentication callback:', error);
    router.push('/login');
  }
});
</script>
