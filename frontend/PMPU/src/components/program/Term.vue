<template>


  <!--div class="accordion" id="accordionExample">
    <div class="card">
      <div class="card-header" id="headingOne">
        <h5 class="mb-0">
          <button class="btn btn-link collapse-header" type="button" data-toggle="collapse" :data-target="termidsharp" aria-expanded="true" >
            {{this.termInfo.term}} семестр
          </button>
        </h5>
      </div>

      <!div :id="termid" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
        <div class="card-body"-->

  <div class="card">
    <div class="card-header">
      <a class="stretched-link text-primary" data-toggle="collapse" :href="'#collapse'+this.termInfo.term" :aria-controls="'collapse'+this.termInfo.term">
        {{ this.termInfo.term }} семестр
      </a>
    </div>

    <div :id="'collapse'+this.termInfo.term" class="collapse" data-parent="#programme">
      <div class="card-body">
        <div class="accordion" :id="'collapseTerm'+this.termInfo.term">
          <Subject v-for="subject in this.termInfo.subjects"
                     :subjectInfo="subject" :termInfo="termInfo.term"
            />
        </div>
      </div>
    </div>
  </div>

  <!--div class="card">
    <div class="card-header" >
      <a data-toggle="collapse" :href="'#collapse'+this.termInfo.term" :aria-controls="'collapse'+this.termInfo.term">
        {{ this.termInfo.term }}
      </a>
    </div>
    <div :id="'collapse'+this.termInfo.term" class="collapse" data-parent="#programme">
      <div class="card-body">
        {{this.termInfo.subjects}}
      </div>
    </div>
  </div-->



        <!--/div>
      </div>
    </div>


  </div-->

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
