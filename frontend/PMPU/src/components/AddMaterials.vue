<template>
  <div class="container">
  <div class="card border-dark row-cols-1 m-auto" style="max-width: 600px">
    <h5 class="card-header text-center"> Добавление материала </h5>
    <div class="card-body text-dark">

      <form @submit.prevent="postMaterial">

        <div class="form-group">

          <select v-model="degreeField" class="form-control" id="field1">
            <option selected="true" value="" disabled> Ступень </option>
            <option> Бакалавриат </option>
            <option> Магистратура </option>
          </select>

          <select v-model="programField" class="form-control mt-3" id="field2" :disabled="disableField2">
            <option selected="true" value="" disabled> Программа </option>
            <option v-for="prog in programs" :value="prog.id"> {{prog.name}} </option>
          </select>

          <div class="row mt-3 ml-1 d-flex justify-content-between">
            <label for="field3" class="col-3 col-form-label"> Семестр </label>
            <div class="col" style="width: 100px">
              <input v-model="semesterField" type="number" class="form-control" id="field3" :disabled="disableField3">
            </div>
            <div class="col-5 d-sm-block d-none"></div>
          </div>

          <select v-model="subjectField" class="form-control mt-3" id="field4" :disabled="disableField4">
            <option selected="true" value="" disabled> Предмет </option>
            <option v-for="subject in subjects" :value="subject.id"> {{subject.name}} </option>
          </select>

          <select v-model="lecturerField" class="form-control mt-3" id="field5" :disabled="disableField5">
            <option selected="true" value="" disabled> Лектор </option>
            <option v-for="lecturer in lecturers" :value="lecturer.id"> {{lecturer.name}} </option>
          </select>

          <input v-model="titleField" class="form-control mt-3" type="text" placeholder="Название" :disabled="disableField6">

          <input v-model="linkField" class="form-control mt-3" type="url" placeholder="Ссылка" :disabled="disableField7">

          <select v-model="typeField" class="form-control mt-3" id="field8" :disabled="disableField8">
            <option selected="true" value="" disabled> Тип материала </option>
            <option value="abstract"> Конспект </option>
            <option value="questions"> Вопросы </option>
            <option value="test"> Контрольная </option>
            <option value="other"> Другое </option>
          </select>

          <div class="text-center mt-3">
            <button type="submit" class="btn btn-primary" :disabled="disableButton"> Отправить </button>
          </div>

        </div>

      </form>

    </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";

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
      disableButton: true,

      degreeField: '',
      programField: '',
      semesterField: '',
      subjectField: '',
      lecturerField: '',
      titleField: '',
      linkField: '',
      typeField: '',

      programs: null,
      subjects: null,
      lecturers: null,

      material: {
        name: '',
        subject: '',
        type: '',
        lecturer: '',
        link: ''
      }
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
      this.disableButton = true

      if (this.programField != '') {
        this.disableField3 = false
      }
    },
    semesterField: 'getSubjects',
    subjectField: 'getLecturers',
    lecturerField: function () {

      //this.resetField('titleField', 'disableField6')
      //this.resetField('linkField', 'disableField7')

      if (this.lecturerField != '') {
        this.disableField6 = false
        this.disableField7 = false
        this.disableField8 = false
      }
    },
    titleField: 'unableButton',
    linkField: 'unableButton',
    typeField: 'unableButton'
  },
  created() {

  },
  methods: {
    getPrograms() {

      this.resetField('programField', 'disableField2')
      this.resetField('semesterField', 'disableField3')
      this.resetField('subjectField', 'disableField4')
      this.resetField('lecturerField', 'disableField5')
      this.resetField('titleField', 'disableField6')
      this.resetField('linkField', 'disableField7')
      this.resetField('typeField', 'disableField8')
      this.disableButton = true

      if (this.degreeField != '') {
        axios.get('/api/programmes/')
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
      this.disableButton = true

      if (this.semesterField != '') {
        axios.get('/api/subjects/', {
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
      this.disableButton = true

      if (this.subjectField != '') {
        axios.get('/api/lecturers/', {
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

      const str = JSON.stringify(this.material);
      axios.post('/api/material/', str)
        .then((response) => {
          if (response.data.status === 'ok') {
            this.degreeField = ''
            this.resetField('programField', 'disableField2')
            this.resetField('semesterField', 'disableField3')
            this.resetField('subjectField', 'disableField4')
            this.resetField('lecturerField', 'disableField5')
            this.resetField('titleField', 'disableField6')
            this.resetField('linkField', 'disableField7')
            this.resetField('typeField', 'disableField8')
            this.disableButton = true

            alert('Успешно отправлено!')
          }
          else{
            alert(response.data.error)
          }
        })
        .catch((error) => {
          alert('Ошибка!')
          console.log(error);
        });
    }
  }
}
</script>

<style scoped>

</style>
