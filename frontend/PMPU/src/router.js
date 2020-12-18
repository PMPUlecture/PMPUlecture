import Vue from "vue";
import Router from "vue-router";
import Programmes from "./components/Programmes";
import Login from "./components/Login";
import ProgramInfo from "./components/program/ProgramInfo";
import LecturerPage from "./components/lecturer/LecturerPage";
import AddMaterials from "./components/AddMaterials";
import P404 from "./views/P404";
import SearchPage from "./components/SearchPage";

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Programmes,
      meta: {title: "Пм-Пу"}
    },
    {
      path: '/login',
      component: Login,
      meta: {title: "Пм-Пу | Вход"}
    },
    {
      path: '/add_materials',
      component: AddMaterials,
    },
    {
      path: '/programme/:progID',
      component: ProgramInfo,
      props: true,
      meta: {title: "Пм-Пу| :progID"}
    },
    {
      path: '/lecturer/:lecturerID',
      component: LecturerPage,
      props: true,
      meta: {title: "Пм-Пу| Лектор"}
    },
    {
      path: '/search',
      component: SearchPage,
    },
    {
      path: '*',
      component: P404
    }
  ]
})

/*router.beforeEach((to, from, next) => {
  document.title = to.meta.title

  next()
});*/

export default router
