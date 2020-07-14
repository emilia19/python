#Que es INDEX (indice) en base de datos, indicar beneficios y desventajas



"""
Indices en BD .- nos sirven para agilizar
                 las consultas a las tablas.



 ventajas .-
 *  evita “escaneos completos de las tablas”, evitamos los siguientes problemas: Sobrecarga de CPU, 
 sobrecarga de disco y concurrencia.
 *  Los índices nos permiten una mayor rápidez en la ejecución de las consultas 
 tipo SELECT lo que sea WHERE.
 *  por último será una ventaja para aquellos campos que no tengan datos duplicados


desventajas .-


*Los índices son una desventaja en aquellas tablas las que se utiliza frecuentemente operaciones de escritura (Insert, Delete, Update),
 esto es porque los índices se actualizan cada vez que se modifica una columna.

*Los índices tambien suponen una desventaja en tablas demasiado pequeñas puesto que no necesitaremos ganar tiempo
en las consultas.

*Tampoco son muy aconsejables cuando pretendemos que la tabla sobre la que se aplica devuelva una gran cantidad de datos en cada consulta.

*hay que tener en cuenta que ocupan espacio y en determinadas ocasiones incluso más espacio que los propios datos.


"""