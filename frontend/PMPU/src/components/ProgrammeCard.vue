<template>
  <button type="button" class="btn btn-secondary btn-lg btn-block">
    <div class="card-body">
      <div class="card bg-dark text-white">
          <img :alt=programme.name :src=programme.img_url class="card-img images" style="max-height: 250px; object-fit: cover;">
        <!-- <p> {{this.progList.bachelor[0].img_url }} </p> -->
        <div class="card-img-overlay">

          <p class="program-text1">
            {{ programme.name }}
          </p>

        </div>
      </div>
    </div>
  </button>
</template>

<script>
export default {
  props: {
    programme: {
      type: Object,
      required: true
    }
  },
  name: "ProgrammeCard"
}
</script>

<style scoped>

</style>
