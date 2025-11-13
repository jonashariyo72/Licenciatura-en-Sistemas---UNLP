program ejercicio1;
type
    archivo = file of integer;
procedure agregarNumeros(var arc: archivo);
var
    nro: integer;
begin
    writeln('Ingrese un numero de teclado');
    readln(nro);
    while(nro <> 30000) do
        begin
            write(arc, nro);
            readln(nro);
        end;
    close(arc);
end;
var
    nombre: string[15];
    arc: archivo;
begin
    writeln('Ingrese un nombre de archivo');
    readln(nombre);
    assign(arc, nombre);
    rewrite(arc);
   agregarNumeros(arc);
end.
