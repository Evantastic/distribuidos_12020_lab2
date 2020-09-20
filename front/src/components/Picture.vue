<template>
    <v-container>
        <v-row>
            <v-col v-for="picture in name" :key="picture">
                <v-img
                src="picture"
                lazy-src="https://picsum.photos/id/11/100/60"
                aspect-ratio="1"
                class="grey lighten-2"
                max-width="500"
                max-height="300"
                >
                    <template v-slot:placeholder>
                        <v-row
                        class="fill-height ma-0"
                        align="center"
                        justify="center"
                        >
                    <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                    </v-row>
                    </template>
                 </v-img>
            </v-col>
        </v-row>
    </v-container>
</template>


<script>
export default {
    name: 'Picture',
    props: ["idObject"],
    data: () => ({
      names:'',
      pictures: [
        {
          id: 1,
          img: 'https://storage.googleapis.com/distribuidos-astro/ZTF17aaarspi/1.png'
        
        },
        {
          id: 2,
          img: 'https://bad.src/not/valid'
          
        },
        {
          id: 3,
          img: 'https://bad.src/not/valid'
          
        },
      ]
    }),
    created () {
      this.names = ['https://storage.googleapis.com/distribuidos-astro/' + this.idObject + '/1.png',
                    'https://storage.googleapis.com/distribuidos-astro/' + this.idObject + '/2.png',
                    'https://storage.googleapis.com/distribuidos-astro/' + this.idObject + '/3.png']
    }
}
</script>