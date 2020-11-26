<template>

  <div>

    <div class="container-fluid">
      <div class="row">
        <div class="col-3 ">
          <img :src="lecturerInfo.photo" alt="фото" class="w-100">
        </div>
        <div class="col-7 ">
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

    <Materials
      :subjectID="this.subjID"
      :lecturerID="this.lecturerID"
    />

  </div>

</template>

<script>

import axios from "axios";
import Materials from "./Materials"

export default {
  name: "LecturerPage",
  props: ['lecturerID',],
  //props: {
  //  lecturerID: Number,
  //  currentsubject1: Number,
  //},
  components: {
    Materials,
  },
  data() {
    return {
      lecturerInfo: null,
      subjID: this.$route.query.subjectID,
    }
  },
  created() {
    console.log(this.currentsubject1)
    this.getLecturerInfo(this.lecturerID)
  },
  methods: {
    getLecturerInfo(lecturerID) {
      axios.get('/api/lecturers/', {
        params: {
          id: lecturerID,
          fields: 'apmath,photo,vk'
        }
      })
        .then(response => {
          this.lecturerInfo = response.data[0]
          document.title = 'ПМ-ПУ | ' + this.lecturerInfo.name
        })
        .catch(error => {
          console.log(error);
        })
    },
  }
}

</script>

<style>
img {
  border: 2px solid black;
}
</style>
