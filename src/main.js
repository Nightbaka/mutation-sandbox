import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index.js';
import vue3GoogleLogin from 'vue3-google-login'

const app = createApp(App);
app.use(vue3GoogleLogin, {
    clientId: '39509314769-c2f05oefah75st584d3f9cuibqsamu2h.apps.googleusercontent.com'
  })
app.use(router);
app.mount('#app');