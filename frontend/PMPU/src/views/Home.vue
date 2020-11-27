<template>
 <!-- id="app" не нужен -->
    <!-- Image and text -->

    <div class="container-fluid min-vh-100">
      <div class="row bg-primary text-white mb-5">
        <div class="col m-2">
          <a class="stretched-link text-white nostroke" href="/"><h1 class="text-center display-5">БАЗА знаний ПМ-ПУ</h1></a>
        </div>
      </div>
      <div class="row">
        <div class="col-3">  <!-- левая колонка со ссылками, не меняется -->

            <div class="d-flex flex-column justify-content-between sticky-top">
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
                      <router-link :to="'/add_materials'" >
                        <button class="btn btn-outline-primary" > Добавить </button>
                      </router-link>
                  </div>
                  </div>
                </template>
                <template v-else>
                  <div class="card text-white bg-warning mt-3 mb-3">
                  <div class="card-body">
                    <h4 class="card-title">Вход не выполнен</h4>
                    <p class="card-text">Вы не вошли на сайт. Вы можете просматривать метериалы, но чтобы добавить свои
                    необходимо войти.</p>

                  </div>
                  </div>
                </template>

              <div class="card list-group-item-success">
                <div class="card-body">
                  <div class="list-group list-group-flush ">
                    <a href="/account/logout/" class="list-group-item-success list-group-item list-group-item-action"
                       v-if="user.is_authenticated" v-on:click="logout()">Выйти</a>
                    <router-link to="/login" class="list-group-item-success list-group-item list-group-item-action" v-else>Вход</router-link>
                    <router-link to="/" class="list-group-item-success list-group-item list-group-item-action">Домой</router-link>
                  </div>
                </div>
              </div>

            </div>

        </div>
        <div class="col-9"> <!-- правая колонка, меняется -->

              <router-view></router-view>

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
        "is_authenticated": true, //false
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
      axios.get('http://pmpulecture.herokuapp.com/api/userш/')
        .then(response => {
          this.user = response.data
        })
        .catch(error => {
          console.log(error);
        })
    },
    logout() {
      axios.get('http://pmpulecture.herokuapp.com/accout/logout/')
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

</style>
