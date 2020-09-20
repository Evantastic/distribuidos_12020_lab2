<template>
    <v-container>
        <v-row>
            <v-col v-for="picture in names" :key="picture">
                <v-img
                :src="picture"
                lazy-src="https://storage.googleapis.com/distribuidos-astro/ZTF17aaagrhs/1.png"
                aspect-ratio="1"
                class="grey lighten-2"
                max-width="200"
                max-height="150"
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
      names:''
    }),
    created () {
      this.names = ['https://storage.googleapis.com/distribuidos-astro/' + this.idObject + '/1.png',
                    'https://storage.googleapis.com/distribuidos-astro/' + this.idObject + '/2.png',
                    'https://storage.googleapis.com/distribuidos-astro/' + this.idObject + '/3.png']
    }
}
</script>