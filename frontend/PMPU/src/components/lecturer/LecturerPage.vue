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

            <div class="custom-control custom-switch mt-3 ml-3">
              <input v-model="materialForEdit.only_authorized_users" type="checkbox" class="custom-control-input" id="field10" >
              <label class="custom-control-label" for="field10">Сделать материал видимым только для студентов</label>
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

    <!-- MODAL for add -->
    <div class="modal fade" id="modal_for_add_material" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Добавить материал</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">

            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text label" >Предмет</span>
              </div>
              <input type="text" class="form-control text-primary" :value="subjectNameForAdd" disabled>
            </div>

            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text label" >Лектор</span>
              </div>
              <input type="text" class="form-control text-primary" :value="lecturerInfo.name" disabled>
            </div>

            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text label">Название</span>
              </div>
              <input type="text" class="form-control text-primary" v-model="materialForAdd.name">
            </div>

            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text label">Ссылка</span>
              </div>
              <input type="text" class="form-control text-primary" v-model="materialForAdd.link">
            </div>

            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text label">Год</span>
              </div>
              <input type="number" class="form-control text-primary" v-model="materialForAdd.year_of_relevance">
            </div>

            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text label">Тип</span>
              </div>
              <select class="form-control custom-select text-primary" disabled>
                <option value="abstract" :selected="materialForAdd.type === 'abstract'"> Конспект </option>
                <option value="questions" :selected="materialForAdd.type === 'questions'"> Вопросы </option>
                <option value="test" :selected="materialForAdd.type === 'test'"> Контрольная </option>
                <option value="other" :selected="materialForAdd.type === 'other'"> Другое </option>
              </select>
            </div>

            <div class="custom-control custom-switch mt-3 ml-3">
              <input v-model="materialForAdd.only_authorized_users" type="checkbox" class="custom-control-input" id="field">
              <label class="custom-control-label" for="field">Сделать материал видимым только для студентов</label>
            </div>

          </div>

          <div class="modal-footer d-flex justify-content-end">
            <button type="button" class="btn btn-light" data-dismiss="modal">Отмена</button>
            <button type="button" class="btn btn-success" v-on:click="addMaterial">Отправить</button>
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
           <template v-if="lecturerInfo.vk_discuss_url">
            <li class="list-group-item list-group-item-primary">Обсуждение и отзывы в группе ВК</li>
            <a :href="lecturerInfo.vk_discuss_url" target="blank" class="list-group-item list-group-item-action"> {{ lecturerInfo.vk_discuss_url }} </a>
           </template>
          </div>

        </div>
      </div>
    </div>

    <div v-if="!loading" class="container-fluid">
      <Materials
        v-for="material in lecturerInfo.materials"
        :material="material"
        :subjectID="subjectID"
        :lecturerID="lecturerID"
        v-on:remove="openModalDelete($event)"
        v-on:edit="openModelEdit($event)"
        v-on:add="openModalAdd($event)"
      />
      <div class="row">
        <button v-if="lecturerInfo.the_rest_of_materials" id="getAll" class="btn btn-outline-primary m-2 mt-5 col" v-on:click="getMaterials">Показать все материалы</button>
      </div>
    </div>


  </div>

</template>

<script>

import axios from "axios";
import Materials from "./Materials"
import Loader from "../Loader";
import variables from "../../views/variables";
import Term from "../program/Term";

export default {
  name: "LecturerPage",
  props: ['lecturerID',],
  components: {
    Term,
    Loader,
    Materials,
  },
  data() {
    return {
      lecturerInfo: {photo: null, name: null, apmath: null, vk_discuss_url: null, the_rest_of_materials: 0},
      subjectID: this.$route.query.subjectID,
      loading: true,
      materialForEdit:{
        id: '',
        name: '',
        link: '',
        type: '',
        only_authorized_users: ''
      },
      materialForAdd: {
        lecturer: '',
        subject: '',
        name: '',
        type: '',
        link: '',
        year_of_relevance: new Date().getFullYear(),
        only_authorized_users: false
      },
      subjectNameForAdd: '',
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
    openModalAdd(data){
      this.materialForAdd.subject = data.subject
      this.materialForAdd.type = data.type
      this.materialForAdd.lecturer = this.lecturerInfo.id
      this.subjectNameForAdd = data.subject_name
      $('#modal_for_add_material').modal('show')
    },

    deleteMaterial() {
      axios.delete(variables.url + '/api/material/', {
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
      axios.put(variables.url + '/api/material/', this.materialForEdit
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
    addMaterial(){
      axios.post(variables.url + '/api/material/', this.materialForAdd
      )
        .then((response) => {
          if (response.data.status === 'ok'){
            this.getLecturerInfo(this.lecturerID)
            $('#modal_for_add_material').modal('hide')
          }
          else{
            alert(response.data.error)
          }
        })
    },
    getLecturerInfo(lecturerID) {
      axios.get(variables.url + '/api/lecturers/', {
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
          //document.getElementById("getAll").classList.remove('invisible')
        })
        .catch(error => {
          console.log(error);
        })
    },
    getMaterials() {
      axios.get(variables.url + '/api/lecturers/', {
        params: {
          id: this.lecturerID,
          fields: 'materials'
        }
      })
        .then(response => {
          this.lecturerInfo.materials = response.data[0].materials
          this.lecturerInfo.the_rest_of_materials = response.data[0].the_rest_of_materials
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
