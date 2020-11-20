<template>
<div>

  <router-link :to="{query: {subjectID: currentsubject}, path: '../lecturer/'+lecturerInfo.id }"
               class="list-group-item-success list-group-item list-group-item-action stretched-link">
    {{lecturerInfo.name}}
  </router-link>

</div>
</template>

<script>

export default {
  name: "Lecturer",
  props: {
    lecturerInfo: {
      type: Object,
      required: true
    },
    currentsubject: Number,
  },
}
</script>

<style scoped>
.lecturer-text {
  position: relative;
  right: 45%;
  color: olivedrab;
}
</style>
