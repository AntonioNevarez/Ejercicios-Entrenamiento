import sys
from collections import deque
"""
Ejercicio
Autor: Jesus Antonio Nevarez Lopez
Fecha 09/02/26
Imprimir numeros naturales del punto a al punto b, uso de deque, pero como solo estamos agregando datos al final
una lista es mejor y uso del objeto range que es un generador que solo guarda el inicio y el fin, tambien sirve
para sucesiones.

"""
def solve():
    dato = sys.stdin.read().split()
    dato = "2 10".split()
    dq = deque()
    a = int(dato[0])
    b = int(dato[1])
    # Objeto range consume mucho menos memoria, pero los datos son inmutables o no modificables
    numeros = range(a, b + 1,2)  # Inicio, fin, sucesion
    sys.stdout.write('\n'.join(map(str,numeros))+'\n') # \n.join salto de linea
    """
   for i in range(a,b+1): # Inicio a, b final
            dq.append(i)
    sys.stdout.write('\n'.join(map(str,dq))+'\n') # \n.join salto de 
        """


if __name__ == '__main__':
    solve()