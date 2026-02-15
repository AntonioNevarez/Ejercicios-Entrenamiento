import sys
import math
"""
Ejercicio 
Jesus Antonio Nevarez Lopez
Ejercicio basico de convertir fracciones en mixtas, se utilizo math.trunc para recortar los decimales
y usamos f" en la salida para evitar la concanetacion y mas eficiente
"""
def solve():
     data = list(map(int,sys.stdin.read().split()))
     entero = math.trunc(data[0]/data[1])
     residuo = data[0]%data[1]
     if residuo == 0:
         sys.stdout.write(f"{entero}\n")
     else:
         sys.stdout.write(f"{entero} {residuo}/{data[1]}")

if __name__ == '__main__':
    solve()


