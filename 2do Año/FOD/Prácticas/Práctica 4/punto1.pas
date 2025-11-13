program punto1;
const
M = 0;
type


alumno = record
nombreYAP: string[50];
dni: integer;
legajo: integer;
anio: integer;
end;

TNodo = record
cantDatos: integer;
datos: array [1..M-1] of alumno;
hijos: array [1..M] of integer;
end;

arbol = file of TNodo;
var
arbolAlumnos: arbol;

begin
  
end.