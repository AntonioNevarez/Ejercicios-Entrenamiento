"""
Ejercicio
Autor: Jesus Antonio Nevarez Lopez
Fecha: 01/02/2026
El problema pide encontrar la suma de una cantidad N de valores, y de esa restarle el menor,
Esta vez se utilizó el uso de una función y de sys.stdin.read.split() junto a un iterador para
ser más eficientes en el uso de memoria, aunque para cantidad mayores de valores "sys.stdin.read().split"
no es muy eficiente si la entrada es por ejemplo de 1 millón, por lo que no es recomendable crear listas o arreglos
si el número es muy grande pero igualmente es una forma más rapida.
"""


import sys

def solve():
    # .read().split() toma  el texto y lo divide en una lista de palabras/números
    input_data = sys.stdin.read().split()
    # Si ya no hay datos  se detiene el programa
    if not input_data:
        return
    # El numero de juguetes toma el primer valor de entrada
    numero_juguetes = int(input_data[0])
    # El puntador empieza desde la posicion 1
    it = iter(input_data[1:])
    # Toma valor del primer valor de la lista recortada
    primer_valor = int(next(it))
    suma = primer_valor
    menor = primer_valor
    for _ in range(numero_juguetes-1):
        actual = int(next(it))
        suma += actual
        if menor >= actual:
            menor = actual
    print(suma-menor)

if __name__ == '__main__':
    # Llamar funcion
    solve()




