from random import randint,uniform,random,randrange

#Generar un codigo en python que sume 10 numeros aleatorios de la siguiente forma: los 5 mas bajos y los 5 mas altos
suma1 = 0
suma2 = 0

for i in range(1,6):
     if i<6:
           suma1 += i


for j in range(5,11):
   if j>5:
       suma2 += j
    

total=suma1 + suma2
print('la suma de 10 numeros aleatorios bajos y altos es :', total)  


