program punto1;

const
    valoralto = 'ZZZZ'
end;
empleado = record
cod: integer;
nombre: string;
montoComision: real;
end;

regEmp = record
cod: integer;
totalMonto:  real;
end;

archivoEmpleados = file of empleado;

comisiones = file of regEmp;

procedure leer (var archivo: detalle; var dato:v_prod);
begin
if (not eof(archivo)) then read (archivo,dato)
else dato.cod := valoralto;
end;

procedure compactar (var archEmp: archivoEmpleados; var com: comisiones);
var
    e: empleado;
    empCom: regEmp;
    codActual: integer;
    total: real;
begin
    reset (archEmp); rewrite (com);
    leer (archEmp,e);
    while (e.cod <> valoralto) do begin
        codActual := e.cod;
        total := 0;
        while (codActual = e.cod) and (e.cod <> valoralto) do begin
            total := total + e.montoComision;
            leer (archEmp,e);
        end;
        empCom.cod := codActual;
        empCom.totalMonto := total;
        write (com,empCom);
    end;
    close (archEmp); close (com);
end;

var
    archEmp: archivoEmpleados;
    com: comisiones;
    nombre: string;

begin
    writeln ('Ingrese un nombre físico para el archivo de empleados: ');
    readln (nombre)
    assign (archEmp, nombre);
    writeln ('Ingrese un nombre físico para el archivo de comisiones: ');
    readln (nombre)
    assign (com, nombre);
end.