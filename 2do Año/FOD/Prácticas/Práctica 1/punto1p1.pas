program punto1p1;
type
  archivo = file of integer;

var
  numeros: archivo;
  n: integer;
  arc_fisico: string[12];

begin
  write('Ingresar nombre del archivo: ');
  readln(arc_fisico);  

  assign(numeros, arc_fisico);
  rewrite(numeros);

  writeln('Ingrese un número: ');
  read(n);

  while (n <> 30000) do 
  begin
    write(numeros, n); 
    writeln('Ingrese un número: ');
    read(n);
  end;

  close(numeros);
end.


