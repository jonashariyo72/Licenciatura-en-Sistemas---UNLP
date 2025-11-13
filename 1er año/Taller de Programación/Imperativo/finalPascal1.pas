program finalPascal1;
type
rangoFacu = 1..17;

egresado = record
nombre: string;
legajo: integer;
ID: rangoFacu;
prom: real;

arbol = ^nodo;
nodo = record
dato: egresado;
HI: arbol;
HD: arbol;

vector = array [rangoFacu] of arbol;

procedure leerEgresado (var e: egresado);
begin
    read (e.prom);
    if (e.prom > 0) then begin
        read (e.nombre);
        read (e.legajo);
        read (e.ID);
    end;
end;

procedure cargarArbol(var a: arbol; e: egresado);
begin
    if (a = nil) then begin
        new (a);
        a^.dato := e;
        a^.HD := nil;
        a^.HI := nil;
    end;
    else
        if (e.legajo >= a^.dato.legajo) then cargarArbol (a^.HD,e);
        else cargarArbol (a^.HI,e);

end;

procedure almacenarEgresados (var a: arbol);
var  
    e: egresado;
begin
    leerEgresado (e);
    while (e.prom > 0) do begin
        cargarArbol (a,e);
        leerEgresado (e);
    end;
end;

procedure cargarArbolFacultad(var a: arbol; e: egresado);
begin
        if (a = nil) then begin
        new (a);
        a^.dato := e;
        a^.HD := nil;
        a^.HI := nil;
    end;
    else
        if (e.prom >= a^.dato.prom) then cargarArbolFacultad (a^.HD,e);
        else cargarArbolFacultad (a^.HI,e);
end;

procedure arbolPorFacultad(a: arbol; var v: vector);
begin
    if (a <> nil) then begin
        cargarArbolFacultad (v[a^.dato.ID],a^.dato);
        arbolPorFacultad (a^.HI,v);
        arbolPorFacultad (a^.HD,v);
    end;
end;

function buscarMax(a: arbol) string;
begin
    if (a^.HD <> nil) then begin
        buscarMax := buscarMax (a^.HD);
    end;
    else buscarMax := a^.dato.nombre;
end;

procedure mejorPromedio (v: vector; ID: integer);
begin
    if v[ID] <> nil then
        write('El mejor promedio de la facultad del ID ingresado es: ', buscarMax(v[ID]))
    else
        writeln('No hay egresados en esa facultad.');
end;



var
    a: arbol;
    v: vector;
    nombreMaxProm: string;
    unID: integer;

begin
    a := nil;
    almacenarEgresados (a);
    cargarArbolFacultad (a,v);
    read (unID);
    mejorPromedio (v,unID);
end.