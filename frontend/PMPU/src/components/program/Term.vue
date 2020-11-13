<template>
<div>

  <div class="accordion" id="accordionExample">
    <div class="card">
      <div class="card-header" id="headingOne">
        <h5 class="mb-0">
          <button class="btn btn-link collapse-header" type="button" data-toggle="collapse" :data-target="termidsharp" aria-expanded="true" >
            {{termInfo.term}} семестр
          </button>
        </h5>
      </div>

      <div :id="termid" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
        <div class="card-body">

          <Subject v-for="subject in termInfo.subjects"
                   :subjectInfo="subject"
          />

        </div>
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
  }
}
</script>

<style scoped>
.collapse-header {
  position: relative;
  right: 45%;
}
</style>
