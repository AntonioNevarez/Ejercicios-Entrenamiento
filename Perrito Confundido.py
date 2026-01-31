"""
 Ejercicio
 Autor: Jesus Antonio Nevarez Lopez
 Fecha: 31/01/2026
 El problema se trata sobre un perro que debe de elegir entre un hueso y el otro considerando las siguientes características
 el olor y el tamaño, si en un hueso tanto el olor y el tamaño es mayor que el otro, toma como preferencia ese hueso, caso
 contrario, preferira el otro hueso o ninguno de los dos si una característica es mayor que otra
"""

if __name__ == '__main__':
    # Pide al usuario 2 enteros en una linea
  hueso1 = list(map(int, input().split()))
  hueso2 = list(map(int, input().split()))

if hueso1[0] > hueso2[0] and hueso1[1] > hueso2[1]:
  print("Hueso 1")
elif hueso2[0] > hueso1[0] and hueso2[1] > hueso1[1]:
    print("Hueso 2")
else:
    print("Perrito confundido :(")




