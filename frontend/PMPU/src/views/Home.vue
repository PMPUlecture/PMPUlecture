<template>
  <div>
    <!-- Верхняя панель -->
    <header>
  <div class="container mb-5">
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top mb-5">
      <router-link class="navbar-brand" to="/"><b>База знаний ПМ-ПУ</b></router-link>

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
          <span class="m-auto">Вход не выполнен</span>
          <a class="btn btn-danger" href="/account/login/google-oauth2/"><i class='fab fa-google'></i></a>
        </div>
      </div>

      <br>
      <!-- Полезные ссылки -->
      <div class="list-group d-lg-none d-block">
        <a class="list-group-item list-group-item-action" target="blank"  href="https://vk.com/pmpu_news">ПМ-ПУ СМИ</a>
        <a class="list-group-item list-group-item-action" target="blank"href="https://vk.com/sspmpu">Студсовет ПМ-ПУ</a>
        <a class="list-group-item list-group-item-action" target="blank"href="#">Студсовет2 ПМ-ПУ</a>
      </div>
      <!-- Поиск преподов -->
      <!--form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form-->
    </div>
  </nav>
  </div>
    </header>

    <div class="container-fluid min-vh-100">
      <div class="row mb-5"></div>

      <!--div class="row bg-primary text-white mb-5">
        <div class="col m-2">
          <router-link class="stretched-link text-white nostroke " to="/"><h1 class="text-center display-5">БАЗА знаний ПМ-ПУ</h1></router-link>
        </div>
      </div-->
      <div class="row">
        <div class="col-3 d-none d-lg-block">  <!-- левая колонка со ссылками, не меняется -->

            <div class="d-flex flex-column justify-content-between my-sticky-top">
              <div class="card">
                <div class="card-body">
                <div class="list-group list-group-flush">
                  <a class="list-group-item list-group-item-action" target="blank"  href="https://vk.com/pmpu_news">ПМ-ПУ СМИ</a>
                  <a class="list-group-item list-group-item-action" target="blank"href="https://vk.com/sspmpu">Студсовет ПМ-ПУ</a>
                  <a class="list-group-item list-group-item-action" target="blank"href="#">Студсовет2 ПМ-ПУ</a>
                </div>
                </div>
              </div>


                <template v-if="user.is_authenticated">
                  <div class="card text-white bg-info mt-3 mb-3">
                    <h3 class="card-header text-center"><b>{{user.first_name}} {{user.last_name}}</b></h3>
                      <div class="card-body">
                        <h4 class="card-title">Добро пожаловать {{user.email}}</h4>
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

                <template v-else>
                  <div class="card text-white bg-warning mt-3 mb-3">
                  <div class="card-body">
                    <h4 class="card-title">Вход не выполнен</h4>
                    <p class="card-text">Вы не вошли на сайт. Вы можете просматривать метериалы, но чтобы добавить свои
                    необходимо войти.</p>
                    <a class="btn btn-danger" href="/account/login/google-oauth2/">Вход через Google</a>

                  </div>
                  </div>
                </template>

            </div>

        </div>
        <div class="col-lg-9 col"> <!-- правая колонка, меняется -->

              <router-view></router-view>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Programmes from '../components/Programmes';
import ProgramInfo from '../components/ProgramInfo';
import Login from '../components/Login.vue';
import axios from "axios";

export default {
  //name: 'App',
  components: {
    Login,
    Programmes,
    ProgramInfo
  },
  data() {
    return {
      state: 'list',
      progName: null,
      user: {
        "is_authenticated": true,
        "email": "ffff@sdsd",
        "first_name": "Kirill",
        "last_name": "Lisov"
      },
    }
  },
  created() {
    this.getUser()
  },
  methods: {
    getUser() {
      axios.get('/api/user/')
        .then(response => {
          this.user = response.data
        })
        .catch(error => {
          console.log(error);
        })
    },
    logout() {
      axios.get('/accout/logout/')
    },
  }
}
</script>

<style>

h1, h2 {
  font-weight: normal;
}

.nostroke:hover{
  text-decoration: none;
}

.my-sticky-top{
  position: sticky;
  left: 0;
  top: 7em;
}

</style>
