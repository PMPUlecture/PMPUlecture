<template>
  <div>

  <h3 class="text-center text-break"> {{material.name}} </h3>


    <div class="row">
      <div class="col" v-if="material.source[0].abstract.length">
        <Abstracts :sources="material.source[0].abstract" />
      </div>
      <div class="col" v-if="material.source[0].questions.length">
        <Questions :sources="material.source[0].questions" />
      </div>
      <div class="col" v-if="material.source[0].test.length">
        <Tests :sources="material.source[0].test" />
      </div>
      <div class="col" v-if="material.source[0].other.length">
        <Other :sources="material.source[0].other" />
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
  props: ['material'],
  data () {
    return {

    }
  },
  created() {

  },


}
</script>

<style scoped>

</style>
