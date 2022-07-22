/* https://sites.google.com/view/casos-de-estudio-sql/casos */


/*CASO: UNIVERSIDAD*/

-- 1 Lista las asignaturas del tipo "optativa".
SELECT asignatura.nombre FROM asignatura WHERE asignatura.tipo = 'Optativa'

-- 2 Lista los nombres de Departamento de la Universidad.
SELECT departamento.nombre FROM departamento

-- 3 Listar apellidos y nombre de las Personas, convirtiendo ambos elementos a mayúsculas

SELECT UPPER(CONCAT(persona.apellido1, ' ', persona.apellido2)) AS APELLIDOS,
UPPER(persona.nombre) AS NOMBRE
FROM persona

-- 4 Listar  apellidos y nombres de Profesores mayores a 40 años en la Universidad.

SELECT CONCAT(persona.apellido1, ' ', persona.apellido2) AS APELLIDOS,
persona.nombre AS NOMBRE, ABS(YEAR(fecha_nacimiento) - YEAR(GETDATE())) AS EDAD
FROM persona WHERE ABS(YEAR(fecha_nacimiento) - YEAR(GETDATE())) > 40