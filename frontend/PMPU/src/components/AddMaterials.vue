<template>
  <div>
    <div v-if="user.is_authenticated">
      <!-- Modal -->
      <div class="modal fade" id="staticBackdrop" data-backdrop="static" data-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="staticBackdropLabel">Добавление лектора</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body d-flex flex-column">
              <p><b>Выберете лектора, который ведёт данный предмет:</b></p>
              <p>{{subjectInformation.name}} на программе {{subjectInformation.programme}}</p>

              <label>
                <select v-model="subjectInformation.currentLecturer" class="form-control">

                  <option v-for="lecturer in this.subjectInformation.allLecturers" :value="lecturer.id">{{lecturer.name}}</option>
                </select>
              </label>

            </div>
            <div class="modal-footer d-flex justify-content-between">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Отмена</button>
              <div id="action">
                <button type="button" class="btn btn-primary" v-on:click="put_lecturer">Добавить лектора</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="container-fluid">
      <div class="card border-dark row-cols-1 m-auto" style="max-width: 600px">
        <h5 class="card-header text-center"> Добавление материала </h5>
        <div class="card-body text-dark">

          <form @submit.prevent="postMaterial">

            <div class="form-group">

              <select v-model="degreeField" class="form-control custom-select" id="field1">
                <option selected="true" value="" disabled> Ступень </option>
                <option> Бакалавриат </option>
                <option> Магистратура </option>
              </select>

              <select v-model="programField" class="form-control custom-select mt-3" id="field2" :disabled="disableField2">
                <option selected="true" value="" disabled> Программа </option>
                <option v-for="prog in programs" :value="prog.id"> {{prog.name}} </option>
              </select>

              <div class="row mt-3 ml-1 d-flex justify-content-between">
                <label for="field3" class="col-3 col-form-label"> Семестр </label>
                <div class="col">
                  <input  style="width: 100px" v-model="semesterField" type="number" class="form-control" id="field3" :disabled="disableField3">
                </div>
              </div>

              <select v-model="subjectField" class="form-control custom-select mt-3" id="field4" :disabled="disableField4">
                <option selected="true" value="" disabled> Предмет </option>
                <option v-for="subject in subjects" :value="subject.id"> {{subject.name}} </option>
              </select>

              <div class="row ml-0 mr-0">
                <select v-model="lecturerField" class="form-control custom-select mt-3 col" id="field5" :disabled="disableField5">
                  <option selected="true" value="" disabled> Лектор </option>
                  <option v-if="!lecturer.length" v-for="lecturer in lecturers" :value="lecturer.id"> {{lecturer.name}} </option>
                </select>

                  <button data-toggle="modal" type="button" data-target="#staticBackdrop" class="btn btn-danger col-sm-3 mt-3 ml-sm-3" v-on:click="get_subject_info" :disabled="disableField5">Нет лектора?</button>
              </div>
              <input v-model="titleField" class="form-control mt-3" type="text" placeholder="Название" :disabled="disableField6">

              <input v-model="linkField" class="form-control mt-3" type="url" placeholder="Ссылка" :disabled="disableField7">

              <div class="row mt-3 ml-1 d-flex justify-content-between">
                <label for="field9" class="col-3 col-form-label"> Год </label>
                <div class="col" >
                  <input style="width: 100px" v-model="year_of_relevance" type="number" class="form-control" id="field9" :disabled="disableField9">
                </div>

              </div>

              <select v-model="typeField" class="form-control custom-select mt-3" id="field8" :disabled="disableField8">
                <option selected="true" value="" disabled> Тип материала </option>
                <option value="abstract"> Конспект </option>
                <option value="questions"> Вопросы </option>
                <option value="test"> Контрольная </option>
                <option value="other"> Другое </option>
              </select>

              <div class="custom-control custom-switch mt-3 ml-3">
                <input v-model="only_authorized_users" type="checkbox" class="custom-control-input" id="field10" :disabled="disableField10">
                <label class="custom-control-label" for="field10">Сделать материал видимым только для студентов</label>
              </div>

              <div class="text-center mt-3">
                <button type="submit" class="btn btn-primary" :disabled="disableButton"> Отправить </button>
              </div>

            </div>

          </form>

        </div>
      </div>
      </div>
      <div aria-live="polite"  aria-atomic="true" class="d-flex justify-content-center align-items-center" style="position: fixed;
    top: 100px; right: 50px; z-index: 10">
        <div role="alert" id="error2" aria-live="assertive" aria-atomic="true" class="toast" data-delay="1500">
          <div class="toast-header">

            <strong class="mr-auto">{{toasts.title}}</strong>
          </div>
          <div class="toast-body">
            {{toasts.body}}
          </div>
        </div>
      </div>

    </div>

    <div v-else>
      <template>
        <div class="card text-white bg-warning mt-3 mb-3">
          <div class="card-body">
            <h4 class="card-title">Вход не выполнен</h4>
            <p class="card-text">Вы не вошли на сайт. Вы можете просматривать метериалы, но чтобы добавить свои
            необходимо войти.</p>
            <a class="btn btn-danger" href="/account/login/google-oauth2/">Вход через Google</a>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import variables from "../views/variables"; variables

export default {
  name: "AddMaterials",
  data () {
    return {
      disableField2: true,
      disableField3: true,
      disableField4: true,
      disableField5: true,
      disableField6: true,
      disableField7: true,
      disableField8: true,
      disableField9: true,
      disableField10: true,
      disableButton: true,

      degreeField: '',
      programField: '',
      semesterField: '',
      subjectField: '',
      lecturerField: '',
      titleField: '',
      linkField: '',
      typeField: '',
      only_authorized_users: false,
      nowYear: new Date().getFullYear(),
      year_of_relevance: new Date().getFullYear(),

      programs: null,
      subjects: null,
      lecturers: null,

      material: {
        name: '',
        subject: '',
        type: '',
        lecturer: '',
        link: ''
      },

      toasts: {
        title: "",
        body: ""
      },

      subjectInformation: {
        name: '',
        programme: '',
        allLecturers: [],
        currentLecturer: '',
        only_authorized_users: false,
      },

      user: {
        "is_authenticated": true,
        "email": "",
        "first_name": "",
        "last_name": "",
        "is_admin": false
      },
    }
  },
  watch: {
    degreeField: 'getPrograms',
    programField: function () {

      this.resetField('semesterField', 'disableField3')
      this.resetField('subjectField', 'disableField4')
      this.resetField('lecturerField', 'disableField5')
      this.resetField('titleField', 'disableField6')
      this.resetField('linkField', 'disableField7')
      this.resetField('typeField', 'disableField8')
      this.disableField9 = true
      this.disableButton = true

      if (this.programField != '') {
        this.disableField3 = false
      }
    },
    semesterField: function (){
      if (this.semesterField < 1){
        this.semesterField = 1
      }
      if (this.semesterField > 8){
        this.semesterField = 8
      }
        this.getSubjects()

    },
    subjectField: 'getLecturers',
    lecturerField: function () {

      //this.resetField('titleField', 'disableField6')
      //this.resetField('linkField', 'disableField7')

      if (this.lecturerField != '') {
        this.disableField6 = false
        this.disableField7 = false
        this.disableField8 = false
        this.disableField9 = false
        this.disableField10 = false

      }
    },
    titleField: 'unableButton',
    linkField: 'unableButton',
    typeField: 'unableButton',
    year_of_relevance: function () {
      if (this.year_of_relevance > this.nowYear + 1){
        console.log("year")
        this.year_of_relevance = this.nowYear + 1
      }
      if (this.year_of_relevance < 2000){
        this.year_of_relevance = 2000
      }
    }
  },
  created() {
    //this.getUser()
  },
  methods: {
    getUser() {
      axios.get(variables.url + '/api/user/')
        .then(response => {
          this.user = response.data
        })
        .catch(error => {
          console.log(error);
        })
    },

    getPrograms() {

      this.resetField('programField', 'disableField2')
      this.resetField('semesterField', 'disableField3')
      this.resetField('subjectField', 'disableField4')
      this.resetField('lecturerField', 'disableField5')
      this.resetField('titleField', 'disableField6')
      this.resetField('linkField', 'disableField7')
      this.resetField('typeField', 'disableField8')
      this.disableField9 = true
      this.disableField10 = true
      this.disableButton = true

      if (this.degreeField != '') {
        axios.get(variables.url + '/api/programmes/')
          .then(response => {
            if (this.degreeField == 'Бакалавриат')
              this.programs = response.data.bachelor
            else if (this.degreeField == 'Магистратура')
              this.programs = response.data.master
            this.disableField2 = false
          })
          .catch(error => {
            console.log(error);
            console.log('bad');
          })
      }
    },
    getSubjects() {
      let semester = this.semesterField
      if (semester == 0) semester = 100

      this.resetField('subjectField', 'disableField4')
      this.resetField('lecturerField', 'disableField5')
      this.resetField('titleField', 'disableField6')
      this.resetField('linkField', 'disableField7')
      this.resetField('typeField', 'disableField8')
      this.disableField9 = true
      this.disableField10 = true
      this.disableButton = true

      if (this.semesterField != '') {
        axios.get(variables.url + '/api/subjects/', {
          params: {
            term: semester,
            programme: this.programField
          }
        })
          .then(response => {
            this.subjects = response.data.subjects
            if (this.subjects)
              this.disableField4 = false
          })
          .catch(error => {
            console.log(error);
          })
      }
    },
    getLecturers() {

      this.resetField('lecturerField', 'disableField5')
      this.resetField('titleField', 'disableField6')
      this.resetField('linkField', 'disableField7')
      this.resetField('typeField', 'disableField8')
      this.disableField9 = true
      this.disableField10 = true
      this.disableButton = true

      if (this.subjectField != '') {
        axios.get(variables.url + '/api/lecturers/', {
          params: {
            subject: this.subjectField
          }
        })
          .then(response => {
            this.lecturers = response.data
            this.disableField5 = false
          })
          .catch(error => {
            console.log(error);
            console.log('bad');
          })
      }
    },
    unableButton() {
      if (this.titleField && this.linkField && this.typeField)
        this.disableButton = false
      else
        this.disableButton = true
    },
    resetField(fieldName, fieldDisable) {
      eval('this.'+fieldName+' = \'\'')
      eval('this.'+fieldDisable+' = true')
    },
    postMaterial() {
      this.material.name = this.titleField
      this.material.subject = this.subjectField
      this.material.type = this.typeField
      this.material.lecturer = this.lecturerField
      this.material.link = this.linkField
      this.material.year_of_relevance = this.year_of_relevance
      this.material.only_authorized_users = this.only_authorized_users

      const str = JSON.stringify(this.material);

      axios.post(variables.url + '/api/material/', str)
        .then((response) => {
          console.log(response.data)
          if (response.data.status === 'ok') {
            this.degreeField = ''
            this.resetField('programField', 'disableField2')
            this.resetField('semesterField', 'disableField3')
            this.resetField('subjectField', 'disableField4')
            this.resetField('lecturerField', 'disableField5')
            this.resetField('titleField', 'disableField6')
            this.resetField('linkField', 'disableField7')
            this.resetField('typeField', 'disableField8')
            this.disableField9 = true
            this.only_authorized_users = false
            this.disableField10 = true
            this.disableButton = true
            ym(70412992,'reachGoal','clickOnAddMaterial')
            this.toasts.title = "Успех";
            this.toasts.body = "Успешно отправлено!"
            $('.toast').toast('show');
          }
          else{
            this.toasts.title = "Error";
            this.toasts.body = response.data.error
            $('.toast').toast('show');
          }
        })
        .catch((error) => {
          this.toasts.title = "Ошибка!";
          this.toasts.body = "Что-то пошло не так..."
          $('.toast').toast('show');
        });
    },

    get_subject_info(){
      axios.get(variables.url + '/api/subjects/', {
        params:{
          id: this.subjectField,
          fields: 'programme'
        }
      })
      .then((response => {
        this.subjectInformation.name = response.data.subjects[0].name
        this.subjectInformation.programme = response.data.subjects[0].programme.name
      }))
      axios.get(variables.url + '/api/lecturers/')
      .then((response => {
        this.subjectInformation.allLecturers = response.data
      }))
    },

    put_lecturer(){
      if (this.subjectInformation.currentLecturer !== '') {
        axios.put(variables.url + '/api/lecturers/', {
          id: this.subjectInformation.currentLecturer,
          subjects: [this.subjectField]
        })
          .then((response) => {
            if (response.data.status === 'ok') {
              this.toasts.title = "Добавлено";
              this.toasts.body = "Преподаватель успешно добавлен!"
              $('.toast').toast('show');
              $('#staticBackdrop').modal('hide');
              this.getLecturers()
            }
            else{
              this.toasts.title = "Ошибка";
              this.toasts.body = "Permission denied!"
              $('.toast').toast('show');
              $('#staticBackdrop').modal('hide');
            }
          })
          .catch((error) => {
            console.log(error)
          })
      }
    }
  }
}
</script>

<style scoped>

</style>
