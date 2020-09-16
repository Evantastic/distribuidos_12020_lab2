<template>
    <v-list  color="rgb(255,255,255)" dense>
        <v-list-item>
            <v-icon id="flecha">mdi-subdirectory-arrow-right</v-icon>
            <v-list-item-content id="datoTarjeta" >Promedio: </v-list-item-content>
            <v-list-item-content id="datoTarjeta2" class="align-end">{{ planet_data.prom }}</v-list-item-content>
        </v-list-item>
        <v-list-item v-if="planet_data.min != NULL">
            <v-icon id="flecha">mdi-subdirectory-arrow-right</v-icon>
            <v-list-item-content id="datoTarjeta" >Mínimo: </v-list-item-content>
            <v-list-item-content id="datoTarjeta2" class="align-end">{{ planet_data.min }}</v-list-item-content>
        </v-list-item>
        <v-list-item v-if="planet_data.min != NULL">
            <v-icon id="flecha">mdi-subdirectory-arrow-right</v-icon>
            <v-list-item-content id="datoTarjeta" >Máximo: </v-list-item-content>
            <v-list-item-content id="datoTarjeta2" class="align-end">{{ planet_data.max }}</v-list-item-content>
        </v-list-item>
        <v-list-item>
            <v-icon id="flecha">mdi-subdirectory-arrow-right</v-icon>
            <v-list-item-content id="datoTarjeta" >Desviación estandar: </v-list-item-content>
            <v-list-item-content id="datoTarjeta2" class="align-end">{{ planet_data.std }}</v-list-item-content>
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