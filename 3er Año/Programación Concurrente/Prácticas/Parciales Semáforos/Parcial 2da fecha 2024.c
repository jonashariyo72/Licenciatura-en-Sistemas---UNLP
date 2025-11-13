Parcial 2da fecha 2024


1. Resolver con SEMÁFOROS. La Clave Única de Identificación Tributaria (CUIT) es una clave que se utiliza
en el sistema tributario en la Argentina. Consta de un total de once cifras, siendo la última un dígito verificador (del 0 al 9). 
Una empresa cuenta con una lista de CUITs que debe procesar, debiendo informar la cantidad de CUITs por dígito verificador.
Para ello, dispone de un software que emplea 5 workers, los cuales trabajan colaborativamente procesando de a un cuit por vez cada uno. Al finalizar el procesamiento, el último worker en terminar debe informar los resultados
del procesamiento. Notas: la función obtenerDV(CUIT) retorna el dígito verificador para la CUIT recibida como entrada.
La lista de CUITs se almacena como una cola global y la solución debe maximizar la concurrencia.

int contGlobal [0..9] = {0,0,0,0,0,0,0,0,0,0};
cola cuits;
int termine = 0;


Process Worker[0..4]{
    int cuit; 
    int contPersonal[0..9];

    P(mutex)
    while (!cuits.isEmpty()){
        P(mutex);
        cuit := cuits.pop();
        contGlobal[obtenerDV(cuit)]++;
        V(mutex);
    }
    V(mutex);

    P(term)
    termine++;
    if (termine = 5){
        for (i: 0..9){
            print (contGlobal[i]);
        }
    }
    V(term);

}


1. Primera Fecha 2024

cola compradores [N];
sem espera[0..N-1];


Process Comprador [0..N-1]{
    P(mutex);
    compradores.push(id);
    V(mutex);
    V(hayComprador);
    P(espera[id]);

    
}


Process Cajero [0..C-1]{
    P(hora);
    P(hayComprador);
    
}