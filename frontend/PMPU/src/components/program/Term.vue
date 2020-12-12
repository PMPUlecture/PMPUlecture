<template>
  <div class="card">
      <a class="card-header text-primary" data-toggle="collapse" :href="'#collapse'+this.termInfo.term" :aria-controls="'collapse'+this.termInfo.term">
        {{ this.termInfo.term }} семестр
      </a>

    <div :id="'collapse'+this.termInfo.term" class="collapse" data-parent="#programme">
      <div class="card-body">
        <div class="accordion" :id="'collapseTerm'+this.termInfo.term">
          <Subject v-for="subject in this.termInfo.subjects"
                     :subjectInfo="subject" :termInfo="termInfo.term"
                   :user="user"
            />
        </div>
      </div>
    </div>
  </div>

</template>

<script>

import Subject from '../program/Subject';

export default {
  name: "Term",
  props: {
    termInfo: {
      type: Object,
      required: true
    },
    user:{
      type: Object
    }
  },
  components: {
    Subject,
  },
  data() {
    return {
      termidsharp: '#term'+this.termInfo.term,
      termid: 'term'+this.termInfo.term,
    }
  },
  created() {
    console.log(this.termInfo.term)
  }
}
</script>

<style scoped>
.collapse-header {
  position: relative;
  right: 45%;
}
</style>
