<template>
  <div>
    <div class=" d-flex">
      <a target="_blank" :href="src.link" class="d-inline-flex justify-content-between flex-grow-1">
        <p class="m-0 mr-auto text-wrap">{{src.name}}</p>
        <p class="m-0 ml-3 text-muted" >{{src.year_of_relevance}}</p>
      </a>
      <a v-if="source.is_author" class="m-0 ml-2 text-danger text-decoration-none delete" v-on:click="testing">
        <i class="fas fa-times"></i>
      </a>
    </div>

  </div>
</template>

<script>
export default {
  name: "MaterialLink",
  props: ['source', ],
  data(){
    return {
      src:{
        id: '',
        name: '',
        year_of_relevance: '',
        link: '',
        is_author: ''
      }
    }
  },
  created() {
    this.src = this.source
  },
  methods:{
    testing: function (){
      console.log(this.source.id)
      this.$emit('remove', {id: this.source.id, name: this.source.name})
    },


  }

}
</script>

<style scoped>
.delete:hover{
  cursor:pointer;
}
</style>
