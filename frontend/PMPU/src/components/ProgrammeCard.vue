<template>

    <div class="card mb-3" @click.prevent="OnClick">
      <img :src=programme.img_url class="card-img imgback" alt="...">
      <div class="card-img-overlay d-flex justify-content-end flex-column">
        <a href="#" class="stretched-link text-white"><h2 class="display program-text text-white">{{programme.name}}</h2></a>
      </div>
    </div>

</template>

<script>
import axios from "axios";

export default {
  props: {
    programme: {
      type: Object,
      required: true
    }
  },
  methods: {
    OnClick() {
      console.log('clicked')
      const progName = this.programme.name
      console.log(progName)
      this.$emit('show-prog',progName)
    }
  },
  name: "ProgrammeCard"
}
</script>

<style scoped>
.imgback{
  max-height: 250px;
  object-fit: cover;
}

.program-text {
  text-shadow: #000 3px 3px 5px;

  //position: relative;
  font-size: 300%;
  //right: 40%;
  //top: 100%;
  //font-family: fantasy;
  //-webkit-text-stroke-width: 2px;
  //-webkit-text-stroke-color: black;
  //text-shadow: black 0 0 20px;;
}
</style>
