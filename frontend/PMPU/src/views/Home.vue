<template>
 <!-- id="app" не нужен -->
    <!-- Image and text -->
    <div class="container-fluid">
      <div class="row vh-100">
        <div class="col-3">  <!-- левая колонка со ссылками, не меняется -->

          <div class="card h-75 sticky-top">
            <div class="card-body d-flex flex-column justify-content-between">

              <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action" href="https://vk.com/pmpu_news">ПМ-ПУ СМИ</a>
                <a class="list-group-item list-group-item-action" href="https://vk.com/sspmpu">Студсовет ПМ-ПУ</a>
                <a class="list-group-item list-group-item-action" href="#">Студсовет2 ПМ-ПУ</a>
              </div>

              <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action" href="#">1</a>
                <a class="list-group-item list-group-item-action" href="#">2</a>
              </div>

            </div>
          </div>

        </div>
        <div class="col"> <!-- правая колонка, меняется -->

          <div class="card h-100">
            <div class="card-body">

              <Login />

            </div>
          </div>

        </div>
      </div>
    </div>

</template>

<script>
import Login from '../components/Login.vue';

export default {
  //name: 'App',
  components: {
    Login,
  },
  data() {

  },
}
</script>

<style>

</style>
