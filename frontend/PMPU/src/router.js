import Vue from "vue";
import Router from "vue-router";
import Programmes from "./components/Programmes";
import Login from "./components/Login";

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Programmes
    },
    {
      path: '/login',
      component: Login,
    },
    {
      path: '/account/logout',
      beforeEnter(to, from, next) {
        // Put the full page url including the protocol http(s) below
        window.location = "http://127.0.0.1:8000/account/logout/"
      }
    }
  ]
})
