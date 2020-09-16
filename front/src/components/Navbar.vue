<template>
  <div>
    <v-app-bar
      id="navbar"
      dark
      class="elevation-0"
    >
      <v-spacer></v-spacer>
      <v-btn id="navbar" to="/" flat v-show="mostrar">Inicio</v-btn>
    </v-app-bar>
  </div>
</template>

<script>
export default {
    name: 'Navbar',
    data: () => ({
      mostrar: true
    })
}
</script>

<style>

#navbar{
  background-color: transparent;
}

</style>