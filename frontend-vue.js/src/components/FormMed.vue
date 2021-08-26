<template>
  <div>
    <h3>Formulário de Nova Cirurgia Indicada</h3>
    <div class="container">
      <form @submit="validateAndSubmit">
        <div v-if="errors.length">
          <div
            class="alert alert-danger"
            v-bind:key="index"
            v-for="(error, index) in errors"
          >
            {{ error }} 
          </div>
        </div>
        <fieldset class="form-group">
          <label>Nome da Paciente</label>
          <input type="text" class="form-control" v-model="nome" />
        </fieldset>

        <fieldset class="form-group">
          <label>CPF</label>
          <input type="text" class="form-control" v-model="cpf" />
        </fieldset>
        <fieldset class="form-group">
          <label>Cirurgião Principal</label>

        <select class="droplist" @change = "medEscolhido($event)" v-model="cirurgiao">
            <option :value="med.nome" v-for="(med) in medicos" :key="med.id">{{med.nome}}</option>
        </select>
        </fieldset>

        <fieldset class="form-group">
          <label>Dias de Internação</label>
          <input type="number" class="form-control" v-model.number="diasInternado" />
        </fieldset>

        <fieldset class="form-group">
          <label>Tempo na Sala Cirúrgica</label>
          <input type="number" class="form-control" v-model.number="horasCirurgia" />
        </fieldset>

        <fieldset class="form-group">
          <label>Necessita de UTI?</label>
          <select class="droplist" @change = "utiEscolhido($event)" v-model="uti">
            <option value="Sim">Sim</option>
            <option value="Não">Não</option>
          </select>
        </fieldset>

        <fieldset class="form-group">
          <label>Necessita de Reserva de Sangue?</label>
          <select class="droplist" @change = "sangEscolhido($event)" v-model="reservaSangue">
            <option value="Sim">Sim</option>
            <option value="Não">Não</option>
          </select>
        </fieldset>

        <fieldset class="form-group">
          <label>Necessidade de Biópsia de Congelação?</label>
          <select class="droplist" @change = "biopEscolhido($event)" v-model="biopsiaCongelacao">
            <option value="Sim">Sim</option>
            <option value="Não">Não</option>
          </select>
        </fieldset>

        <fieldset class="form-group">
          <label>Preferência de Hospital</label>
        <select class="droplist" @change = "hospEscolhido($event)" v-model="hospital">
          <option :value="hosp.nome" v-for="(hosp) in hospitais" :key="hosp.id">{{hosp.nome}}</option>
        </select>
        </fieldset>

        <button class="btn btn-success" type="submit">Salvar</button>
      </form>
    </div>
  </div>
</template>
<script>
import UserDataService from "../service/UserDataService";

export default {
  name: "Paciente",
  data() {
    return {
      nome: "",
      cpf: "",
      cirurgiao: "",
      diasInternado:"",
      horasCirurgia:"",
      uti:"Não",
      reservaSangue:"Não",
      biopsiaCongelacao:"Não",
      hospital:"",

      medicos: [],
      hospitais: [],
      errors: [],
    };
  },

  computed: {
    id() {
      return this.$route.params.id;
    },
  },
  methods: {
    refreshPacDetails() {
      UserDataService.retrievePac(this.id).then((res) => {
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
    validateAndSubmit(e) {
      e.preventDefault();
      this.errors = [];
      if (!this.nome) {
        this.errors.push("Campo obrigatório");
      }
      if (!this.cpf) {
        this.errors.push("Campo obrigatório");
      } else if (this.cpf.length < 14) {
        this.errors.push("Insira o CPF com pontos e vírgulas");
      }
      if (this.errors.length === 0) {
        if (this.id == -1) {
          UserDataService.createPac({
            nome: this.nome,
            cpf: this.cpf,
            cirurgiao: this.cirurgiao,
            diasInternado: this.diasInternado,
            horasCirurgia: this.horasCirurgia,
            uti: this.uti,
            reservaSangue: this.reservaSangue,
            biopsiaCongelacao: this.biopsiaCongelacao,
            hospital: this.hospital,
          }).then(() => {
            this.$router.push("/");
          });
        } else {
          UserDataService.updatePac(this.id, {
            id: this.id,
            nome: this.nome,
            cpf: this.cpf,
            cirurgiao: this.cirurgiao,
            diasInternado: this.diasInternado,
            horasCirurgia: this.horasCirurgia,
            uti: this.uti,
            reservaSangue: this.reservaSangue,
            biopsiaCongelacao: this.biopsiaCongelacao,
            hospital: this.hospital,
          }).then(() => {
            this.$router.push("/");
          });
        }
      }
    },
    refreshMedicos() {
      UserDataService.retrieveAllMedicos().then((res) => {
        this.medicos = res.data;
      });
    },
    medEscolhido (event) {
      this.cirurgiao = event.target.options[event.target.options.selectedIndex].text
    },

    utiEscolhido (event) {
      this.uti = event.target.options[event.target.options.selectedIndex].text
    },

    sangEscolhido (event) {
      this.reservaSangue = event.target.options[event.target.options.selectedIndex].text
    },

    biopEscolhido (event) {
      this.biopsiaCongelacao = event.target.options[event.target.options.selectedIndex].text
    },

    refreshHospitais() {
      UserDataService.retrieveAllHospitais().then((res) => {
        this.hospitais = res.data;
      });
    },

    hospEscolhido (event) {
      this.hospital = event.target.options[event.target.options.selectedIndex].text
    },
    
  },
  created() {
    this.refreshPacDetails();
    this.refreshMedicos();
    this.refreshHospitais();
  },
};
</script>

<style>
select {
  width: 100%;
  padding: 16px 20px;
  border: none;
  border-radius: 10px #000000;
  background-color: #ffff;
}
</style>
