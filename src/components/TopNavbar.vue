<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <router-link to="/">Mutation Sandbox</router-link>
    </div>
    <div class="navbar-links">
      <router-link to="/experiment">Experiments</router-link>
      <router-link to="/history">History</router-link>
    </div>
    <div class="navbar-user" v-if="userData">
      <span>{{ user.username }}</span>
    </div>
  </nav>
</template>

<script setup>
import { computed } from 'vue';
import { useUserStore } from '@/stores/user';

const { user } = useUserStore();
const userData = computed(() => user.value);

</script>

<style>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #333;
  color: white;
}

.navbar-brand, .navbar-links, .navbar-user {
  display: flex;
  align-items: center;
}

.navbar-links a, .navbar-brand a {
  margin-right: 1rem;
  color: white;
  text-decoration: none;
}

.user-image {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-left: 10px;
}
</style>
