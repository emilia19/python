

#Escribir una funcion sum() y una función multip() que sumen 
# y multipliquen respectivamente todos los números de una lista.
#Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.


def sum(listado):
    resul=0
    for i in listado:
        resul+=i
    return resul

def multip(listado):
    resul=1
    for i in listado:
        resul*=i
    return resul
    


lista=[1,2,3,4]


print(" La Suma de la lista es: ",sum(lista) ," La multiplicacion  es: ", multip(lista))
