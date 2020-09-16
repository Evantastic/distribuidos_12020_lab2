const express = require('express');
const redis = require('redis');
const cors = require('cors');

const redisClient = redis.createClient({
    host: process.env.REDISHOST,
    port: process.env.REDISPORT
});

const app = express();
app.use(express.json());
app.use(cors());

//Rutas para conseguir datos
app.get('/:id', (req,res) => {
    const { id } = req.params;
    redisClient.hgetall(id,(err,object) => {
        res.send(object);
    });
});

redisClient.on("connect", function(){
    console.log("Estas conectado");
});

app.set("port", process.env.EXPRESSPORT || 3000);

app.listen(process.env.EXPRESSPORT, () =>{
    console.log(`Listening on ${process.env.EXPRESSPORT} connected to ${process.env.REDISHOST} on ${process.env.REDISPORT}`)
});