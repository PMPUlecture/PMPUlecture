<template>
  <div>

  <h3 class="text-center text-break"> {{material.name}} </h3>


    <div class="row">
      <div class="col">
        <Abstracts :sources="material.source[0].abstract" />
      </div>S
      <div class="col">
        <Questions :sources="material.source[0].questions" />
      </div>
      <div class="col">
        <Tests :sources="material.source[0].test" />
      </div>
      <div class="col">
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
