"""
Fecha 19/02/2025
Ejercicio
Jesus Antonio Nevarez Lopez
Se pide imprimir el consola el index del alumno con el valor mas alto en estatura, pero si el numero de niños es menor a 40
0 menor que 1, imprimir ERROR en su lugar, y tambien si la estatura de algunos de los niños es menor a 50, tambien imprimir
ERROR, valor de la practica solo fue el uso de if any, if all y generador de condicion.
"""
import sys
def solve():
    entrada = list(map(int, sys.stdin.read().split()))
    if not entrada:
        return
    n = entrada[0]
    estatura = entrada[1:]

    if n < 1 or n >= 40:
        return sys.stdout.write("ERROR\n")
    """
    for i in range(len(estatura)):
        if estatura[i] < 50:
            return sys.stdout.write("ERROR\n")
    """

    if any(x < 50 for x in estatura): # if any es si uno de los valores es verdadero, retorna true (false,false,true) = true
        print("ERROR")
        return
    alto = estatura.index(max(estatura))
    return sys.stdout.write(str(alto+1))




if __name__ == '__main__':
    solve()
