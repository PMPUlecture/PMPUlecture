<template>
  <div class="card bg-light">
    <div class="card-header">
      <a class="stretched-link text-primary" data-toggle="collapse" :href="'#collapseS'+this.subjectInfo.id" :aria-controls="'collapseS'+this.subjectInfo.id">
        {{ this.subjectInfo.name }}
      </a>
    </div>

    <div :id="'collapseS'+this.subjectInfo.id" class="collapse" :data-parent="'#collapseTerm'+this.termInfo">
        <div class="list-group card-body pl-4">
          <Lecturer v-for="lecturer in this.subjectInfo.lecturers"
                    :lecturerInfo="lecturer"
                    :currentsubject="subjectInfo.id"
          />

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
    },
    termInfo:{

    }
  },
  components: {
    Lecturer,
  },
}
</script>

<style scoped>
.collapse-header {
  position: relative;
  right: 45%;
  color: black;
}
</style>
