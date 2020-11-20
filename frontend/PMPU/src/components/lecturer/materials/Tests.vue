<template>
  <div>
    <div class="card bg-light mb-3">
      <div class="card-header"> Контрольные </div>
      <div class="card-body">
        <!-- <h5 class="card-title">Light card title</h5> -->
        <!-- <p class="card-text"> {{this.sources}} </p> -->
        <div v-for="source in this.sources">
          <a :href="source.link" > {{source.name}} </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Tests",
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
