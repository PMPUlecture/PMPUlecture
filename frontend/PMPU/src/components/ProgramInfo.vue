<template>
  <div>
    <p class="progname">{{progName}}</p>

    <Term v-for="term in progInfo"
          :termInfo="term"
    />

  </div>
</template>

<script>

import axios from "axios";
import Term from '../components/program/Term';

export default {
  props: {
    progName: {
      type: String,
      required: true
    }
  },
  components: {
    Term,
  },
  data() {
    return {
      progInfo: null,
    }
  },
  created() {
    this.getProgInfo(this.progName)
    console.log('progName: '+this.progName)
  },
  methods: {
    getProgInfo(progName) {
      axios.get('https://pmpulecture.herokuapp.com/api/struct/?programme='+progName)
        .then(response => {
          this.progInfo = response.data
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
  //text-shadow: #000 3px 3px 5px;

  position: relative;
  font-size: 250%;
  color: cornflowerblue;

  font-family: fantasy;
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: black;

}
</style>
