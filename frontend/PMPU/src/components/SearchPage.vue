<template>
  <div class="container-fluid">

    <h3 v-if="!lecturers.length">По вашему запросу ничего не найдено</h3>
    <template v-for="lecturer in lecturers">
      <div class="card mb-3">
        <div class="d-flex no-gutters">
          <div class=" d-md-block d-none">
            <img :src="lecturer.photo" class="card-img" alt="photo" style="height: 200px; width: auto">
          </div>
            <div class="card-body container-fluid">
              <h4 class="card-title row-cols-1">{{lecturer.name}}</h4>
              <div class="d-flex justify-content-between">
                <div class="">

                  <p class="card-text">Предметы:</p>
                  <b>{{ get_subjects(lecturer.subjects) }}</b>
                </div>

                <div class="mr-4">
                <router-link class="btn btn-primary mt-auto stretched-link" :to="'/lecturer/'+lecturer.id">Перейти</router-link>
                </div>

              </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import axios from "axios";
import variables from "../views/variables";
export default {
name: "SearchPage",
  data() {
    return {
      lecturers: [],
    }
  },

 mounted: function (){
  this.get_lecturers()
  },
  methods: {
    get_subjects(ar){
      let out = ar[0].name
      for (let i =1; i < ar.length; i++){
        out += ', ' + ar[i].name
      }
      return out;
    },

    get_lecturers(){
      if (this.$route.query.q){
        console.log(this.$route.query.q)
        axios.get(variables.url + '/api/lecturers/', {
          params:{
            name: this.$route.query.q,
            fields: 'photo,subjects,apmath'
          }
        })
        .then((response) => {
          this.lecturers = response.data
        })
      }

    }
  }
}
</script>

<style scoped>

</style>
