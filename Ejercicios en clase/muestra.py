import numpy as np
import random as rnd

print("Hola mundo")
a = 1
b = 2
c = a + b
print(c)

array = np.zeros(100)
for i in range(100):
    array[i] = rnd.randrange(1, 10)

for a in array:
    if a % 2 == 0:
        print(f"el numero par es: {a}")
        
enteros = []
for i in range(100):
    enteros.append(rnd.randrange(1, 10))
    
def printList(ListaEnteros):
    for i in ListaEnteros:
        if i % 2 == 0:
            print(f"el numero par es: {i}")