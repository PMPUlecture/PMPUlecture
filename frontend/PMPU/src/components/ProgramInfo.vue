<template>

  <div>
    <p class="progname">{{ progInfo.name }}</p>
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

export default {
  name: "ProgramInfo",
  props: ['progID',]
  ,
  components: {
    Term,
  },
  data() {
    return {
      progInfo: null,
    }
  },
  created() {
    this.getProgInfo(this.progID)
  },
  methods: {
    getProgInfo(progID) {
      axios.get('/api/programmes/'+progID)
        .then(response => {
          this.progInfo = response.data
          console.log(this.progInfo)
        })
        .catch(error => {
          console.log(error);
        })
      this.progInfo = "nonnono";
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
</style>
