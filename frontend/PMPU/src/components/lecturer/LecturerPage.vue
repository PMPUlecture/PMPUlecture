<template>

  <div>
      <Loader v-if="loading"></Loader>
    <div v-if="!loading" class="container-fluid">
      <div class="row">
        <div class="col-3 d-lg-block d-none">
          <img :src="lecturerInfo.photo" alt="фото" class="w-100">
        </div>
        <div class="col-lg-7 col">
          <h2 class="text-center"> {{lecturerInfo.name}} </h2>

          <div class="list-group">
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
      lecturerInfo: {photo: null, name: null, apmath: null, vk_discuss_url: null},
      subjectID: this.$route.query.subjectID,
      loading: true,
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
    getLecturerInfo(lecturerID) {
      axios.get('/api/lecturers/', {
        params: {
          id: lecturerID,
          fields: 'apmath,photo,vk,materials',
          id_subject_for_material: this.subjectID,
        }
      })
        .then(response => {
          this.lecturerInfo = response.data[0]
          document.title = 'ПМ-ПУ | ' + this.lecturerInfo.name
          console.log(this.lecturerInfo.materials)
          this.loading = false;
        })
        .catch(error => {
          console.log(error);
        })
    },
    getMaterials() {
      axios.get('/api/lecturers/', {
        params: {
          id: this.lecturerID,
          fields: 'materials'
        }
      })
        .then(response => {
          this.lecturerInfo.materials = response.data[0].materials
          document.getElementById("getAll").className += " invisible";
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
</style>
