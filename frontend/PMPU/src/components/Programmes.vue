<template>
  <div>
      <h3 v-if="progList.bachelor.length" class="display-3 text-center text-white"><span class="badge badge-pill badge-light">Бакалавриат</span></h3>

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

export default {
  //name: 'App',
  components: {
    ProgrammeCard,
  },
  data() {
    return {
      progList: null,
      progInfo: null,
      loading: true,
    }
  },
  created() {
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
          document.title = 'ПМ-ПУ';
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

