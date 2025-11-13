program punto3;

const
    valoralto = 999;
end;
 
type

producto =  record
cod: integer;
nombre: string;
precio: real;
stockActual: integer;
stockMinimo: integer;
end;


venta = record
cod: integer;
cantVentas: integer;
end;


maestro = file of producto;
detalle = file of venta;

procedure leer (var archivo: detalle; var dato: regD);
begin
if (not eof(archivo)) then read (archivo,dato)
else dato.cod := valoralto;
end;

procedure actualizarMaestro (var mae: maestro; var det: detalle);
var
    regM: producto;
    regD: venta;
    codActual: integer;
begin
    reset (mae); reset (det);
    leer (det,regD);
    while (regD.cod <> valoralto) do begin 
        read (mae,regM);
        while (regM.cod <> regD.cod) do read (mae,regM);
        codActual := regD.cod;
        while (regD.cod = codActual) and (regD.cod <> valoralto) do begin
            regM.stockActual := regM.stockActual - regD.cantVentas;
            seek (mae, filepos (mae) - 1);
            write (mae,regM);
            leer (det,regD);
        end;
    end;
    close (mae); close (det);
end;

procedure listarProductos (var mae: maestro; var archivoTexto: Text);
var
    regM: producto
begin
    reset (mae); rewrite (archivoTexto);
    read (mae,regM);
    while (not eof(mae)) do begin
        if (regM.stockActual < regM.stockMinimo) then begin
            write (sinStock, regM.cod, ' ', regM.precio, ' ', regM.stockActual, ' ', regM.stockMinimo, ' ', regM.nombre, ' ');  
        end;
        read (mae,regM);
    end;
    close (mae); close (archivoTexto);
end; 

var
    mae: maestro;
    det: detalle; 
    regM: producto;
    regD: venta;
    nombre: string;
    archivoTexto: Text;

begin
    writeln ('Ingrese un nombre físico para el archivo Maestro: ');
    readln (nombre)
    assign (mae, nombre);
    writeln ('Ingrese un nombre físico para el archivo : ');
    readln (nombre)
    assign (detalle, nombre);
    actualizarMaestro (mae,det);
    assign (archivoTexto, 'stock_minimo.txt');
    listarProductos (mae,archivoTexto);
end.