<template>

  <div>
    <Loader v-if="loading"></Loader>
    <p class="progname">{{ progInfo.programme }} </p>
    <div class="accordion" id="programme">
      <Term v-for="term in progInfo.terms"
            :termInfo="term"
      />
    </div>
  </div>


</template>

<script>

import axios from "axios";
import Term from '../components/program/Term';
import Loader from "./Loader";

export default {
  name: "ProgramInfo",
  props: ['progID',]
  ,
  components: {
    Loader,
    Term,
  },
  data() {
    return {
      progInfo: {terms: [], programme: ''},
      loading: true
    }
  },
  created() {
    this.getProgInfo(this.progID);

  },
  methods: {
    getProgInfo(progID) {
      axios.get('https://pmpulecture.herokuapp.com/api/subjects/', {
        params: {
          programme: progID,
          fields: 'term,lecturers'
        }
      })
        .then(response => {
          this.progInfo = response.data
          console.log(this.progInfo)
          document.title = 'ПМ-ПУ | ' + this.progInfo.programme;
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
.progname {
  position: relative;
  font-size: 250%;
  color: cornflowerblue;

  font-family: fantasy;
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: black;

}

@media (max-width: 500px) {
  .progname {
    font-size: 150%;
    -webkit-text-stroke: revert;
    color: #1a252f;
    font-weight: bold;
  }
}
</style>
