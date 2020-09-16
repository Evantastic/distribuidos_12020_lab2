<template>
    <v-container id="principal">
        <v-row style="height:90%" align="center">
            <v-col cols="12" class="white--text text-center display-1" id="posicion">
                <h1 id="tituloInicio">El universo en un Stream</h1> <br />
                <p  id="tituloInicio" style="text-align:center;">Explora la información de nuevos mundos</p>
            </v-col>
            <List/>
        </v-row>   
    </v-container>
</template>

<script>
import List from '@/components/List.vue';


export default {
    name: 'Home',
    components: {
        List,

    }
}
</script>

<style>
#principal{
    background-image: url("../assets/stars2.jpg");
    background-size: cover;
    width: 100%;
    max-width: 100%;
    height: 100%;
    max-height: 100%;
}

#principal:before {
	content:'';
	position: absolute;
    top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	background-color: rgba(0,0,0,0.3);
}

#tituloInicio{
    color: #fff;
    position: relative;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

#posicion{
    margin-top: auto;
}
</style>