<template>
  <div class="card bg-light">
      <a class="card-header text-primary" data-toggle="collapse" :href="'#collapseS'+this.subjectInfo.id" :aria-controls="'collapseS'+this.subjectInfo.id">
        {{ this.subjectInfo.name }}
      </a>

    <div :id="'collapseS'+this.subjectInfo.id" class="collapse" :data-parent="'#collapseTerm'+this.termInfo">
        <div class="list-group card-body pl-4">
          <div v-if="!subjectInfo.lecturers.length">
            <p>Ой! Похоже сюда ещё не добавили преподавателя и его материалы. </p>
            <p v-if="user.is_authenticated">Ты можешь добавить их <router-link class="text-danger" to="/add_materials">здесь</router-link></p>
            <p v-else>Ты можешь <a class="text-danger" href="/account/login/google-oauth2/">войти</a> на сайт, чтобы добавить их.</p>
          </div>
          <Lecturer v-for="lecturer in this.subjectInfo.lecturers"
                    :lecturerInfo="lecturer"
                    :currentSubject="subjectInfo.id"
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
    user:{
      type: Object
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
