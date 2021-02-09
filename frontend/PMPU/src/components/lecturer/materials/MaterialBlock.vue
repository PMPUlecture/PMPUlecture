<template>
  <div class="card bg-light mb-3" >
    <div class="card-header d-flex">
      <span>{{ name }}</span>
      <a class="ml-auto cursor-pointer text-dark mr-2" @click="$emit('add', {'subject': '', 'type': ''})"><i class="fas fa-plus"></i></a>
    </div>
    <div class="card-body">
      <MaterialLink v-for="source in this.sources" :source="source" v-on:remove="$emit('remove', $event)"
                    v-on:edit="$emit('edit', $event)"></MaterialLink>
    </div>
  </div>
</template>

<script>
import MaterialLink from "./MaterialLink";
export default {
name: "MaterialBlock",
  components: {MaterialLink},
  props: ['name', 'sources'],
  comments: {
    MaterialLink
  }
}
</script>

<style scoped>
.cursor-pointer{
  cursor: pointer;
}
</style>
