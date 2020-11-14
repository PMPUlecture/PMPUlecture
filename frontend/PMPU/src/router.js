import Vue from "vue";
import Router from "vue-router";
import Programmes from "./components/Programmes";
import Login from "./components/Login";
import ProgramInfo from "./components/ProgramInfo";

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
      path: '/programme/:progID',
      component: ProgramInfo,
      props: true
    },
  ]
})
