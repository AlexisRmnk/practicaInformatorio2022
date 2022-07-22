/* https://sites.google.com/view/casos-de-estudio-sql/p%C3%A1gina-principal */ 

-- consultas auxiliares
select * from producto
select * from fabricante

/* https://sites.google.com/view/casos-de-estudio-sql/casos */
/*CASO: EMPRESA DE PRUEBA*/

/*1 Lista el nombre de todos los productos que hay en la tabla producto.*/
SELECT nombre FROM producto 

/*2 Lista todas las columnas de la tabla producto.*/
SELECT * FROM producto

/*3 Lista el nombre de los productos y el precio en USD.*/
SELECT nombre, precio FROM producto

/*4 Lista los nombres y los precios de todos los productos de la tabla producto, convirtiendo los nombres a mayúscula. */
SELECT UPPER(nombre) AS nombre, precio FROM producto

/*5 Lista los nombres y los precios de todos los productos de la tabla producto, redondeando el valor del precio.*/
SELECT nombre, ROUND(precio,0) FROM producto

SELECT * from fabricante, producto

/*6 Lista el código de los fabricantes que tienen productos en la tabla producto.*/
SELECT * from fabricante, producto 
where fabricante.codigo = producto.codigo_fabricante

SELECT * from fabricante, producto 
where fabricante.codigo = producto.codigo_fabricante 
ORDER BY fabricante.codigo

/*Lista el código de los fabricantes que tienen productos en la tabla producto, eliminando los códigos que aparecen repetidos*/
/*7*/ -- SELECT Distinct producto.codigo_fabricante from fabricante, producto where fabricante.codigo = producto.codigo_fabricante
SELECT DISTINCT codigo_fabricante from producto

/*8 Lista los nombres de los fabricantes ordenados de forma ascendente.*/
SELECT nombre from fabricante 
order by nombre

-- 9 Lista los nombres de los productos ordenados en primer lugar por el nombre de forma ascendente y en segundo lugar
-- por el precio de forma descendente.
SELECT producto.nombre, producto.precio from producto
order by nombre asc, precio desc

-- 10  Devuelve una lista con las 5 primeras filas de la tabla fabricante.
SELECT TOP 5 * FROM fabricante

-- 11 Lista el nombre de todos los productos del fabricante cuyo código de fabricante es igual a 2
SELECT * from producto where producto.codigo_fabricante = 2

/*12 Lista el nombre de los productos que tienen un precio menor o igual a 120USD */
select nombre from producto 
where producto.precio <= 120

/* 13 Devuelve todos los productos del fabricante Lenovo. (Sin utilizar INNER JOIN). */
SELECT * from fabricante, producto 
where fabricante.codigo = producto.codigo_fabricante AND fabricante.nombre like 'Lenovo'

select nombre from producto 
where codigo_fabricante = (select codigo from fabricante where nombre = 'Lenovo') -- forma con subconsulta, es la mas ineficiente!

SELECT * from fabricante, producto 
where fabricante.codigo = producto.codigo_fabricante AND fabricante.nombre = 'lenoVo' -- se puede usar sin like!

-- con inner join: antes de hacer el producto cartesiano ya filtra
-- es mas eficiente!!
select producto.nombre, fabricante.nombre from producto 
inner join fabricante on fabricante.codigo = producto.codigo_fabricante 
where fabricante.nombre = 'lenovo'

/* de clase:

select * from producto, fabricante 
where fabricante.nombre = 'lenovo' and fabricante.codigo = producto.codigo_fabricante

select * from producto 
inner join fabricante on fabricante.codigo = producto.codigo_fabricante 
where fabricante.nombre = 'lenovo'

select nombre from producto 
where codigo_fabricante = (select codigo from fabricante where nombre = 'Lenovo')
*/

-- 14 Devuelve todos los datos de los productos que tienen el mismo precio que el producto más caro del 
-- fabricante Lenovo. (Sin utilizar INNER JOIN).
SELECT * FROM producto 
WHERE producto.precio = 
	(SELECT MAX(producto.precio) FROM producto, fabricante 
	WHERE producto.codigo_fabricante = fabricante.codigo AND fabricante.nombre = 'Lenovo')


--auxiliar
	SELECT producto.codigo, producto.codigo_fabricante, producto.nombre, producto.precio,
	fabricante.codigo, fabricante.nombre
	FROM producto, fabricante 
	WHERE producto.codigo_fabricante = fabricante.codigo AND fabricante.nombre = 'Lenovo'

-- 15 Lista el nombre del producto más caro del fabricante Lenovo.
SELECT DISTINCT producto.nombre FROM producto, fabricante where producto.precio = 
(SELECT max(producto.precio) FROM producto where producto.codigo_fabricante = fabricante.codigo
AND fabricante.nombre = 'lenovo' )


-- 16 Devuelve los nombres de los fabricantes que tienen productos asociados. (Utilizando ALL o ANY).
SELECT fabricante.nombre FROM fabricante WHERE fabricante.codigo = ANY (
SELECT producto.codigo_fabricante FROM producto)