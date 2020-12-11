<template>
  <div>
    <!-- MODAL -->
    <div class="modal fade" :id="'ModalFor'+src.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-sm">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Удалить материал {{src.name}}?</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Нет</button>
            <button type="button" class="btn btn-danger" v-on:click="deleteMaterial">Да</button>
          </div>
        </div>
      </div>
    </div>


    <div class=" d-flex">
      <a target="_blank" :href="src.link" class="d-inline-flex justify-content-between flex-grow-1">
        <p class="m-0 mr-auto text-wrap">{{src.name}}</p>
        <p class="m-0 ml-3 text-muted" >{{src.year_of_relevance}}</p>
      </a>
      <a v-if="src.is_author" class="m-0 ml-2 text-danger text-decoration-none" v-on:click="openModal(src.id)" >&times;</a>
    </div>

  </div>
</template>

<script>
import axios from "axios";
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
    openModal(){
      $('#ModalFor'+this.src.id).modal('show')
    },

    deleteMaterial() {
      axios.delete('http://127.0.0.1:8000/api/material/', {
        data:{
          id: this.src.id
        }
      })
      .then((response) =>
      {
        if (response.data.status === 'ok'){
          this.src = null
        }
        $('#myModal').modal('hide')
      })
    }
  }

}
</script>

<style scoped>

</style>
