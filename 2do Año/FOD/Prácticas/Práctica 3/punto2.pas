program punto2p3;

type

asistente = record
num: integer;
apYNom: string [40];
email: string [20];
telefono: integer;
dni: integer;
end;

arc_asistentes = file of asistente;

procedure leerAsistente(var a: asistente);
begin
    writeln('Ingrese un numero del asistente');
    readln(a.num);
    if(a.num <> -1) then
        begin
            writeln('Ingrese el apellido y nombre del asistente');
            readln(a.apYNom);
            writeln('Ingrese el email del asistente');
            readln(a.email);
            writeln('Ingrese el telefono del asistente');
            readln(a.telefono);
            writeln('Ingrese el dni del asistente');
            readln(a.dni);
        end;
end;

procedure crearArchivo(var arc: arc_asistentes);
var
    a: asistente;
    nombre: string;
begin
    writeln('Ingrese el nombre del archivo');
    readln(nombre);
    assign(arc, nombre);
    rewrite(arc);
    leerAsistente(a);
    while(a.num <> -1) do
        begin
            write(arc, a);
            leerAsistente(a);
        end;
    close(arc);
end;

procedure imprimirAsistente(a: asistente);
begin
    writeln('Numero=', a.num, ' Apellido Y Nombre =', a.apYNom, ' Telefono=', a.telefono, ' DNI=', a.dni);
end;

procedure imprimirArchivo(var arc: arc_asistentes);
var
    a: asistente;
begin
    reset(arc);
    while(not eof(arc)) do
        begin
            read(arc, a);
            imprimirAsistente(a);
        end;
    close(arc);
end;

procedure eliminarAsistentes (var arc: arc_asistentes);
var  
    a: asistente;
begin
    rewrite (arc);
    read (arc,a);

    while (not eof (arc)) do begin
      if (a.num < 1000) then begin
        a.apYNom := '!' + a.apYNom;
        seek (arc,filePos(arc)-1);
        write (arc,a);
      end;
      read (arc,a);
    end;

    close (arc);
end;


var
    arc: arc_asistentes;
begin
  crearArchivo (arc);
  writeln('Archivo original:');
  imprimirArchivo(arc);
  eliminarAsistentes (arc);
  writeln('Archivo modificado:');
  imprimirArchivo(arc);
end.
