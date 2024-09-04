# cheat-sheet

```python
# Declaración de variables
x = 10
nombre = "santiago"

1)Tipos De Datos
# Tipos básicos
entero = 42
flotante = 3.14
cadena = "Hola, Mundo!"
booleano = True

# Listas
lista = [1, 2, 3, 4, 5]

# Tuplas
tupla = (1, 2, 3, 4, 5)

# Diccionarios
diccionario = {"clave1": "valor1", "clave2": "valor2"}

# Conjuntos
conjunto = {1, 2, 3, 4, 5}
2)Operaciones

# Suma
a = 5 + 3

# Resta
b = 5 - 3

# Multiplicación
c = 5 * 3

# División
d = 5 / 3

# Módulo
e = 5 % 3

# Exponenciación
f = 5 ** 3
Operadores de Comparación
a == b  # Igual a
a != b  # Diferente de
a > b   # Mayor que
a < b   # Menor que
a >= b  # Mayor o igual que
a <= b  # Menor o igual que
Operadores Logicos
a and b  # Y lógico
a or b   # O lógico
not a    # Negación lógica
3) Estructuras de Control
if x > 10:
    print("x es mayor que 10")
elif x == 10:
    print("x es igual a 10")
else:
    print("x es menor que 10")
Bucles
for i in range(5):
    print(i)
i = 0
while i < 5:
    print(i)
    i += 1
4)Funciones
def saludo(nombre):
    return f"Hola, {nombre}!"

print(saludo("Santiago"))

def potencia(base, exponente=2):
    return base ** exponente

print(potencia(4))       # Usa el valor predeterminado de exponente
print(potencia(4, 3))    # Usa el valor proporcionado de exponente

5)Modulos
import math
print(math.sqrt(16))  # Usa la función sqrt del módulo math

from math import sqrt
print(sqrt(16))
6) Manejo de Archivos
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
with open('archivo.txt', 'w') as archivo:
    archivo.write("Hola, Mundo!")
7)excepciones
try:
    x = 1 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
finally:
    print("Esto siempre se ejecuta")
8) Listas
mi_lista = [1, 2, 3, 4, 5]

cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # Imprime los cuadrados de los números del 0 al 9
9)Clases/Objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

persona = Persona("Alice", 30)
print(persona.saludar())
10)Bibliotecas

import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array.mean())  # Calcula la media de los valores en el array

import pandas as pd

data = {'Nombre': ['Alice', 'Bob'], 'Edad': [30, 25]}
df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de ejemplo')
plt.show()



































