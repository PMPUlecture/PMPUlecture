import Vue from 'vue'
import App from './App.vue'
import VueCookies from 'vue-cookies';
import router from "./router";

Vue.use(VueCookies);

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
