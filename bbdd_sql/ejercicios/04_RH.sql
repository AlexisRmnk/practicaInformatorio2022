/* https://sites.google.com/view/casos-de-estudio-sql/casos */


/*CASO: RH*/

-- 1 En base a la tabla EMPLOYEES, listar datos de quienes tengan un sueldo mayor a 10000.
SELECT * FROM empleado WHERE sueldo > 10000

-- 2 En base a la tabla EMPLOYEES, contar cuántas personas, al aplicar un aumento de 5%, su sueldo supere los 15000.
SELECT COUNT(*) AS [Cantidad de personas que al aplicar un aumento de 5% su sueldo supere los 15000] 
	FROM empleado WHERE empleado.nombre 
	IN (SELECT empleado.nombre FROM empleado WHERE sueldo*1.05 > 15000)

-- 3 Listar los nombres de todos los departamentos.
SELECT d.nombre FROM departamento AS d

-- 4 Listar la cantidad de personas de la tabla EMPLOYEES, que tengan el cargo de Programador. 
--	Y cuantas de estas personas superen el sueldo mínimo en esa categoría.
-- Nota: sueldo minimo 7k
SELECT COUNT(e.nombre) FROM empleado AS e, cargo AS c WHERE e.idcargo = c.idcargo AND c.nombre = 'Programador'

SELECT COUNT(e.nombre) FROM empleado AS e, cargo AS c WHERE e.idcargo = c.idcargo AND c.nombre = 'Programador' 
AND e.sueldo > c.sueldo_min