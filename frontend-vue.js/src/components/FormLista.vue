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
            <th>Visualização</th>
            <th>Update</th>
            <th>Exclusão</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="cir in cirurgias" v-bind:key="cir.id">
          
            <td>{{ cir.nome }}</td>
            <td>{{ cir.cpf }}</td>
            <td>
              <button class="btn btn-success" v-on:click="visualizarPac(cir.id)">
                Visualizar
              </button>
            </td>
            <td>
              <button class="btn btn-warning" v-on:click="updatePac(cir.id)">
                Update
              </button>
            </td>
            <td>
              <button class="btn btn-danger" v-on:click="deletePac(cir.id)">
                Delete
              </button>
            </td>
          </tr>

        </tbody>
      </table>
      
      <div class="row">
        <button class="btn btn-success" v-on:click="addPac()">Adicionar</button>
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
      cirurgias: [],
      message: "",
      medicos: [],
      errors:[],
    };
  },
  methods: {
    refreshPac() {
      UserDataService.retrieveAllPacs().then((res) => {
        this.cirurgias = res.data;
      });
    },
    addPac() {
      this.$router.push(`/pac/-1`);
    },
    visualizarPac(id) {
      this.$router.push(`/pac/${id}/visualizar`);
    },
    updatePac(id) {
      this.$router.push(`/pac/${id}`);
    },
    deletePac(id) {
      UserDataService.deletePac(id).then(() => {
        this.refreshPac();
      });
    },

  },
  created() {
    this.refreshPac();
  },
};
</script>