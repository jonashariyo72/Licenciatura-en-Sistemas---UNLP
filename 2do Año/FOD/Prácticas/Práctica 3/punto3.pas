program punto3;
type
novela = record
cod: integer;
genero: string [15];
nombre: string [20];
duracion: integer;
director: string [20];
precio: real;



archivo = file of novela;
end;

procedure leerNovela(var n: novela);
begin
    writeln('Ingrese el codigo de novela');
    readln(n.cod);
    if(n.cod <> -1) then
        begin
            writeln('Ingrese el género de la novela');
            readln(n.genero);
            writeln('Ingrese el nombre de la novela');
            readln(n.novela);
            writeln('Ingrese la duración de la novela');
            readln(n.duracion);
            writeln('Ingrese el director de la novela');
            readln(a.director);
            writeln('Ingrese el precio de la novela');
            readln(a.director);
        end;
end;

procedure crearArchivo (var arc: archivo);
var
    reg: novela;
    nombre: string;
begin
    writeln ('Ingrese el nombre del archivo');
    readln(nombre);
    assign(arc, nombre);
    rewrite(arc);

    reg.cod := 0; write (arc,reg);  
    leerNovela (reg);

    writeln ('La lectura terminará con el código de novela -1');
    while (reg.cod <> -1) do begin
        write (arc,reg);
        leerNovela (reg);
    end;
    close (arc);
end;

procedure darDeAlta (var arc: archivo);
var
    reg,n: novela;
    
begin
    writeln ('Ingresar los datos de la novela a dar de alta');
    leerNovela (reg);
    seek (arc,filePos(0))
    read (arc,n)
    if (n.cod <> 0) then begin
        seek (arc,n.cod * -1);
        read (arc,n);
        seek (arc,filePos(arc)-1);
        write (arc,reg);
        seek (arc,0);
        write (arc,n);
    end;
    else begin
        writeln ('No hay espacio libre para dar de alta');
        seek (arc,fileSize (arc));
        write (arc,reg);
    end;
    close (arc);
end;

procedure modificarDatos (var arc: archivo);
var
    genero: string;
    nombre: string;
    duracion: integer;
    director: string;
    precio: real;
    codAModificar: integer;
    ok: boolean;
    n: novela;
    end;
begin
    writeln ('Ingresar el género para reemplazar');
    readln (genero);
    writeln ('Ingresar el nombre para reemplazar');
    readln (nombre);
    writeln ('Ingresar la duración para reemplazar');
    readln (duracion);
    writeln ('Ingresar el director para reemplazar');
    readln (director);
    writeln ('Ingresar el precio para reemplazar');
    readln (precio);


    writeln ('INGRESE EL CÓDIGO A MODIFICAR');
    readln (codAModificar);
    reset (arc);
    ok := false;
    while ((not eof(arc)) and (ok = false)) do begin
        read (arc,n);
        if (n.cod = codAModificar) then begin
          n.genero := genero;
          n.nombre := nombre;
          n.duracion := duracion;
          n.director := director;
          n.precio := precio;
          seek (arc,filePos(arc)-1);
          write (arc,n);
          ok := true;
        end;
    end;
    close (arc);
    if (ok) then writeln ('Se modificó el archivo');
    else ('No se encontró el archivo con el código ingresado');
end;

procedure darDeBaja (var arc: archivo);
var
    n,aux: novela;
    codABorrar: integer;
begin
    reset (arc);
    writeln ('INGRESE EL CÓDIGO A BORRAR');
    readln (codABorrar);
    ok := false;
    while ((not eof(arc)) and (ok = false)) do begin
        read (arc,n);
        if (n.cod = codAModificar) then begin
          aux.cod := filePos(arc) * -1;
          seek (arc,0);
          read (arc,n);
          write (arc,aux);
          seek (arc,aux.cod * - 1)
          write (arc,n);
          ok := true;
        end;
    end;
    close (arc);
    if (ok) then writeln ('Se modificó el archivo');
    else ('No se encontró el archivo con el código ingresado');
end;


var
    arc: archivo;

begin


end.