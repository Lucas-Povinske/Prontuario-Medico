<template>
  <div class="container">
    <h3>Todos os Formulários</h3>
    <div v-if="message" class="alert alert-success">{{ this.message }}</div>
    <div class="container">
      <table class="table">
        <thead> 
          <tr>
           
            <th>Nome da Paciente</th>
            <th>CPF</th>
            <th>Cirurgião Principal</th>
            <th>Dias de Internação</th>
          </tr>
        </thead>
        <tbody>
          <tr>
          
            <td>{{ nome }}</td>
            <td>{{ cpf }}</td>
            <td>{{ cirurgiao }}</td>
            <td>{{ diasInternado }}</td>
          </tr>

        </tbody>
      </table>

      <table class="table">
        <thead> 
          <tr>
            <th>Tempo de Sala Cirúrgica</th>
            <th>Necessita de UTI?</th>
            <th>Necessita de Reserva de Sangue?</th>
            <th>Necessidade de Biópsia Congelação?</th>
            <th>Preferência de Hospital</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{{ horasCirurgia }}</td>
            <td>{{ uti }}</td>
            <td>{{ reservaSangue }}</td>
            <td>{{ biopsiaCongelacao }}</td>
            <td>{{ hospital }}</td>
          </tr>

        </tbody>
      </table>

      <div class="row">
        <button class="btn btn-success" v-on:click="voltarLista()">Voltar</button>
      </div>
      
    </div>
  </div>
</template>
<script>
import UserDataService from "../service/UserDataService";

export default {
  name: "Cirurgias",
  data() {
    return {
      nome: "",
      cpf: "",
      cirurgiao: "",
      diasInternado:"",
      horasCirurgia:"",
      uti:"",
      reservaSangue:"",
      biopsiaCongelacao:"",
      hospital:"",
      errors:[],
    };
  },
  computed: {
    id() {
      return this.$route.params.id;
    },
  },
  methods: {
    refreshPacDetails() {
      UserDataService.visualizarPac(this.id).then((res) => {
        this.nome = res.data.nome;
        this.cpf = res.data.cpf;
        this.cirurgiao = res.data.cirurgiao;
        this.diasInternado = res.data.diasInternado;
        this.horasCirurgia = res.data.horasCirurgia;
        this.uti = res.data.uti;
        this.reservaSangue = res.data.reservaSangue;
        this.biopsiaCongelacao = res.data.biopsiaCongelacao;
        this.hospital = res.data.hospital;
      });
    },
    voltarLista() {
      this.$router.push(`/`);
    },

  },
  created() {
    this.refreshPacDetails();
  },
};
</script>