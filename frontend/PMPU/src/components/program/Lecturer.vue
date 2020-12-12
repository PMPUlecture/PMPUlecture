<template>
  <router-link :to="{query: {subjectID: currentSubject}, path: '../lecturer/'+lecturerInfo.id }"
               class="list-group-item-success list-group-item list-group-item-action stretched-link">
    {{lecturerInfo.name}}
  </router-link>
</template>

<script>

export default {
  name: "Lecturer",
  props: {
    lecturerInfo: {
      type: Object,
      required: true
    },
    currentSubject: Number,
  },
}
</script>

