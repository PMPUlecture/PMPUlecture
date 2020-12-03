<template>
  <div>
    <div class="card bg-light mb-3">
      <div class="card-header"> Вопросы </div>
      <div class="card-body">
        <!-- <h5 class="card-title">Light card title</h5> -->
        <!-- <p class="card-text"> {{this.sources}} </p> -->
        <MaterialLink v-for="source in this.sources" :source="source"></MaterialLink>
      </div>
    </div>
  </div>
</template>

<script>
import MaterialLink from "./MaterialLink";
export default {
  name: "Questions",
  components: {MaterialLink},
  props: {
    sources: {
      type: Object,
      required: true
    },
  }
}
</script>

<style scoped>

</style>
