import Vue from "vue";
import Router from "vue-router";
import Programmes from "./components/Programmes";
import Login from "./components/Login";
import ProgramInfo from "./components/ProgramInfo";
import LecturerPage from "./components/lecturer/LecturerPage";

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
    }
  ]
})

/*router.beforeEach((to, from, next) => {
  document.title = to.meta.title

  next()
});*/

export default router
