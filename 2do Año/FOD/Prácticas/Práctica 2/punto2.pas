program punto2;
type
const
valoralto = 'ZZZZ'
end;

informacion = 1..2;

alumno = record
cod: integer;
apellido: string[20];
nombre: string [20];
cursadas: integer;
finales: integer;
end;

regD = record
cod: integer;
info: informacion; {1 si aprobó la cursada, 2 si aprobó el fina}
end;

maestro = file of alumno;
detalle = file of regD;

procedure leer (var archivo: detalle; var dato: regD);
begin
if (not eof(archivo)) then read (archivo,dato)
else dato.cod := valoralto;
end;

procedure actualizarMaestro (var mae: maestro; var det: detalle);
var
    regM: alumno;
    regD: regD;
    codActual: integer;
begin
    reset (mae); reset (det);
    leer (det,regD);
    while (regD.cod <> valoralto) do begin
        read (mae,regM);
        while (regM.cod <> regD.cod) do read (mae,regM);
        codActual := regD.cod;
        
    end;

end;

var
    mae: maestro;
    det: detalle;
    nombre: string;

begin
    assign (maestro, 'mae');
    assign (detalle, 'det');
end.