<template>
    <v-list  color="rgb(255,255,255)" dense>
        <v-list-item>
            <v-icon id="flecha">mdi-subdirectory-arrow-right</v-icon>
            <v-list-item-content id="datoTarjeta" >Promedio: </v-list-item-content>
            <v-list-item-content v-if="planet_data.promedio!=null" id="datoTarjeta2" class="align-end">{{ planet_data.promedio }}</v-list-item-content>
            <v-list-item-content v-else id="datoTarjeta2" class="align-end">null</v-list-item-content>
        </v-list-item>
        <v-list-item>
            <v-icon id="flecha">mdi-subdirectory-arrow-right</v-icon>
            <v-list-item-content id="datoTarjeta" >Desviación estandar: </v-list-item-content>
            <v-list-item-content v-if="planet_data.desviacion!=null" id="datoTarjeta2" class="align-end">{{ planet_data.desviacion }}</v-list-item-content>
            <v-list-item-content v-else id="datoTarjeta2" class="align-end">null</v-list-item-content>
        </v-list-item>
    </v-list>
</template>

<script>
export default {
    name: 'Data',
    props: {
        planet_data: Object
    }
}
</script>

<style>

#flecha{
    color: #f86525;
}

</style>