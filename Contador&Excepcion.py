"""
Ejercicio
Autor: Jesus Antonio Nevarez Lopez
Fecha: 03/02/26
El problema pide una lista de caracteres separados por espacios y contar el conjunto de la lista
se utilizo una funcion y en este caso una variable global que se maneje tanto en la funcion como
en la main y una excepcion con una funcion llamada StopIteration que viene por predeterminado
y esta ocurre cuando la variable dato se queda sin datos (valga la redundancia) al pasar en next(it), practicamente
es si el iterador se queda sin argumentos
"""

import sys

contador = 0 # Variable global antes de la funcion y el main

def solve():
    global contador # Poner global para que se active
    input_data = sys.stdin.read().split() # Lee un conjunto y el .split forma una lista
    it = iter(input_data) # Iteracion apuntando a ese conjunto
    while True: # Bucle Infinito
        try:
            dato = next(it) # Lo que provoca la excepcion
            contador += 1
        except StopIteration:
           break # Forzar salir del bucle


if __name__ == '__main__':
    solve()
    print(contador)
    sys.stdout.flush() # Limpiar el buffer

