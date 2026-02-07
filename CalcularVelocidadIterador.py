"""
Ejercicio
Autor: Jesus Antonio Nevarez Lopez
Se pide calcular la velocidad media maxima de un numero dado de valores que son la distancia y el tiempo, inicialmente si pide el numero de
veces o trayectos que hace el objeto, pero no fue necesario saberlo debido al uso de un iterador, en este problema, se empleó distintas
funciones y el retorno de multiples valores de una sola función
Fecha 07/02/2026
"""
import sys


def solve():
 input_data = list(map(int,sys.stdin.read().split()))
 if not input_data:
     return
 it = iter(input_data[1:]) # Se empieza el iterador en 1 porque el problema en especifico pide el numero de puntos

 vel_max=0
 distancia_f = 0
 tiempo_f = 0
 while True: #
     try: # Excepcion para saber cuando el iterador se queda sin valores
         tiempo_i = next(it)
         distancia_i = next(it)
         velocidad, tiempo_f, distancia_f = calcular_velocidad(distancia_i, tiempo_i, distancia_f, tiempo_f) # Se puede almacenar varios valores que retorna una funcion
         if velocidad > vel_max:
              vel_max = velocidad
     except StopIteration: # Salir del bucle
         break
 print(int(vel_max))

def calcular_velocidad(distancia_i,tiempo_i,distancia_f,tiempo_f):
    if distancia_i==0 and tiempo_i==0:
        return 0,0,0 # Retornamos 3 ceros debido a la linea 25 que pide obligatoriamente retornar 3 valores de la funcion
    else:
        velocidad = (distancia_f-distancia_i)/(tiempo_f-tiempo_i)
        tiempo_f = tiempo_i
        distancia_f = distancia_i
        return velocidad,tiempo_f,distancia_f

if __name__ == '__main__':
    solve()
