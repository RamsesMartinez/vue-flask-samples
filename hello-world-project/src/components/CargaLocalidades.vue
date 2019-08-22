<template>
  <div class="ReporteGlobal">
    <div class="container">
      <div>
        <div class="container">
          <md-field>
            <label>Single</label>
            <md-file v-model="file" @md-change="onFileUpload($event)" ></md-file>
          </md-field>
          <md-button class="md-raised md-primary" @click.native="submitFile()">
            Cargar Layout
            <md-icon>cloud_upload</md-icon>
          </md-button>
        </div>
      </div>
    </div>
  </div>


</template>

<script>

export default {
  name: 'CargaLocalidades',
  props: {
    msg: String,
  },
  data() {
    return {
      file: null,
      finalFile: null,
    };
  },
  methods: {
    /**
     * Submits the file to the server
     */
    submitFile() {
      // Initialize the form data
      const formData = new FormData();
      const headers = {
        'Content-Type': 'multipart/form-data',
      };
      // Add the form data we need to submit
      formData.append('file', this.finalFile);

      // Make the request to the POST /single-file URL
      this.$http.post('http://127.0.0.1:5000/api/file', formData, { headers }).then((res) => {
        // success actions
        console.log(res);
      });
    },

    onFileUpload(evt) {
      this.finalFile = evt[0];
    },
  },
};
</script>
