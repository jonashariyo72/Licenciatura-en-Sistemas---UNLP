program parcial;
const
    vA = 'ZZZZ';
type

municipio = record
nombre: string;
descripcion: string;
cant_habitantes: integer;
extension: integer;
anio: integer;
end;

municipios = file of municipio;

procedure leerMunicipio(var arch: municipios; var m: municipio);
begin
    if (not eof (arch)) then read (arch,m);
    else  m.nombre := vA;
end;

function existeMunicipio(var arch: municipios; nombre: string):boolean;
var
    m: municipio; ok: boolean;
begin
    reset(arch);
    ok := false;
    leerMunicipio (arch,m);
    while (m.nombre <> vA) and (not ok) do begin
        if (m.nombre = nombre) then ok := true;
        leerMunicipio (arch,m);
    end;
    close (arch);
    existeMunicipio := ok;
end;

procedure altaMunicipio(var arch: municipio);
var
    m,cab: municipio;
begin
    leerUnMunicipio (m);
    if (existeMunicipio(arch,m)) then writeln ('El municipio ya existe');
    else
    begin
        reset (arch);
        read (arch,cab);
        if (cab.nombre)
    end;
end;


var



begin


end.