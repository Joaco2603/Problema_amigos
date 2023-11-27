const express = require('express');
const cors = require('cors');

class Server{

    constructor()
    {
        this.port = {}
        this.app = express();

        this.middlewares()
    }

    middlewares()
    {
        this.app.use('cors');
        this.app.use(express.static('public'));
    }

    listen()
    {
        this.app(this.port,()=>{
            console.log("Conectado en el puerto " + this.port);
        })
    }
}


export default Server;