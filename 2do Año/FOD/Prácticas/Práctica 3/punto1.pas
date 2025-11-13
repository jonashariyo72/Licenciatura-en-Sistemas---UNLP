program punto1p3;
type

empleado = record
num: integer;
nombre: string[20];
apellido: string[20];
edad: integer;
dni: integer;
end;

archivo = file of empleado;

procedure leerEmpleado(var e: empleado);
begin
    writeln ('apellido: ');
    readln (e.apellido);
    if (e.apellido <> 'fin') then begin
        writeln ('numero: ');
        readln (e.num);
        writeln ('nombre: ');
        readln (e.nombre);
        writeln ('edad: ');
        readln (e.edad);
        writeln ('dni: ');
        readln(e.dni);
    end;
end;

procedure leer (var arc_emple: archivo; var dato: empleado);
begin
    if (not eof(arc_emple)) then read (arc_emple,dato)
    else dato.edad := 999999999;
end;

procedure realizarBajas (var arc_emple: archivo);
var
    cod: integer;
    e, unEmpleado: empleado;
begin
    reset (arc_emple);
    writeln ('Ingresar un codigo a borrar: ');
    readln (cod);
    seek (arc_emple,fileSize(arc_emple)-1)
    read (arc_emple,unEmpleado);

    seek (arc_emple,0);
    read (arc_emple,e);
    while ((not eof(arc_emple)) and (e.codigo <> cod)) do begin
      read (arc_emple,e);
    end;
    if (e.codigo = cod) then begin
        seek (arc_emple,filePos(arc_emple)-1);
        write (arc_emple,unEmpleado);
        seek(arc_emple, fileSize(arc_emple)-1);
        truncate(arc_emple);
    end
    else writeln ('No se encontró el codigo ingresado');
    close (arc_emple);
end;


var

    arc_emple: archivo;
    arc_fisico: string[12];  //preguntar
    e: empleado;
    unNombre: string;
    unApellido: string;
    valorAlto : integer;
end;


begin
    write('Ingresar nombre del archivo: ');
    readln(arc_fisico);  

    assign (arc_emple,arc_fisico);
    rewrite (arc_emple);

    leerEmpleado (e);
    while (e.apellido <> 'fin') do begin
        write (arc_emple,e);
        leerEmpleado (e);
    end;

    close (arc_emple); // hasta acá el punto a)

    write('Ingresar un nombre: ');
    readln(unNombre);  

    write('Ingresar un apellido: ');
    readln(unApellido);  
    
    valorAlto := 999999999;

    reset (arc_emple);
    leer (arc_emple,e);

    while (e.edad <> valorAlto) do begin
        write (arc_emple,e);
        if ((e.nombre = unNombre) or (e.apellido = unApellido)) then writeln (e.nombre,e.apellido);
        leer (arc_emple,e);
    end;

    close (arc_emple); // hasta acá el punto b)i)

    reset (arc_emple);

    while (not eof (arc_emple)) do begin
        read (arc_emple,e);
        write (e.nombre);
    end;                        

    close (arc_emple); // hasta acá el punto b)ii)

end.
