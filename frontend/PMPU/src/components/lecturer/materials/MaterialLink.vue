<template>
  <div>
    <div class=" d-flex">
      <a target="_blank" :href="source.link" class="d-inline-flex justify-content-between flex-grow-1">
        <p class="m-0 mr-auto text-wrap">{{source.name}} <i v-if="source.only_authorized_users" class="fas fa-crown ml-1 text-warning" title="Этот материал виден только студентам"></i></p>
        <p class="m-0 ml-3 text-muted" >{{source.year_of_relevance}}</p>
      </a>
      <div v-if="source.is_author" class="m-0 ml-2">
        <a class="text-warning text-decoration-none delete" v-on:click="edit">
          <i class="fas fa-pen"></i>
        </a>
        <a class="text-danger text-decoration-none delete" v-on:click="remove">
          <i class="fas fa-times"></i>
        </a>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "MaterialLink",
  props: ['source', ],

  methods:{
    edit: function (){
      let event = {
        id: this.source.id,
        name: this.source.name,
        link: this.source.link,
        year_of_relevance: this.source.year_of_relevance,
        type: '',
        only_authorized_users: this.source.only_authorized_users,
      }
      this.$emit('edit', event)
    },
    remove: function (){
      this.$emit('remove', this.source)
    },


  }

}
</script>

<style scoped>
.delete:hover{
  cursor:pointer;
}
</style>
