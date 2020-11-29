<template>
  <div>
    <Loader v-if="loading"></Loader>
      <h2 v-if="progList.bachelor.length" class="display-4 text-center text-white"><span class="badge badge-pill badge-light">Бакалавриат</span></h2>

      <div class="w-auto  p-1"></div>

    <ProgrammeCard v-for="programme in progList.bachelor"
                    v-bind:programme="programme"
    />   <!-- v-bind:programme="programme" - передача параметров -->

    <h3 v-if="progList.master.length" class="display-3 text-center text-white"><span class="badge badge-pill badge-light">Магистратура</span></h3>

    <ProgrammeCard v-for="programme in progList.master"
                   v-bind:programme="programme"
    />
  </div>


</template>

<script>

import axios from "axios";
import ProgrammeCard from "./ProgrammeCard";
import Loader from "./Loader";
import Login from "./Login";

export default {
  //name: 'App',
  components: {
    Loader,
    Login,
    ProgrammeCard,
  },
  data() {
    return {
      progList: {bachelor: [{'name': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor', 'img_url': 'https://hsto.org/webt/59/e1/14/59e1140d498b7040864280.png', 'id': 1}], master: []},
      loading: true,
    }
  },
  mounted() {
    document.title = 'ПМ-ПУ';
    this.getProgList()
  },
  methods: {
    getProgList() {
      axios.get('/api/programmes/', {
        params: {
          fields: 'img_url'
        }
      })
        .then(response => {
            this.progList = response.data
            this.loading = false;
        })
        .catch(error => {
          console.log(error);
        })
    },
  }
}

</script>

<style>

</style>

