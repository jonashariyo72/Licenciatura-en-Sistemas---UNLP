program punto5;
const
    valoralto := 99999999999999999;



type

producto =  record
cod: integer;
nombre: string;
precio: real;
descripcion: string;
stockActual: integer;
stockMinimo: integer;
end;

regDetalle = record
cod: integer;
cantVendida: integer;
end;

regTexto = record
nombre: string;
descripcion: string;
stock: integer;
precio: real;
end;


detalle = file of regDetalle;

maestro = file of producto;

vectorDetalles = array [1..30] of detalle;
detalleActual = array [1..30] of regDetalle;

var

procedure leer (var archivo: detalle; var dato: regDetalle);
begin
if (not eof(archivo)) then read (archivo,dato)
else dato.cod := valoralto;
end;

procedure minimo(var v: vectorDetalles; var vA: detalleActual var min: regDetalle);
var 
    i,pos: integer;
begin
    min.codigo := 999999;
    for i := 1 to 30 do begin
      if (vA[i].codigo < min.codigo) then begin
        min.codigo := vA[i].codigo;
        pos := i;
      end;
    end;
    if(min.codigo <> valoralto) then
        leer(v[pos], vA[pos]);
end;

procedure actualizarMaestro (var mae: maestro; var v: vectorDetalles);
var
    i,cant,codActual: integer;
    regM: regMaestro;
    vector: detalleActual;
    min: regDetalle;
begin
    assign(mae, 'ArcMaestro');
    rewrite (mae);
    for i := 1 to 5 do begin
      reset (v[i]);
      leer (v[i],vector[i]);
    end;

    minimo (v,vector,min);

    while (min.codigo <> valorAlto) do begin
      cant := 0;
      codActual := min.codigo;

      while (min.codigo = codActual) do begin
            cant:= cant + min.cant;
            minimo(vec, vecReg, min);
      end;

      read (mae,p);
      while (p.codigo <> codActual) do begin
        read (mae,p);
      end;

        seek(mae, filepos(mae)-1);
        p.stockActual:= p.stockActual - cant;
        write(mae, p);
    end;


    informarProd (mae); // preguntar si el archivo maestro hay que volverlo a resetear, cambiar con el seek, o como hacer
    
    close (mae);

    for i := 1 to 30 do begin
      close (v[i]);
    end;
end;



begin
  
end.
