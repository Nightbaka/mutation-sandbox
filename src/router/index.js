import { createRouter, createWebHistory } from 'vue-router';
import Experiment from '../views/Experiment.vue';
import History from '../views/History.vue';
import AuthCallback from '../views/AuthCallback.vue'
import userLogin from '../components/userLogin.vue'
import userManager from '@/services/userManager';

const routes = [
  {
    path: '/',
    name: 'Experiment',
    component: Experiment,
    meta: { requiresAuth: true }
  },
  {
    path: '/experiment',
    name: 'Experiment',
    component: Experiment,
    meta: { requiresAuth: true }
  },
  {
    path: '/history',
    name: 'History',
    component: History,
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: userLogin
  },
  { path: '/callback',
   component: AuthCallback }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach(async (to, from, next) => {
  const user = await userManager.getUser();
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (user && !user.expired) {
      next();
    } else {
      next({ name: 'Login', query: { redirect: to.fullPath } });
    }
  } else {
    next();
  }
});

export default router;
