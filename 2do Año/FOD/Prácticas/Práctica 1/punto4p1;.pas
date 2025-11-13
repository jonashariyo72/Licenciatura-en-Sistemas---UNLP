program punto4p1;
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
    writeln ('numero: ');
    readln (e.num);
    writeln ('nombre: ');
    readln (e.nombre);
    writeln ('edad: ');
    readln (e.edad);
    writeln ('dni: ');
    readln(e.dni);
end;

procedure leer (var arc_emple: archivo; var dato: empleado);
begin
    if (not eof(arc_emple)) then read (arc_emple,dato)
    else dato.edad := 999999999;
end;

procedure agregarEmpleadoAlFinal (var arc_emple: archivo);
var
    e, emp: empleado; ok: boolean;
begin
    ok := false;
    reset (arc_emple);
    leerEmpleado(e);
    while (not eof (arc_emple)) do begin
        read(arc_emple,emp);
        if (emp.num = e.num) then ok := true;
    end;
    if (ok = false) then write (arc_emple,e);
    close (arc_emple);
end;

procedure modificarEdad (var arc_emple: archivo; e: empleado; edad: integer);
var
    emp: empleado; ok: false;
begin
        ok := false;
        reset (arc_emple);
        while (not eof (arc_emple)) and (ok = false) do begin
        read(arc_emple,emp);
        if (emp.num = e.num) then begin
            ok := true;
            emp.edad := edad;
            seek (arc_emple, filepos(arc_emple)-1);
            write (arc_emple,emp);
        end; 
        close (arc_emple);
    end;
end;

procedure exportarArchivo (var arc_emple: archivo, var archivoTexto: Text);
var  
    emp: empleado;
begin
    assign (archivoTexto,“todos_empleados.txt”);
    reset (arc_emple);
    rewrite (archivoTexto);
    while (not eof(arc_emple)) do begin
        read(arc_emple, emp); 
        writeln (archivoTexto, emp.num ,' ', emp.nombre, ' ' , emp.apellido ,' ', emp.edad , ' ' , emp.dni); 
    end;
      close(arc_emple) ; close(archivoTexto);
    end;

end;

procedure exportarArchivo (var arc_emple: archivo, var archivoDNI: Text);
var  
    emp: empleado;
begin
    assign (archivoDNI,'faltaDNIEmpleado.txt');
    reset (arc_emple);
    rewrite (archivoDNI);
    while (not eof(arc_emple)) do begin
        read(arc_emple, emp); 
        if (emp.dni = 00) then writeln (archivoDNI, emp.num ,' ', emp.nombre, ' ' , emp.apellido ,' ', emp.edad , ' ' , emp.dni); 
    end;
      close(arc_emple) ; close(archivoDNI);
    end;

end;






var

    arc_emple: archivo;
    arc_fisico: string[12];  //preguntar
    e: empleado;
    unNombre: string;
    unApellido: string;
    valorAlto : integer;
    archivoTexto: Text;
    archivoDNI: Text;
end;

begin
    





end.