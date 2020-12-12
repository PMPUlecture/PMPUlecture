<template>
  <div id="app">

    <Home/>

  </div>
</template>

<script>

import Home from "./views/Home";

export default {
  name: 'app',
  data() {
    return {
      msg: 'База знаний ПМ-ПУ',
    }
  },
  components:{
    Home,
  }
}
</script>

<style>
#app {
/*  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;*/
  background-color: #B6D0E2;
}

h1, h2 {
  font-weight: normal;
}


a {
  color: #42b983;
}
</style>
