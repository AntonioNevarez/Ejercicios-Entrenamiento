""""
Ejercicio: Imprimiendo enteros por paridad
Autor: Jesus Antonio Nevarez Lopez
Fecha: 30/01/26

"""
if __name__ == '__main__':
    # Se lee la cantidad de numeros contenidos del arreglo y la paridad que se busca
 Tamaño = int(input())
 Arreglo = list(map(int,input().split()))
 Par_o_Impar = int(input())
 for i in range(Tamaño):
     if Par_o_Impar == 0:
         # Caso para numeros pares
         if Arreglo[i]% 2 == 0:
             print(Arreglo[i])
     # Caso para numeros impares (P=1)
     elif Arreglo[i]%2 != 0:
         print(Arreglo[i])















