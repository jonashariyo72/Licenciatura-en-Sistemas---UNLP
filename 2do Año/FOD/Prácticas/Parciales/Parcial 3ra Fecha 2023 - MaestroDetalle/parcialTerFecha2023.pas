program parcial1;
const
    valoralto := 99999999999999999;
type
regDetalle = record
cod: integer;
cantVendida: integer;
end;

regMaestro = record
cod: integer;
nombre: string;
precio: real;
stockActual: integer;
stockMinimo: integer;
end;

maestro = file of regMaestro;
detalle = file of regDetalle;


vectorDetalles = array [1..20] of detalle;
detalleActual = array [1..20] of regDetalle;

procedure leer (var archivo: detalle; var dato: regDetalle);
begin
if (not eof(archivo)) then read (archivo,dato)
else dato.cod := valoralto;
end;

procedure minimo(var v: vectorDetalles; var vA: detalleActual var min: regDetalle);
var 
    i,pos: integer;
begin
    min.codigo := 9999999999999999;
    for i := 1 to 20 do begin
      if (vA[i].codigo < min.codigo) then begin
        min.codigo := vA[i].codigo;
        pos := i;
      end;
    end;
    if(min.codigo <> valoralto) then
        leer(v[pos], vA[pos]);
end;

procedure actualizarMaestro (var mae: maestro; var v: vectorDetalles; var txt: TEXT);
var
    cant,i: integer;
    regM: regMaestro;
    vector: detalleActual;
    min: regDetalle;
    montoTotal: real;
begin
    assign(txt, 'archivoTexto');
    rewrite (txt);
    for i := 1 to 20 do begin
      reset (v[i]);
      leer (v[i],vector[i]);
    end;

    reset (mae);

    minimo (v,vector,min);

    while (min.cod <> valorAlto) do begin
        read (mae,regM);
        while (min.cod <> regM.cod) do begin
            read (mae,regM);
        end;


        cant := 0;
        while (min.cod = regM.cod) do begin
            cant := cant + min.cantidad;
            minimo(dets, regs, min);
        end;

        montoTotal := totalVendida * regM.precio;  // preguntar si me quedo con el registro correspondiente

        seek(mae, filepos(mae)-1);
        regM.stockActual:= regM.stockActual - cant;
        write(mae, regM);

        if(montoTotal > 10000) then
            writeln(txt, infoMae.codigo, ' ', precioActual:0:2, ' ', infoMae.stockActual, ' ', infoMae.stockMinimo, infoMae.nombre);
        end;
    end;

    for i := 1 to 20 do
        close(v[i]);
    close(mae);
    close(txt);
end;

var



begin
    
end.