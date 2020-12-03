<template>
    <a target="_blank" :href="source.link" class="d-flex">
      <p class="mr-auto">{{source.name}}</p>
      <p class="align-self-end ml-3 text-muted" >{{source.year_of_relevance}}</p>
    </a>
</template>

<script>
export default {
  name: "MaterialLink",
  props: ['source', ],

}
</script>

<style scoped>

</style>
