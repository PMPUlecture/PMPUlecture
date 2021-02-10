<template>
  <div id="app" class="d-flex flex-column justify-content-between vh-100">

    <Home class=" flex-grow-1"/>
    <footer class="pt-3 pb-3 mt-3" style="background-color: #598bab;">
      <div class="container">
        <div class="row" id="footer">
          <router-link to="/about" class="col-lg row-cols-1 text-center">О нас</router-link>
          <a href="https://github.com/PMPUlecture/PMPUlecture/blob/for_deploy/README.md" class="col-lg row-cols-1 text-center" target="_blank">API</a>
          <router-link to="/funding" class="col-lg row-cols-1 text-center">Пожертвовать</router-link>
        </div>
        <div class="row d-flex justify-content-center">
          <p class="h5 col-lg row-cols-lg-1" style="max-width: max-content">По всем вопросам писать на почту</p>
          <div class="rounded bg-primary p-1 pl-2 pr-2 text-white col-lg row-cols-lg-1" style="font-size: medium; max-width: max-content">
            pmpulecture@bk.ru
          </div>
        </div>
      </div>
    </footer>

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
