<template>
<div>
  <a href="#" class="list-group-item-success list-group-item list-group-item-action stretched-link">{{lecturerInfo.name}}</a>
</div>
</template>

<script>
export default {
  name: "Lecturer",
  props: {
    lecturerInfo: {
      type: Object,
      required: true
    }
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
