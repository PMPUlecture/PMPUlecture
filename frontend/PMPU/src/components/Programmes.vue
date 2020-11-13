<template>
  <div>
      <h3 class="display-3 text-center text-white"><span class="badge badge-pill badge-light">Бакалавриат</span></h3>

      <div class="w-auto  p-1"></div>

    <ProgrammeCard v-for="programme in progList.bachelor"
                    v-bind:programme="programme"
                   @show-prog="changeView"
    />   <!-- v-bind:programme="programme" - передача параметров -->

    <h3 class="display-3 text-center text-white"><span class="badge badge-pill badge-light">Магистратура</span></h3>

    <ProgrammeCard v-for="programme in progList.master"
                   v-bind:programme="programme"
                   @show-prog="changeView"
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
    }
  },
  created() {
    this.getProgList()
  },
  methods: {
    getProgList() {
      axios.get('https://pmpulecture.herokuapp.com/api/programmes/')
        .then(response => {
          this.progList = response.data
        })
        .catch(error => {
          console.log(error);
        })
    },
    changeView(progName) {
      console.log('changeView()')
      this.$emit('show-prog',progName)
    }
  }
}

</script>

<style>

</style>

