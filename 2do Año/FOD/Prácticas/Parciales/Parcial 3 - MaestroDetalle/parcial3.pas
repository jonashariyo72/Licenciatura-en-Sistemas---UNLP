program parcial3;
const
    DF = 25;
    valorAlto = 99999999999999999;
type
    producto = record;
    cod: integer;
    desc: string;
    cant: integer;
    stockMinimo: integer;
    precio: real;
    end;

    venta = record;
    num: integer;
    cod: integer;
    cantVendidas: integer;
    end;

    maestro = file of producto;
    detalle = file of venta;

    vectorDet = array [1..DF] of detalle;
    vectorVentas = array [1..DF] of venta;

end;

procedure leer(var det: detalle; var v: venta);
begin
    if (not eof(det)) then
        read(det, v);
    else
        v.cod := valorAlto;
end;


procedure minimo(var vDet: vectorDet; var vVen: vectorVentas; var min: venta );
begin
var
  i, pos: integer;
begin
  min.cod := valorAlto;
  for i := 1 to N do
    if (vVen[i].cod < min.cod) then
    begin
      min := vVen[i];
      pos := i;
    end;
  if (min.cod <> valorAlto) then
    leer(vDet[pos], vVen[pos]);
end;
end;



procedure actualizarMaestro (var mae: maestro; var vDet: vectorDet);
var
    cant: integer; 
    monto,total: real; 
    p: producto;
    v: venta;
    vD:vectorVentas;
begin
    


end;