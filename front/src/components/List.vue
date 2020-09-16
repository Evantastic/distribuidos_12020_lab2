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
export default {
    data: () => ({
      page: 1,
      perPage: 5,
      Planets: [
        {
          id: 1,
          nombre: 'Planeta 1'
        },
        {
          id: 2,
          nombre: 'Planeta 2'
        },
        {
          id: 3,
          nombre: 'Planeta 3'
        },
        {
          id:4,
          nombre: 'Planeta 4'
        },
        {
          id: 5,
          nombre: 'Planeta 5'
        },
        {
          id: 6,
          nombre: 'Planeta 6'
        },
        {
          id: 7,
          nombre: 'Planeta 7'
        },
        {
          id: 8,
          nombre: 'Planeta 8'
        },
        {
          id: 9,
          nombre: 'Planeta 9'
        },
        {
          id: 10,
          nombre: 'Planeta 10'
        },
        {
          id: 11,
          nombre: 'Planeta 11'
        },
        {
          id: 12,
          nombre: 'Planeta 12'
        }

      ]
    }),
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