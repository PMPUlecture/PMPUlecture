<template>
  <div style="text-align: left">
    <div class="alert alert-danger" role="alert" v-if="$route.query.error === '1'">
      Неправильный логин или пароль!
    </div>
    <form action="http://127.0.0.1:8000/account/login/" method="post">
      <div class="form-group row">
        <input type="hidden" name="csrfmiddlewaretoken" :value=getCSRF>
        <label class="col-sm-2 col-form-label">Email:</label>
        <div class="col-sm-7">
          <input type="email" class="form-control" id="InputEmail" name="email" aria-describedby="emailHelp">
          <small id="emailHelp" class="form-text text-muted">Используйте ваш st******@student.spbu.ru</small>
        </div>
      </div>
      <div class="form-group row">
        <label class="col-sm-2">Пароль:</label>
        <div class="col-sm-7">
        <input type="password" class="form-control" name="password" id="InputPassword">
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
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
  }
}
</script>

<style scoped>

</style>
