import { createRouter, createWebHistory } from 'vue-router';
import Experiment from '../views/Experiment.vue';
import History from '../views/History.vue';
import userLogin from '../components/userLogin.vue'
import userRegistration from '../components/userRegistration.vue';
import HomePage from '../components/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
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
    component: userLogin,
    // meta: { requiresAuth: false }
  },
  {
    path: '/registration',
    name: 'Registration',
    component: userRegistration,
    // meta: { requiresAuth: false }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});


export default router;
