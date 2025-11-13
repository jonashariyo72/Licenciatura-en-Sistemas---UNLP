program punto4;
const
    valoralto := 99999999999999999;
end;

type
    dataAlf = record
    nombreProv: string;
    cantAlfabetizados: integer;
    totalEncuestados: integer;
    end;

    dataCenso = record
    nombreProv: string;
    codLocalidad: integer;
    cantAlfabetizados: integer;
    totalEncuestados: integer;
    end;

    maestro = file of dataAlf;
    detalle1 = file of dataCenso;
    detalle2 = file of dataCenso;

procedure leer (var archivo: detalle; var dato: regD);
begin
if (not eof(archivo)) then read (archivo,dato)
else dato.cod := valoralto;
end;












end;

var




begin
    
end.