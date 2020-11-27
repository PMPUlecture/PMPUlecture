import Vue from "vue";
import Router from "vue-router";
import Programmes from "./components/Programmes";
import Login from "./components/Login";
import ProgramInfo from "./components/ProgramInfo";
import LecturerPage from "./components/lecturer/LecturerPage";
import AddMaterials from "./components/AddMaterials";

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
      path: '/add_materials',
      component: AddMaterials,
    },
    {
      path: '/programme/:progID',
      component: ProgramInfo,
      props: true
    },
    {
      path: '/lecturer/:lecturerID',
      component: LecturerPage,
      props: true
    }
  ]
})
