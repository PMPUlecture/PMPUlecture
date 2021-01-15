<template>
  <div id="app">

    <Home class="vh-100"/>

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


h1, h2 {
  font-weight: normal;
}


a {
  color: #42b983;
}
</style>
