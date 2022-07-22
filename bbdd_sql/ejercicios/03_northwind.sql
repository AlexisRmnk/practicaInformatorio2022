/* https://sites.google.com/view/casos-de-estudio-sql/casos */


/*CASO: NORTHWIND*/

-- 1 Una lista de los nombres y apellidos dede la tabla de EMPLOYEES.
SELECT Employees.FirstName AS Nombre, Employees.LastName AS Apellido FROM Employees

-- 2 Una lista de todos los nombres de las ciudades que aparecen en la tabla de EMPLOYEES.-
-- No mostrar 2 veces un mismo nombre de ciudad.
SELECT DISTINCT Employees.City from Employees

-- 3 Una lista de los nombres de productos y precios unitarios de la tabla PRODUCTS.
SELECT ProductName, UnitPrice FROM Products

-- 4 En la tabla EMPLOYEES: una lista de los detalles completos de quienes viven en EE.UU.
SELECT * FROM Employees WHERE Country='USA'

-- 5 A partir de la tabla ORDERS, listar todos los pedidos que tienen un gasto de envio > 50.
SELECT * FROM Orders WHERE Freight>50

-- 6 De la tabla de CUSTOMERS: listar nombre de la empresa de clientes donde el cargo es igual a Owner.
SELECT CompanyName FROM Customers WHERE ContactTitle = 'Owner'

-- 7 A partir de la tabla CUSTOMERS una lista de clientes cuyo nombre comienza con la letra "A”.
SELECT ContactName FROM Customers WHERE ContactName like 'A%'

-- 8 Una lista de los nombres de clientes donde la región no está en blanco.
SELECT ContactName FROM Customers WHERE Region IS NOT NULL

-- 9 Una lista de todos los productos, ordenado por precio unitario (el más barato primero).
SELECT ProductName, UnitPrice FROM Products ORDER BY UnitPrice ASC

-- 10 Una lista de todos los productos, ordenado por precio unitario (el más caro primero).
SELECT ProductName, UnitPrice FROM Products ORDER BY UnitPrice DESC

-- 11 El número total de registros de la tabla EMPLOYEES. 
-- Nombre de la columna de salida "TotalEmpleados"
SELECT COUNT(*) AS TotalEmpleados FROM Employees

-- 12 De la tabla de pedidos, el gasto de envío promedio y el máximo gasto de envío.
SELECT AVG(Freight) AS [Gasto de envio promedio], MAX(Freight) AS [Gasto maximo de envio] FROM Orders
