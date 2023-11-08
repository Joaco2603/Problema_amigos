
let ListaDeAmigos = [];
let ListaDeAmigosAInvitar = [];

class Amigos
{
    constructor(nombre,platos)
    {
        this.nombre = nombre;
        this.platos = platos;
    }
}

const NuevoAmigo =(nombreP = '',platosP = '')=>
{
    const nuevoAmigo = new Amigos(nombreP, platosP);
    ListaDeAmigos.push(nuevoAmigo)
}

NuevoAmigo('Carlos',10);
NuevoAmigo('Sofia',8);
NuevoAmigo('Carlos',10);

const main = ()=>
{
    let filtro;


    for (let i = 0; i < ListaDeAmigos.length; i++) {
        filtro = ListaDeAmigos[i];
        for (let j = 0; j < ListaDeAmigos.length; j++) {
            if(ListaDeAmigos[j+1] != undefined && filtro == ListaDeAmigos[j+1])
            {
                filtro = ListaDeAmigos[j+1];
                ListaDeAmigosAInvitar.push(filtro);
            }
        }
    }
    console.log(ListaDeAmigosAInvitar)
}


main();