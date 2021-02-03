<template>
  <div class="bg-white rounded p-5">
    <h2>Пожертвования</h2>
      <p>Спасибо, что заинтересовалсь поддержкой проекта. На этой странице вы найдете реквизиты для доната.</p>
    <div class="container">
      <div class="row">
        <div class="col-3">
          <h5>QIWI</h5>
          <p>Перевод с <a target="_blank" href="https://my.qiwi.com/Kyryll-LjbVlZwU0P">карты банка</a></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
name: "Funding",
  methods:{
  copy(){
    navigator.clipboard.writeText($('#nick')[0].textContent)
      .then(() => {
        alert("copied")
      })
      .catch(err => {
        console.log('Something went wrong', err);
      });

  }
  }
}
</script>

<style scoped>

</style>
