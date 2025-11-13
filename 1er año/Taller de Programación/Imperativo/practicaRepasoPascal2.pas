program punto2Repaso;

type
anio = 2010..2018;

auto = record
patente: integer;
anioFab: anio;
marca: string;
modelo: integer;

arbol = ^nodo;
nodo = record
dato: auto;
HI: arbol;
HD: arbol;
end;

lista = ^nodo2;
nodo2 = record
dato: auto;
sig: lista;
end;

arbolPatente = ^nodo3;
nodo = record
dato: lista;
HI: arbol;
HD: arbol;
end;


procedure agregarAlArbol(var a: arbol; au: auto);
begin
    if (a = nil) then begin
        new (a);
        a^.dato := au;
        a^.HD := nil;
        a^.HI := nil;
    end;
    else
        if (au.patente > a^.dato.patente) then cargarArbol (a^.HD,au);
        else cargarArbol (a^.HI,au);

end;

procedure agregarALista(var l: lista; au: auto);
var
    aux: lista;
begin
    new(aux);
    aux^.sig:= l;
    aux^.dato:= au;
    l:= aux;
end;

procedure agregarAlArbolPatente(var aP: arbolPatente; au: auto);
begin
    if (a = nil) then begin 
        new(a);  
        aP^.dato := nil; 
        agregarALista(aP^.dato,au);
        aP^.HI:=nil; 
        aP^.HD:=nil; 
   end 
   else 
     if (a^.dato.marca = au.marca) then 
       agregarALista(a^.dato,au) 
     else 
       if (au.marca < a^.dato.marca) then 
         agregarAlArbolDeListas(aP^.HI,au) 
       else 
         agregarAlArbolDeListas(aP^.HD,au) 
end; 

procedure cargarArboles (var a: arbol; var aP: arbolPatente);
var
    au: auto;
begin
    leerAuto (e);
    while (au.marca <> 'MMM') do begin
        agregarAlArbol (a,au);
        agregarAlArbolPatente (aP,au);
        leerEgresado (au);
    end;
end;

procedure leerAuto(var au: auto);
begin
    read (au.marca);
    if (au.marca <> 'MMM') then
        read (au.patente);
        read (au.anio);
        read (au.modelo)
    end;
end;

procedure cantPorMarca(a: arbol; unaMarca: string; var cant: integer);
begin
    if (a <> nil) then begin
        if (a^.dato.marca = unaMarca) then cant := cant + 1;
        cantPorMarca (a^.HD, unaMarca,cant);
        cantPorMarca (a^.HI, unaMarca,cant);
    end;
end;

procedure contarEnLista(l: lista; var cant2: integer);
begin
    while (l <> nil) do begin
      cant2 := cant2 + 1;
      l := l^.sig;
    end;
end;

procedure cantPorMarca2 (aP: arbolPatente; unaMarca: string; var cant2: integer);
begin
    if (aP <> nil) then begin
      if (aP^.marca = unaMarca) then contarEnLista (aP^.dato,cant2);
      else
        if (unaMarca > aP^.marca) then cantPorMarca (aP^.HD,unaMarca,cant2);
        else cantPorMarca (aP^.HD,unaMarca,cant2);
    end;
end;

var
    a: arbol;
    aP: arbolPatente;
    cant: integer;
    unaMarca: string;
begin
    a := nil;
    aP := nil;
    cargarArboles (a,aP);
    cant := 0;
    writeln ('Ingrese una marca: ');
    read (unaMarca);
    cantPorMarca (a,unaMarca,cant);
end.