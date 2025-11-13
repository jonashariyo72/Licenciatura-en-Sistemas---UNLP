program punto6;
const 
orden = 4;
type
empleado = record
dni: integer;
legajo: integer;
nombre: integer;
salario: real;
end;

TNodo = record
cantDatos: integer;
datos: array [1..orden-1] of empleado;
hijos: array [1..orden] of integer;
end;

arbol = file of TNodo;
archivoEmpleados = file of empleado;





var


begin
  // preguntar como queda graficado
end.