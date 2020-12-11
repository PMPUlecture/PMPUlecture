<template>

  <div>
    <!-- MODAL for delete -->
    <div class="modal fade" id="modal_for_material" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-sm">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Удалить материал {{ materialForEdit.name }}</h5>
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


    <!-- MODAL for edit -->
    <div class="modal fade" id="modal_for_edit_material" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Редактировать материал {{ materialForEdit.name }}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text label" >Название</span>
              </div>
              <input type="text" class="form-control text-primary" v-model="materialForEdit.name">
            </div>
            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text label">Ссылка</span>
              </div>
              <input type="text" class="form-control text-primary" v-model="materialForEdit.link">
            </div>
            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text label">Год</span>
              </div>
              <input type="number" class="form-control text-primary" v-model="materialForEdit.year_of_relevance">
            </div>
            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text label">Тип</span>
              </div>
              <select v-model="materialForEdit.type" class="form-control text-primary">
                <option value="abstract"> Конспект </option>
                <option value="questions"> Вопросы </option>
                <option value="test"> Контрольная </option>
                <option value="other"> Другое </option>
              </select>
            </div>

          </div>

          <div class="modal-footer d-flex justify-content-end">
            <button type="button" class="btn btn-danger mr-auto" v-on:click="deleteMaterial">Удалить</button>
            <button type="button" class="btn btn-light" data-dismiss="modal">Отмена</button>
            <button type="button" class="btn btn-success" v-on:click="editMaterial">Применить</button>
          </div>
        </div>
      </div>
    </div>


      <Loader v-if="loading"></Loader>
    <div v-if="!loading" class="container-fluid">
      <h2 class="row-cols-lg-1 d-block d-lg-none">{{lecturerInfo.name}}</h2>
      <div class="row">
        <div class="col-lg-3 row-cols-lg-1">
          <img :src="lecturerInfo.photo" alt="фото" class="w-100" style="max-width: 500px">
        </div>
        <div class="col-lg-7 col">
          <h2 class="text-center d-none d-lg-block"> {{lecturerInfo.name}} </h2>

          <div class="list-group text-break">
            <li class="list-group-item list-group-item-primary">Страница преподавателя на сайте факультета</li>
            <a :href="lecturerInfo.apmath" target="blank" class="list-group-item list-group-item-action"> {{ lecturerInfo.apmath }} </a>
            <li class="list-group-item list-group-item-primary">Обсуждение и отзывы в группе ВК</li>
            <a :href="lecturerInfo.vk_discuss_url" target="blank" class="list-group-item list-group-item-action"> {{ lecturerInfo.vk_discuss_url }} </a>
          </div>

        </div>
      </div>
    </div>

    <div v-if="!loading" class="container-fluid">
      <Materials
        v-for="material in lecturerInfo.materials"
        :material="material"
        :subjectID="subjID"
        :lecturerID="lecturerID"
        v-on:remove="openModalDelete($event)"
        v-on:edit="openModelEdit($event)"
      />
      <div class="row">
        <button id="getAll" class="btn btn-outline-primary m-2 mt-5 col" v-on:click="getMaterials">Показать все материалы</button>
      </div>
    </div>


  </div>

</template>

<script>

import axios from "axios";
import Materials from "./Materials"
import Loader from "../Loader";

export default {
  name: "LecturerPage",
  props: ['lecturerID',],
  components: {
    Loader,
    Materials,
  },
  data() {
    return {
      url: '',
      lecturerInfo: {photo: null, name: null, apmath: null, vk_discuss_url: null},
      subjectID: this.$route.query.subjectID,
      loading: true,
      materialForEdit:{
        id: '',
        name: '',
        link: '',
        type: '',
      }
    }
  },
  created() {
    console.log(this.currentsubject1)
    this.getLecturerInfo(this.lecturerID)
  },
  beforeRouteUpdate (to, from, next) {
    console.log(to)
    this.getLecturerInfo(this.lecturerID);
  },
  methods: {
    openModalDelete(material){
      this.materialForEdit = material
      $('#modal_for_material').modal('show')
    },

    openModelEdit(material){
      this.materialForEdit = material
      $('#modal_for_edit_material').modal('show')
    },

    deleteMaterial() {
      axios.delete(this.url + '/api/material/', {
        data:{
          id: this.materialForEdit.id
        }
      })
        .then((response) =>
        {
          if (response.data.status === 'ok'){
            this.getLecturerInfo(this.lecturerID)
            $('.modal').modal('hide')
          }
          else{
            alert(response.data.error)
          }
        })
    },

    editMaterial(){
      axios.put(this.url + '/api/material/', this.materialForEdit
      )
      .then((response) => {
        if (response.data.status === 'ok'){
          this.getLecturerInfo(this.lecturerID)
          $('#modal_for_edit_material').modal('hide')
        }
        else{
          alert(response.data.error)
        }
      })
    },
    getLecturerInfo(lecturerID) {
      axios.get(this.url + '/api/lecturers/', {
        params: {
          id: lecturerID,
          fields: 'apmath,photo,vk,materials',
          id_subject_for_material: this.subjectID,
        }
      })
        .then(response => {
          this.lecturerInfo = response.data[0]
          document.title = 'ПМ-ПУ | ' + this.lecturerInfo.name
          this.loading = false;
          document.getElementById("getAll").classList.remove('invisible')
        })
        .catch(error => {
          console.log(error);
        })
    },
    getMaterials() {
      axios.get(this.url + '/api/lecturers/', {
        params: {
          id: this.lecturerID,
          fields: 'materials'
        }
      })
        .then(response => {
          this.lecturerInfo.materials = response.data[0].materials
          document.getElementById("getAll").classList.add('invisible');
        })
        .catch(error => {
          console.log(error);
        })
    }
  }
}

</script>

<style>
img {
  border: 2px solid black;
}

.label{
  width: 90px;
}

</style>
