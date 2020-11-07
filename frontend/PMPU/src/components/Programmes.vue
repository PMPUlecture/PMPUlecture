<template>
  <div class="card text-white bg-secondary mb-3">
    <div class="card-header">
      <p class="degree-text">Бакалавриат</p>
    </div>

    <ProgrammeCard v-for="programme in progList.bachelor"
                    v-bind:programme="programme"/>

    <div class="card-header">
      <p class="degree-text">Магистратура</p>
    </div>

    <ProgrammeCard v-for="programme in progList.master"
                   v-bind:programme="programme"/>


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
    getProgInfo(progName) {
      axios.get('https://pmpulecture.herokuapp.com/api/struct/?programme='+progName)
        .then(response => {
          this.progInfo = response.data
        })
        .catch(error => {
          console.log(error);
        })
    }
  }
}

</script>

<style>
.program-text1 {
  position: relative;
  top: 30%;
  font-size: 500%;
  font-family: fantasy;
  text-shadow: red 2px 3px 30px;
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: red;
}
.program-text2 {
  position: relative;
  top: 30%;
  font-size: 500%;
  font-family: fantasy;
  text-shadow: blue 2px 3px 30px;
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: blue;
}
.degree-text {
  position: relative;
  top: 50%;
  font-size: 300%;
  font-family: fantasy;
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: black;
  text-shadow: black 0 0 20px;;
}
</style>

