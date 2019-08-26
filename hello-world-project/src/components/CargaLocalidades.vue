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
      <md-table v-model="localidades" md-sort="id" md-sort-order="asc" md-card md-fixed-header>
        <md-table-toolbar>
          <h1 class="md-title">Localidades</h1>
        </md-table-toolbar>

        <md-table-row slot="md-table-row" slot-scope="{ item }">
          <md-table-cell md-label="ID" md-sort-by="id" md-numeric>
            {{ item.id }}
          </md-table-cell>
          <md-table-cell md-label="Concepto" md-sort-by="concepto">
            {{ item.concepto }}
          </md-table-cell>
          <md-table-cell md-label="No. Registros" md-sort-by="noRegistros">
            {{ item.noRegistros }}
          </md-table-cell>
          <md-table-cell md-label="Monto" md-sort-by="monto" md-numeric>
            {{ item.monto }}
          </md-table-cell>
        </md-table-row>
      </md-table>
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
      localidades: [
        {
          id: 1,
          concepto: 'Localidades No Vigentes',
          noRegistros: 100,
          monto: '0.0',
        },
        {
          id: 2,
          concepto: 'Localidades No Vigentes',
          noRegistros: 100,
          monto: '0.0',
        },
        {
          id: 3,
          concepto: 'Clientes a Desmarcar',
          noRegistros: 100,
          monto: '0.0',
        },
        {
          id: 4,
          concepto: 'Clientes a Desmarcar',
          noRegistros: 100,
          monto: '0.0',
        },
        {
          id: 5,
          concepto: 'Clientes a Desmarcar',
          noRegistros: 100,
          monto: '0.0',
        },
        {
          id: 6,
          concepto: 'Localidades No Vigentes',
          noRegistros: 100,
          monto: '0.0',
        },
        {
          id: 7,
          concepto: 'Localidades No Vigentes',
          noRegistros: 100,
          monto: '0.0',
        },
        {
          id: 8,
          concepto: 'Clientes a Desmarcar',
          noRegistros: 100,
          monto: '0.0',
        },
        {
          id: 9,
          concepto: 'Asentamientos a Eliminar',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 10,
          concepto: 'Asentamientos a Eliminar',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 11,
          concepto: 'Asentamientos a Eliminar',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 12,
          concepto: 'Localidades No Vigentes',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 13,
          concepto: 'Localidades No Vigentes',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 14,
          concepto: 'Localidades No Vigentes',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 15,
          concepto: 'Localidades No Vigentes',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 16,
          concepto: 'Localidades Nuevas',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 17,
          concepto: 'Localidades Nuevas',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 18,
          concepto: 'Localidades Nuevas',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 19,
          concepto: 'Localidades Nuevas',
          noRegistros: 50,
          monto: '0.0',
        },
        {
          id: 20,
          concepto: 'Localidades No Vigentes',
          noRegistros: 50,
          monto: '0.0',
        },
      ],
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
