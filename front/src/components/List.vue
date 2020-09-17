<template>
 <v-container id="list">
    <v-card>
      <v-list >
        <v-list-item :to="{ name:'Planet', params:{id: item.id}}" v-for="item in visiblePages" :key="item.id" >
          <v-icon id="flecha">mdi-earth</v-icon>
          <v-list-item-content>
            <v-list-title  >{{ item.nombre }}</v-list-title>
          </v-list-item-content>
        </v-list-item>
        <v-pagination
        v-model="page"
        :length="Math.ceil(Planets.length/5)"
      ></v-pagination>
      </v-list>
    </v-card>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
    data: () => ({
      page: 1,
      perPage: 5,
      Planets: ''
    }),
    created () {
      axios.get('http://localhost:5000/').then(
        res => {
          this.Planets = res.data
        } 
      );
    },
    computed: {
      visiblePages(){
        return this.Planets.slice((this.page -1) * this.perPage, this.page * this.perPage)
      },
      totalPages(){
        return this.Planets.length / 2
      }
    }
}
</script>

<style >
#elementList{
  background-color: #3998b5 !important;
}

#list{
  width: 60%;
}
</style>