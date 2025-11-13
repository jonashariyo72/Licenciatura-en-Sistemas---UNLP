program prac1ejer5y6;

celular = record
cod: integer;
nombre: string [10];
desc: string[20];
marca: string;
precio: real;
stockMin: integer
stockDispo: integer;

archivo = file of celular;

procedure crearArchivoBinario(var arch: archivo; var texto: Text);
var
    nombre: string; c: celular;
begin
    writeln ('Ingresar un nombre de archivo: ');
    readln (nombre);
    assign (archivo, texto);
    rewrite (arch);
    reset (texto);
    while (not eof(texto)) do begin
        read (c.cod, c.precio, c.marca);  
        read (c.stockDispo,c.stockMin, c.desc);
        read (c.nombre);
        write (arch,c); 
    end;
    close (arch); close (texto);
end;

procedure imprimirCelular(c:celular);
begin
    writeln (c.cod);
    writeln (c.marca);
    writeln (c.precio) ;
    writeln (c.stockMin) ;
    writeln (c.stockDispo) ;
    writeln (c.nombre);
    writeln (c.desc);
    writeln (c.marca);
end;

procedure stockMinimo(var arch: archivo);
var
    c: celular;
begin
    reset (arch);
    while (not eof(arch)) do begin
        if (c.stockDispo < c.stockMin) then imprimirCelular(c);
    end;
    close(arch);
end;

procedure cadenaDeCaracteres (var arch: archivo);
var
    cadena: string; c: celular;
begin
    writeln ('Ingrese un string para comparar: ');
    read (cadena);
    while (not eof(arch)) do begin
        if (c.desc = cadena ) then imprimirCelular(c);
    end;
    close (arch);
end;

procedure exportarBinarioATexto(var arch: archivo; var texto: Text);
var
    c: celular;
begin
    reset (arch); rewrite (texto);
    while (not eof (texto)) do begin
        read (arch, c);
        write (texto, c.cod, ' ', c.precio, ' ', c.marca, ' ');  
        write (texto, c.stockDispo, ' ' , c.stockMin, ' ' c.desc, ' ');
        write (texto, c.nombre, ' ');
    end;
    close (arch); close (texto);
end;

procedure leerCelular(var c: celular);
begin
    writeln('Ingrese el codigo del celular');
    readln(c.codigo);
    if(c.codigo <> 0) then
        begin
            writeln('Ingrese el nombre del celular');
            readln(c.nombre);
            writeln('Ingrese la descripcion del celular'); //Dejar un espacio para que se guarde bien el celular agregado
            readln(c.descripcion);
            writeln('Ingrese la marca del celular');
            readln(c.marca);
            writeln('Ingrese el precio del celular');
            readln(c.precio);
            writeln('Ingrese el stock minimo del celular');
            readln(c.stockMin);
            writeln('Ingrese el stock del celular');
            readln(c.stock);
        end;
end;

procedure modificarStock(var arch: archivo; cod: integer; stockNuevo: integer);
var
    c: celular; ok: boolean;
begin
    reset (arch);
    ok := false;
    while (not eof (arch)) and (not ok) do begin
        read (arch, c);
        if (c.cod = cod) then begin
            ok := true;
            seek(arc, filepos(arc)-1);
            c.stockDispo := stockNuevo;
            write(arc, c);
        end;
    end;
    close (arch);
end;

procedure añadirCelular (var arch: archivo);
var
    c: celular;
begin
    reset (arch);
    leerCelular (c);
    seek(arch, filesize(arch));
    while (c.codigo <> 0) do begin
        write (arch,c);
        leerCelular (c);
    end;
    close (arch);
end;

procedure exportarSinStock (var );
var
    c: celular;
begin
    reset (arch);
    rewrite (sinStock);
    while (not eof (arch)) do begin
        read (arch, c)
        if (c.stockDispo = 0) then begin
            write (sinStock, c.cod, ' ', c.precio, ' ', c.marca, ' ');  
            write (sinStock, c.stockDispo, ' ' , c.stockMin, ' ' c.desc, ' ');
            write (sinStock, c.nombre, ' ');
        end;
    end;
    close (arch); close (sinStock);
end;

var
    arch: archivo;
    texto: Text;
    sinStock: Text;
begin
    assign (texto, 'celulares.txt');
    crearArchivoBinario (arch,texto);
    stockMinimo (arch);
    cadenaDeCaracteres (arch);
    exportarBinarioATexto (arch,texto);
    añadirCelular (arch);
    modificarStock(arch);
    assign (sinStock, 'sinStock.txt')
    exportarSinStock (arch, sinStock);
end.