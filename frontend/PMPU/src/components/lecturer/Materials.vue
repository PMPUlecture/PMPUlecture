<template>
  <div>

  <h2 class="text-center"> {{materials.name}} </h2>

  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <Abstracts :sources="materials.source[0].abstract" />
      </div>
      <div class="col">
        <Questions :sources="materials.source[0].questions" />
      </div>
      <div class="col">
        <Tests :sources="materials.source[0].test" />
      </div>
      <div class="col">
        <Other :sources="materials.source[0].other" />
      </div>
    </div>
  </div>

  </div>
</template>

<script>

import Abstracts from "./materials/Abstracts";
import Questions from "./materials/Questions";
import Tests from "./materials/Tests";
import Other from "./materials/Other";
import axios from "axios";

export default {
  name: "Materials",
  components: {
    Abstracts,
    Questions,
    Tests,
    Other
  },
  props: ['lecturerID','subjectID'],
  data () {
    return {
      materials: null
    }
  },
  created() {
    this.getMaterials(this.subjectID)
  },
  methods: {
    getMaterials(subjectID) {
      axios.get('http://pmpulecture.herokuapp.com/api/lecturers/', {
        params: {
          id: this.lecturerID,
          id_subject_for_material: this.subjectID,
          fields: 'materials'
        }
      })
        .then(response => {
          this.materials = response.data[0].materials[0]
        })
        .catch(error => {
          console.log(error);
        })
    }
  }
}
</script>

<style scoped>

</style>
