<template>
 <!-- id="app" не нужен -->
    <!-- Image and text -->
    <div class="container-fluid">
      <div class="row">
        <div class="col-3">  <!-- левая колонка со ссылками, не меняется -->

          <div class="card sticky-top">
            <div class="card-body d-flex flex-column justify-content-between">

              <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action" href="https://vk.com/pmpu_news">ПМ-ПУ СМИ</a>
                <a class="list-group-item list-group-item-action" href="https://vk.com/sspmpu">Студсовет ПМ-ПУ</a>
                <a class="list-group-item list-group-item-action" href="#">Студсовет2 ПМ-ПУ</a>
              </div>
              <div style="height: 200px"></div>

              <div class="list-group list-group-flush">
                <router-link to="/login" class="list-group-item list-group-item-action">Перейти к Login</router-link>
                <router-link to="/" class="list-group-item list-group-item-action">Перейти к Home</router-link>
              </div>

            </div>
          </div>

        </div>
        <div class="col"> <!-- правая колонка, меняется -->

          <div class="card">
            <div class="card-body">

              <router-view></router-view>

            </div>
          </div>

        </div>
      </div>
    </div>

</template>

<script>
import Programmes from "../components/Programmes";
import Login from '../components/Login.vue';

export default {
  //name: 'App',
  components: {
    Login,
    Programmes,
  },
  data() {

  },
}
</script>

<style>

</style>
