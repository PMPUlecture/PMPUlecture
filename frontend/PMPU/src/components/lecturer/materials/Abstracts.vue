<template>
  <div>
    <div class="card bg-light mb-3" >
      <div class="card-header"> Конспекты </div>
      <div class="card-body">
        <!-- <h5 class="card-title">Light card title</h5> -->
        <!-- <p class="card-text"> {{this.sources}} </p> -->
        <MaterialLink v-for="source in this.sources" :source="source" v-on:remove="$emit('remove', $event)"
                  v-on:edit="add_type($event)"></MaterialLink>
      </div>
    </div>
  </div>
</template>

<script>
import MaterialLink from "./MaterialLink";
export default {
  name: "Abstracts",
  components: {MaterialLink},
  props: {
    sources: {
      type: Object,
      required: true
    }
  },
  methods: {
    add_type(event){
      event.type = 'abstract'
      this.$emit('edit', event)
    }
  }
}
</script>

<style scoped>

</style>
