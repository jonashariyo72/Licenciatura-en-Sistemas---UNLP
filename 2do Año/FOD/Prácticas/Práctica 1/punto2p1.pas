program punto2p1;
type
  archivo = file of integer;

var
  numeros: archivo;
  n: integer;
  arc_fisico: string[12];
  total: integer;
  cant: integer;

begin
    assign (numeros,arc_fisico);
    total := 0;
    
    reset (numeros);
    while (not eof(numeros)) do begin
        read (numeros,n);
        writeln (n);
        total := total + n;
        if (n > 1500) then cant := cant + 1;
    end;
    close (numeros);

    writeln ('El promedio del archivo es de: ', total/filesize(numeros));
    writeln ('La cantidad de numeros mayores a 1500 es: ', cant);
end.
