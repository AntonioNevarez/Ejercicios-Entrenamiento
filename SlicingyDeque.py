import sys
from collections import deque
"""
Ejercicio
Slicing
Autor: Jesus Antonio Nevarez Lopez
Fecha: 08/02/2026
El problema pide encontrar el valor maximo en un cierto periodo, la complejidad del problema fue el tiempo, ya que los
valores a insertar son mas de un millon, pór lo que un array comun no funciona, o ciclos comunes, por lo que se tuvo
que usar dq que actua como una lista doblemente enlazada con sus nodos y punteros de derecha e izquierda, ademas de usar
slicing que permite recortar una lista, el codigo comentado fueron otros metodos que igual funcionaban pero no eran lo 
suficientemente eficientes, por lo que deque seria la mejor funcion en cuanto listas porque va borrando las que ya no se 
usan aunque no terminé de comprender como funcionan exactamente por lo que trataré de usarlo en futuros ejercicios

"""
def solve():
    dato = sys.stdin.read().split()
    if not dato: return
    dias = int(dato[0])
    periodo = int(dato[1])
    periodo_dias = list(map(int, dato[2: 2 + dias])) # Slicing 2: indicia el comienzo, 2+dias el resto
    dq = deque()
    resultados = []

    for i in range(dias):
        # Saca el elemento mas viejo
        if dq and dq[0] <= i - periodo: # if dq comprueba si la lista esta vacia y i - periodo es el limite para eliminar
            dq.popleft() # Elimina izquierda
            # Inserta el elemento con mayor valor
        while dq and periodo_dias[dq[-1]] <= periodo_dias[i]: # dq[-1+] es el ultimo
         dq.pop() # Elimina derecha
        dq.append(i)
        if i >= periodo-1:
            resultados.append(periodo_dias[dq[0]])
    sys.stdout.write('\n'.join(map(str,resultados))+ '\n') # Mas eficiente que print


"""
    for i in range(salida):
        ventana = periodo_dias[i: i + periodo]
        resultados.append(max(ventana))
 sys.stdout.write('\n'.join(map(str,resultados))+'\n')
 """

"""
    valores_max = [0] * salida
    contador_dias =0
    contador = 0
    for _ in range(salida):
        for _i in range(periodo):
            actual = periodo_dias[contador_dias]
            if contador > len(valores_max):
                break
            if actual > valores_max[contador]:
                valores_max[contador]= actual
            contador_dias +=1
        contador += 1
        contador_dias = (contador_dias - periodo+1)
    for i in range(len(valores_max)):
        print(valores_max[i])
"""

if __name__ == '__main__':
 solve()

