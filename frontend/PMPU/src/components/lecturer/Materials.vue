<template>
  <div v-if="hasSmth">
  <h3 class="text-center ml-auto text-break"> {{material.name}} </h3>


    <div class="row">

      <div class="col">
        <MaterialBlock :sources="material.source[0].abstract"
                       :user="user"
                       v-on:remove="$emit('remove', $event)"
                       v-on:edit="addType($event, 'abstract', 'edit')"
                       v-on:add="$emit('add', {'subject': material.id_subject,
                        'subject_name': material.name, 'type': 'abstract'})"
        name="Конспекты"/>
      </div>

      <div class="col">
        <MaterialBlock :sources="material.source[0].questions"
                       :user="user"
                       v-on:remove="$emit('remove', $event)"
                       v-on:edit="addType($event, 'questions', 'edit')"
                       v-on:add="$emit('add', {'subject': material.id_subject,
                        'subject_name': material.name, 'type': 'questions'})"
        name="Вопросы"/>
      </div>

      <div class="col">
        <MaterialBlock :sources="material.source[0].test"
                       :user="user"
                       v-on:remove="$emit('remove', $event)"
                       v-on:edit="addType($event, 'test', 'edit')"
                       v-on:add="$emit('add', {'subject': material.id_subject,
                        'subject_name': material.name, 'type': 'test'})"
        name="Контрольные"/>
      </div>

      <div class="col">
        <MaterialBlock :sources="material.source[0].other"
                       :user="user"
                       v-on:remove="$emit('remove', $event)"
                       v-on:edit="addType($event, 'other', 'edit')"
                       v-on:add="$emit('add', {'subject': material.id_subject,
                        'subject_name': material.name, 'type': 'other'})"
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
  props: ['material', 'user'],

  methods: {
    addType(event, type, name_of_event){
      event.type = type
      this.$emit(name_of_event, event)
    },
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
