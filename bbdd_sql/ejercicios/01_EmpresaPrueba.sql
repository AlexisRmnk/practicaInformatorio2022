/* https://sites.google.com/view/casos-de-estudio-sql/p%C3%A1gina-principal */ 



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

/*9 */

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

