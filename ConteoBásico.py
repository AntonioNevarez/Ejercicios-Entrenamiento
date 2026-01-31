"""
Ejercicio: Conteos básicos
Autor: Jesus Antonio Nevarez Lopez
Fecha: 30/01/26

Realizar un programa que pida al usuario un numero A inicial y un numero B final e imprima
el conteo del punto A al B
"""

if __name__ == '__main__':
 numeros = list(map(int, input().split())) # Se piden 2 numeros en una sola linea
 inicio = numeros[0]
 contador = 0
 if numeros[0] > 0 and numeros[1] > 0: # Si el numero inicial es positivo, ejemplo (3, 4)
     indice = (numeros[1]-numeros[0])+1 # Se calcula la cantidad de numeros a contar
     contador = [0] * indice
     for i in range(indice):
         contador[i] = inicio
         print(contador[i])
         inicio += 1
 elif numeros[0] < 0: # Si el numero inicial es negativo, ejemplo (-3, 4)
     indice = (-1*(numeros[0])+numeros[1])+1
     contador = [0] * indice
     for i in range(indice):
         contador[i] = inicio
         print(contador[i])
         inicio += 1
 elif numeros[0] == 0: # Si el numero inicial es 0, ejemplo (0, 4)
     indice = numeros[1]+1
     contador = [0] * indice
     for i in range(indice):
         contador[i] = inicio
         print(contador[i])
         inicio += 1












