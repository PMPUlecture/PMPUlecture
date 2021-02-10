<template>
  <div>
    <!-- Верхняя панель -->
    <header>
  <div class="container mb-5">
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top mb-5">
      <router-link class="navbar-brand" to="/"><b style="margin-left: 42px">База знаний ПМ-ПУ</b></router-link>

    <!-- Кнопка для выпадающего списка (активируется только на <lg экранах) -->
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <!-- Форма для авторизированных пользователей -->
      <div class="mr-auto mt-2 mt-lg-0  d-lg-none d-block">
        <div v-if="user.is_authenticated" class="d-flex flex-column">
        <div class="bg-info p-2 rounded d-flex flex-row justify-content-between">
          <span class="m-auto">Добро пожаловать, <b>{{user.first_name + ' ' + user.last_name}}</b></span>
          <a href="/account/logout/" class="btn btn-danger">Выйти</a>
        </div>
          <router-link :to="'/add_materials'" class="btn btn-outline-light mt-2" data-toggle="collapse" data-target="#navbarTogglerDemo01">
            Добавить материал
          </router-link>
        </div>

        <!-- Форма для неавторизированных пользователей -->
        <div v-else class="bg-warning p-2 rounded d-flex flex-row justify-content-between">
          <span class="text-center">Войдите, чтобы видеть больше материалов и добавлять новые</span>
          <a class="btn btn-danger mt-auto mb-auto" href="/account/login/google-oauth2/"><i class='fab fa-google' style="font-size: large"></i></a>
        </div>
      </div>

      <br>
      <!-- Полезные ссылки -->
        <UsefulLinks class="list-group d-lg-none d-block"></UsefulLinks>
      <form @submit.prevent="search" class="form-inline my-2 my-lg-0 ml-auto">
        <input v-model="searchInput" class="form-control mr-sm-2" type="text" placeholder="Найти лектора">
        <button class="btn btn-secondary my-2 my-sm-0" type="submit">Поиск</button>
      </form>
    </div>
  </nav>
  </div>
    </header>

    <div class="container-fluid">
      <div class="row mb-5"></div>

      <div class="row">
        <div class="col-3 d-none d-lg-block">  <!-- левая колонка со ссылками, не меняется -->

            <div class="d-flex flex-column justify-content-between my-sticky-top">
              <div class="card">
                <div class="card-body">
                  <UsefulLinks class="list-group list-group-flush"></UsefulLinks>
                </div>
              </div>


              <template v-if="user.is_authenticated && user.is_admin">
                <div class="card text-white bg-success mt-3 mb-3">
                  <a href="/admin/" style="text-decoration: none" class="text-white">
                    <h3 class="card-header text-center"><b>{{user.first_name}} {{user.last_name}}</b></h3>
                  </a>
                  <div class="card-body">
                    <h4 class="card-title">Вы являетесь администратором</h4>
                    <p class="card-text">Можете продолжить смотреть учебные материалы или добавить свои тут</p>

                    <div class="d-flex justify-content-between">
                      <router-link :to="'/add_materials'">
                        <button class="btn btn-outline-primary">Добавить </button>
                      </router-link>
                      <a href="/account/logout/" class="btn btn-danger">Выйти</a>
                    </div>
                  </div>
                </div>

              </template>

                <template v-else-if="user.is_authenticated && !user.is_admin">
                  <div class="card text-white bg-info mt-3 mb-3">
                    <h3 class="card-header text-center"><b>{{user.first_name}} {{user.last_name}}</b></h3>
                      <div class="card-body">
                        <h4 class="card-title">Добро пожаловать {{user.email}}</h4>
                        <p class="card-text">Материалы, видимые только студентами помечаются значком <i class="fas fa-eye text-warning"></i>. .</p>
                        <p>Можете продолжить смотреть учебные материалы или добавить свои тут</p>

                        <div class="d-flex justify-content-between">
                          <router-link :to="'/add_materials'">
                              <button class="btn btn-outline-primary">Добавить </button>
                          </router-link>
                          <a href="/account/logout/" class="btn btn-danger">Выйти</a>
                      </div>
                      </div>
                  </div>

                </template>

                <template v-else>
                  <div class="card text-white bg-warning mt-3 mb-3">
                  <div class="card-body">
                    <h4 class="card-title">Вход не выполнен</h4>
                    <p class="card-text">Вы не вошли на сайт.</p>
                    <p class="card-text">Вы можете просматривать материалы, но чтобы видеть дополнительные и добавлять свои
                    необходимо войти.</p>
                    <a class="btn btn-danger" href="/account/login/google-oauth2/">Вход через Google</a>

                  </div>
                  </div>
                </template>

            </div>

        </div>
        <div class="col-lg-9 col"> <!-- правая колонка, меняется -->

              <router-view :key="$route.fullPath"></router-view>

        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Programmes from '../components/Programmes';
import ProgramInfo from '../components/program/ProgramInfo';
import Login from '../components/Login.vue';
import axios from "axios";
import UsefulLinks from "./UsefulLinks";
import variables from "./variables";

export default {
  //name: 'App',
  components: {
    Login,
    Programmes,
    ProgramInfo,
    UsefulLinks
  },
  data() {
    return {
      state: 'list',
      progName: null,
      user: {
        "is_authenticated": false,
        "email": "",
        "first_name": "",
        "last_name": "",
        "is_admin": false
      },
      searchInput: '',
    }
  },
  created() {
    this.getUser()
  },
  methods: {
    getUser() {
      axios.get(variables.url + '/api/user/')
        .then(response => {
          this.user = response.data
          variables.user = response.data
        })
        .catch(error => {
          console.log(error);
        })
    },
    search(){
      this.searchInput = this.searchInput.trim()
      if (this.searchInput !== '') {
        this.$router.push('/search/?q=' + this.searchInput)
      }
    }
  }
}
</script>

<style>

h1, h2 {
  font-weight: normal;
}

.my-sticky-top{
  position: sticky;
  left: 0;
  top: 7em;
}

</style>
