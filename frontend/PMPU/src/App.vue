<template>
  <div id="app">
    <h1 class="header-text">{{ msg }}</h1>
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
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  //margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.header-text {
  position: relative;
  top: 50%;
  font-size: 700%;
  font-family: fantasy;
  color: teal;
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: black;
  text-shadow: black 0 0 20px;;
}
</style>
