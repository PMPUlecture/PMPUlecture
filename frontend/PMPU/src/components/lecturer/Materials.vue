<template>
  <div v-if="hasSmth">

  <h3 class="text-center text-break"> {{material.name}} </h3>


    <div class="row">

      <div class="col" v-if="material.source[0].abstract.length">
        <MaterialBlock :sources="material.source[0].abstract"
                   v-on:remove="$emit('remove', $event)"
                   v-on:edit="addType($event, 'abstract', 'edit')"
        name="Конспекты"/>
      </div>

      <div class="col" v-if="material.source[0].questions.length">
        <MaterialBlock :sources="material.source[0].questions"
                   v-on:remove="$emit('remove', $event)"
                   v-on:edit="addType($event, 'questions', 'edit')"
        name="Вопросы"/>
      </div>

      <div class="col" v-if="material.source[0].test.length">
        <MaterialBlock :sources="material.source[0].test"
               v-on:remove="$emit('remove', $event)"
               v-on:edit="addType($event, 'test', 'edit')"
        name="Контрольные"/>
      </div>

      <div class="col" v-if="material.source[0].other.length">
        <MaterialBlock :sources="material.source[0].other"
               v-on:remove="$emit('remove', $event)"
               v-on:edit="addType($event, 'other', 'edit')"
        name="Другое"/>
      </div>
    </div>
  </div>
</template>

<script>

import MaterialBlock from "./materials/MaterialBlock";


export default {
  name: "Materials",
  components: {
    MaterialBlock
  },
  props: ['material'],

  methods: {
    addType(event, type, name_of_event){
      event.type = type
      this.$emit(name_of_event, event)
    }
  },

  data () {
    return {
      hasSmth:
        ((this.material.source[0].abstract[0] != null) ||
        (this.material.source[0].questions[0] != null) ||
        (this.material.source[0].test[0] != null) ||
        (this.material.source[0].other[0] != null))
    }
  },
  watch: {
    material: function () {
      this.hasSmth =
        ((this.material.source[0].abstract[0] != null) ||
        (this.material.source[0].questions[0] != null) ||
        (this.material.source[0].test[0] != null) ||
        (this.material.source[0].other[0] != null))
    }
  },
}
</script>

<style scoped>

</style>
