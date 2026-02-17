"Ejemplo de Funcion y tablas"

import sys
def f(x):
    return x**2 + 2
serie = [1,2,3,4,5]
acumulado=[]
suma_total = 0

sys.stdout.write(f"{'x':^10} | {'f(x)':^10} | {'Suma Acumulada':^15}\n")
print("-"*40)
for valor in serie:
    resultado = f(valor)
    acumulado.append(resultado)
    suma_total +=resultado
    sys.stdout.write(f"{valor:^10} | {resultado:^10} | {suma_total:^15}\n")
print("-" * 40)
sys.stdout.write(f"Lista final: {acumulado}\n")
sys.stdout.write(f"Gran Total: {suma_total}")




 