import { ref } from 'vue';

const user = ref(null);

export const useUserStore = () => {
  const setUser = (userData) => {
    user.value = userData;
  };

  return {
    user,
    setUser
  };
};
