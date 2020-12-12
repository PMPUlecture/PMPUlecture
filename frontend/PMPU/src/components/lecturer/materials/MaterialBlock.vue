<template>
  <div class="card bg-light mb-3" >
    <div class="card-header"> {{ name }} </div>
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

</style>
