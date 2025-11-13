program parcialPrimeraFecha2023;
const

type
  producto = record
    codigo: integer;         
    nombre: string[30];
    descripcion: string[50];
    precioCompra: real;
    precioVenta: real;
    ubicacion: string[20];
  end;

  archivo = file of producto;

procedure leerProducto(var p: producto);
begin
    writeln('Ingrese código de producto:');
    readln(p.codigo);
    if existeProducto(p.codigo, arch) then begin
        writeln('El producto ya existe.');
        close(arch);
    end;
    else begin
        writeln('Ingrese nombre:'); readln(p.nombre);
        writeln('Ingrese descripción:'); readln(p.descripcion);
        writeln('Ingrese precio de compra:'); readln(p.precioCompra);
        writeln('Ingrese precio de venta:'); readln(p.precioVenta);
        writeln('Ingrese ubicación:'); readln(p.ubicacion);
    end;
end;
procedure agregarProducto(var arch: archivo);
var
    p,aux,cab: producto;
begin
    reset (arch);
    leerProducto(p);
    if (existeProducto(p.cod,arch)) do begin
        writeln ('El producto ya existe');
    end;
    else begin
        seek (arch,0);
        read (arch,cab); // leo el primer registro, la cabecera

        if (cab.cod = 0) then begin // si es 0, significa que no hay espacio libre y agrego a lo ultimo
            seek(arch, filesize(arch));
            write(arch, p);
        end;
        else begin // si no es 0, tengo que buscar la posicion que está libre
                //me posiciono
                seek(arch,cab.cod*(-1));
                //leo lo que hay y lo guardo en aux
                read(arch,aux);
                //vuelvo uno para atras despues de la lectura
                seek(arch,filepos(arch)-1);
                //escribo el registro nuevo
                write(arch,p);
                //vuelvo a la cabecera
                seek(arch,0);
                //escribo en la cabecera con aux
                write(arch,aux);
        end;
    end;
    close (arch);
end;

procedure quitarProducto(var arch: archivo);
var
    aux,cab: producto;
    cod:integer;
begin
    writeln ('Ingresar un codigo de producto');
    readln (cod);
    if (not existeProducto(cod,arch)) then writeln ('El producto no existe');
    else begin
            reset(a);
            read(a, cab);
            read(a, aux);
            while(aux.codigo <> codigo) do
                read(a, aux);
            seek(a, filepos(a)-1);
            write(a, cab);
            cab.codigo:= (filepos(a)-1)*-1;
            seek(a, 0);
            write(a, cab);
            close(a);
        end
    end;

    close (arch);
end;

var





begin
    
end.