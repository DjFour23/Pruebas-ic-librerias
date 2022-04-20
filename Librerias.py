# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:39:29 2022

@author: diego
"""

import numpy as np
import time

n = 10000

#Lista en python
l1=list(range(n))
l2=list(range(n))


start = time.time()
l3 = []
for x in range(len(l1)):
    l3.append(l1[x]+l2[x])
end = time.time()
print('Total milisegundos lista: ',(end-start)*1000)

n1= np.arange(n)
n2= np.arange(n)

start = time.time()
n3= n1+n2
end= time.time()
print('Total milisegundos Numpy: ',(end-start)*1000)


# Metodos de Numpy

a = [2, 3, 4, 5, 6]
b = [7, 9, 10, 11, 12]

#Convertir el vector en un vector numpy

n1 = np.array(a)
n2 = np.array(b)

# Operaciones numpy

n3 = n1 + n2
n3 = n1 - n2
n3 = n1 * n2
n3 = n1 / n2

# Conocer las dimesiones de un vector numpy

n3.shape

n4 = np.array([[3, 4, 5], [5, 6, 7], [5, 6, 7]])

#Matriz de ceros

n4 = np.zeros((4, 4))

# Matriz de unos

n4 = np.ones((4, 4))

# Matriz de un nuemero especifico

n4 = np.full((5, 6),9)

#Matiz con elementos random

n4 = np.random.random((3, 3))

#Matriz identidad

n4 = np.eye(5)

#HUA que de como resultado la diagonal principal de una matriz random y los demas
#elementos en cero

num = 3
n5 = np.random.random((num, num))
n6 = n5 * np.eye(num)


#Cual es elemento mas grande de de una matriz
print(n5.max())
#Cual es elemento mas pequeño de de una matriz
print(n5.min())
#Cual es el promedio de de una matriz
print(n5.mean())
#Cual es la sumatoria de de una matriz
print(n5.sum())
#Raiz cuadrada de todos los elementos
print(np.sqrt(n4))
#Seno
print(np.sin(n4))
#Coseno
print(np.cos(n4))
#logaritmo
print(np.log(n4))

f1 = [4, 5, 6, 7, 9]
f2 = [3, 4, 5, 6, 8]
f3 = [1, 5, 6, 9, 10]

matriz = np.array([f1, f2, f3])
trasp = matriz.T

c = [[3, 1, 9], [7, 2, 4],[8, 6, 6]]
d = [[3, 1, 9], [7, 2, 5],[8, 6, 6]]

nc = np.array(c)
nd = np.array(d)

# Validar que los sean iguales

nc == nd

# multiplicar por un escalar

nc * 2

# elevar al cuadrado

nc ** 2

# filtrado de elementos

nc[nc < 5]

# Fila uno todas las columnas 
nc[1, :]

# Todas las filas de la columna uno
nc[:, 1]

nc[2, 1:2]

nc[2, 1:3]

nc[2, 1:]


# Matriz aleatoria de números enteros

ma = np.random.randint(20, size=(5,5))
ma = np.random.randint(20, size=(5,5))

# Random de números decimales
np.random.uniform(0,5, size = (5,5))

#Cosa 1
#Cosa 2
#Cosa 3



