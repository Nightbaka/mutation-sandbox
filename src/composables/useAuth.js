// src/composables/useAuth.js
import { reactive } from 'vue';
import axios from 'axios';

export function useAuth() {
  const state = reactive({
    isAuthenticated: false,
    user: null,
    token: null
  });

  const authenticate = async (provider) => {
    try {
      const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?client_id=YOUR_CLIENT_ID&redirect_uri=${encodeURIComponent('http://localhost:8080/auth/callback')}&response_type=code&scope=openid email profile`;
      window.location.href = authUrl;
    } catch (error) {
      console.error('Authentication error:', error);
    }
  };

  return {
    state,
    authenticate
  };
}
