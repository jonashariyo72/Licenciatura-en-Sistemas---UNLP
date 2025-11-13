program punto6;
const
valorAlto := 9999999;

type

regDetalle = record
cod_usuario: integer;
fecha: integer;
tiempo_sesion: integer;
end;

regMaestro = record
cod_usuario: integer;
fecha: integer;
tiempo_total_de_sesiones_abiertas: integer;
end;

maestro = file of regMaestro;
detalle = file of regDetalle;


vectorDetalles = array [1..5] of detalle;
detalleActual = array [1..5] of regDetalle;

procedure leer (var archivo: detalle; var dato: regDetalle);
begin
if (not eof(archivo)) then read (archivo,dato)
else dato.cod := valoralto;
end;

procedure minimo(var v: vectorDetalles; var vA: detalleActual var min: regDetalle);
var 
    i,pos: integer;
begin
    min.cod_usuario := 9999999;
    for i := 1 to 30 do begin
      if (vA[i].cod_usuario < min.cod_usuario) then begin
        min.cod_usuario := vA[i].cod_usuario;
        pos := i;
      end;
    end;
    if(min.cod_usuario <> valoralto) then
        leer(v[pos], vA[pos]);
end;

