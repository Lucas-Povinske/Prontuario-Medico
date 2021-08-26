<template>
  <div class="container">
    <div class="navbar-header">
      <img src="./assets/Form.png" height="100px" width="150px">
      <a class="navbar-brand" href="#">Aplicação de Prontuário Médico</a><br/><br/>
    <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: "app"
};
</script>

<style>
@import url(https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css);

</style>
