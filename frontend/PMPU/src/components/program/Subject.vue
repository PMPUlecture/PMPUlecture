<template>
  <div>

    <div class="accordion" id="accordionExample1">
      <div class="card">
        <div class="card-header bg-secondary" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link collapse-header" type="button" data-toggle="collapse" :data-target="subjectidsharp" aria-expanded="true" >
              {{subjectInfo.name}}
            </button>
          </h5>
        </div>

        <div :id="subjectid" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample1">
          <div class="card-body">

            <Lecturer v-for="lecturer in subjectInfo.lecturers"
                     :lecturerInfo="lecturer"
            />

          </div>
        </div>
      </div>


    </div>

  </div>
</template>

<script>

import Lecturer from '../program/Lecturer';

export default {
  name: "Subject",
  props: {
    subjectInfo: {
      type: Object,
      required: true
    }
  },
  components: {
    Lecturer,
  },
  data() {
    return {
      subjectidsharp: '#subject'+this.subjectInfo.id,
      subjectid: 'subject'+this.subjectInfo.id,
    }
  }
}
</script>

<style scoped>
.collapse-header {
  position: relative;
  right: 45%;
  color: black;
}
</style>
