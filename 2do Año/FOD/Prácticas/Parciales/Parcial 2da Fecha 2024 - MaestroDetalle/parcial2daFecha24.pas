program dengue;
const
DF = 30;
VA = 999999999999;

type

municipio = record
cod: integer;
nombre: string;
casos_totales: integer;
end;

regDetalle = record
cod: integer;
cant_casos: integer;
end;

maestro = file of municipio;
detalle = file of regDetalle;

vecDetalles = array [1..DF] of detalle;
vecRegistros = array [1..DF] of regDetalle;

procedure leerMaestro(var mae: maestro; var dato: municipio);
begin
    if (not eof(mae)) then read (mae,dato)
    else dato.cod := VA;
end;


procedure leerDetalle(var det: detalle; var dato: regDetalle);
begin
    if (not eof(det)) then read (det,dato)
    else dato.cod := VA;
end;

procedure minimo(var vD: vecDetalles; var vR: vecRegistros; var min: regDetalle );
var
    i,pos: integer;
begin
    min.cod := valorAlto;
    for i := 1 to N do
        if (vR[i].cod < min.cod) then begin
            min := vR[i];
            pos := i;
        end;
    if (min.cod <> VA) then
        leerDetalle(vD[pos], vR[pos]);
end;

procedure informarMunicipio(var dato: municipio);
begin
    writeln ('Nombre del municipio: ', dato.nombre);
    writeln ('Código del municipio: ', dato.cod);
end;

procedure actualizarMaestro(var mae: maestro; var vD: vecDetalles);
var
    total,i: integer;
    min: regDetalle;
    regM: municipio;
    vR: vecRegistros;
begin
    for i := 1 to DF do begin
        reset(vD[i]);
        leer (vD[i],vR[i])
    end;
    reset (mae);
    leerMaestro(mae,regM);
    minimo (vD,vR,min);
    while (regM.cod <>valorAlto) do begin
        
        total := 0
        
        while (min.cod = regM.cod) do begin
            total := total + min.cant_casos;
            minimo (vD,vR,min);
        end;
        
        regM.casos_totales := regM.casos_totales + total;
        
        seek(mae,filepos(mae)-1);
        write(mae,regM);
        
        if (regM.casos_totales > 15) then informarMunicipio(regM);
        leerMaestro(mae,regM);
    end;

    for i := 1 to DF do begin
        close(vD[i]);
    end;
    close (mae);
end;

var 
    mae: maestro;
    vD: vecDetalles;
    nombreMaestro: string;
    nombreDetalle: string;
begin
    writeln ('Ingresar nombre para el archivo maestro');
    readln (nombreMaestro);
    assign (mae,nombreMaestro);
    
    for i := 1 to DF do begin
        writeln ('Ingresar nombre para el archivo detalle número: ', i);
        readln (nombreDetalle);
        assign (vD[i],nombreDetalle);
    end;
    
    actualizarMaestro(mae,vD);
end.