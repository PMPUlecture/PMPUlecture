<template>
  <form action="" method="post">
    <input type="hidden" name="csrfmiddlewaretoken" :value=getCSRF>
    <h4 class="text-monospace">Enter the username:</h4>
    <input class="form-control mr-sm-2" type="email" name="email" size=50>
    <br>
    <h4 class="text-monospace">Enter the password:</h4>
    <input class="form-control mr-sm-2" type="password" name="password" size=50>
    <br>
    <br>
    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Log in</button>
  </form>
</template>

<script>
export default {
name: "Login",
  computed:{
  getCSRF: function (){
    console.log(this.$cookies)
    if (this.$cookies.isKey('csrftoken')){
      return this.$cookies.get('csrftoken')
   }
    else{
      return 'no token'
    }
  }
  }
}
</script>

<style scoped>

</style>
