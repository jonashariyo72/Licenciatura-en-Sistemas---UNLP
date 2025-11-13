program punto7;
const
    valorAlto:= 99999999;
type

regDetalle = record
codLocalidad: integer;
codCepa: integer;
cantCasos: integer;
casosNuevos: integer;
casosRecuperados: integer;
casosFallecidos: integer;
end;

regMaestro = record
codLocalidad: integer;
nombreLocalidad: string;
codCepa: integer;
nombreCepa: string;
cantCasos: integer;
casosNuevos: integer;
casosRecuperados: integer;
casosFallecidos: integer;
end;

maestro = file of regMaestro;
detalle = file of regDetalle;

vectorDetalles = array [1..10] of detalle;
vectorRegistros = array [1..10] of regDetalle;

procedure leer (var archivo: detalle; var dato: regDetalle);
begin
if (not eof(archivo)) then read (archivo,dato)
else dato.cod := valoralto;
end;

procedure minimo(var v: vectorDetalles; var vR: vectorRegistros var min: regDetalle);
var 
    i,pos: integer;
begin
    min.codLocalidad := 9999999;
    for i := 1 to 10 do begin
      if (vR[i].codLocalidad < min.codLocalidad) or ((vR[i].codLocalidad < min.codLocalidad) and (vR[i].codCepa < min.codCepa)) then begin
        min := vA[i];
        pos := i;
      end;
    end;
    if(min.cod_usuario <> valoralto) then
        leer(v[pos], vR[pos]);
end;

procedure actualizarMaestro (var mae: maestro; var v: vectorDetalles);
var
    
begin
    
end;