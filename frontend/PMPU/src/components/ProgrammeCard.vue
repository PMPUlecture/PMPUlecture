<template>

  <div class="shadow card mb-3">
    <img :src="programme.img_url" class=" imgback" alt="...">
    <div class="card-img-overlay d-flex justify-content-end flex-column m-md-3">
      <router-link :to="'programme/'+programme.id" class="stretched-link text-white"><h3
        class="display program-text1 text-white text-of-card text-break text-truncate">{{ programme.name }}</h3></router-link>
    </div>
  </div>

</template>

<script>

export default {
  props: {
    programme: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      loading: false
    }
  },
  name: "ProgrammeCard"
}
</script>

<style scoped>

a:hover {
  text-decoration: none; /* Отменяем подчеркивание у ссылки */
}

.imgback {
  height: 250px;
  object-fit: cover;

}

.program-text1 {
  text-shadow: #000 3px 3px 5px;
}

.shadow {
  box-shadow: 0 0 18px #000;
}
</style>
