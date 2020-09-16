<template>
    <v-container>
        <v-row>
            <v-col v-for="picture in pictures" :key="picture.id">
                <v-img
                :src="picture.img"
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
    data: () => ({
      pictures: [
        {
          id: 1,
          img: 'https://picsum.photos/id/11/100/60'
        
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
    })
}
</script>