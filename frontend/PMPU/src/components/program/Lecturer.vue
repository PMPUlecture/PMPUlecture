<template>
<div>
  <a href="#"><h4 class="lecturer-text">{{lecturerInfo.name}}</h4></a>
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
