<template>
  <div class="text-center m-auto d-flex align-content-between flex-column center card bg-light">
    <h2 class="p-4 card-header">Вход</h2>

    <div class="card-header bg-danger" role="alert" v-if="$route.query.error === '1'">
      Неправильный логин или пароль!
    </div>
    <div class="alert alert-danger" role="alert" style="background-color: #ed7669" v-if="$route.query.error === '2'">
      Используйте аккаунт СПбГУ.
    </div>

    <div class="text-left card-body">
      <form action="/account/login/" method="post">
        <div class="form-group row">
          <input type="hidden" name="csrfmiddlewaretoken" :value=getCSRF>
          <label class="col-sm-2 col-form-label">Email:</label>
          <div class="col-sm-10">
            <input type="email" class="form-control" id="InputEmail" name="email" aria-describedby="emailHelp"readonly>
            <small id="emailHelp" class="form-text text-muted">Используйте ваш st******@student.spbu.ru</small>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-sm-2">Пароль:</label>
          <div class="col-sm-10">
            <input type="password" class="form-control" name="password" id="InputPassword"readonly>
          </div>
        </div>
        <div class="d-flex justify-content-between">
            <button type="submit" class="btn btn-primary">Войти</button>
            <a class="btn btn-danger" href="/account/login/google-oauth2/">Войти через Google</a>
        </div>
      </form>
    </div>
  </div>
</template>
</template>

<script>
export default {
  name: "Login",
  computed: {
    getCSRF: function () {
      console.log(this.$cookies)
      if (this.$cookies.isKey('csrftoken')) {
        return this.$cookies.get('csrftoken')
      } else {
        return 'no token'
      }
    }
  },
  created() {
    document.title = 'ПМ-ПУ | Вход';
  }
}
</script>

<style scoped>
.center{
  max-width: 50em;
}
</style>
