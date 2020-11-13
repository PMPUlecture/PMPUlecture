<template>
 <!-- id="app" не нужен -->
    <!-- Image and text -->
    <div class="container-fluid">
      <div class="row vh-100">
        <div class="col-3">  <!-- левая колонка со ссылками, не меняется -->

          <div class="card h-75 sticky-top">
            <div class="card-body d-flex flex-column justify-content-between">

              <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action" href="https://vk.com/pmpu_news">ПМ-ПУ СМИ</a>
                <a class="list-group-item list-group-item-action" href="https://vk.com/sspmpu">Студсовет ПМ-ПУ</a>
                <a class="list-group-item list-group-item-action" href="#">Студсовет2 ПМ-ПУ</a>
              </div>

              <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action" href="#">1</a>
                <a class="list-group-item list-group-item-action" href="#">2</a>
              </div>

            </div>
          </div>

        </div>
        <div class="col"> <!-- правая колонка, меняется -->

          <div class="card h-100">
            <div class="card-body">

              <Programmes v-if="state == 'list'"
                          @show-prog="changeView"
              />
              <ProgramInfo v-if="state == 'info'"
                           :progName="this.progName"
              />
              <!-- @show-list="changeView2" -->


            </div>
          </div>

        </div>
      </div>
    </div>

</template>

<script>
import Programmes from '../components/Programmes';
import ProgramInfo from '../components/ProgramInfo';

export default {
  //name: 'App',
  components: {
    Programmes,
    ProgramInfo
  },
  data() {
    return {
      state: 'list',
      progName: null,
    }
  },
  methods: {
    changeView(progName){
      console.log('changeView1()')
      console.log(progName)
      this.state = 'info'
      this.progName = progName
    }
  }
}
</script>

<style>

</style>
