import sys
import math
def calcular_et(valor_verdadero,valor_aproximado):
    return (abs(valor_verdadero-valor_aproximado))

def calcular_et_porcentual(et,valor_verdadero):
    return (abs((et/valor_verdadero*100)))

def calcular_relativo_proporcional(aproxactual,aproxanterior):
    return (abs((aproxactual-aproxanterior)/aproxactual)*100)

def serie(suma, potencia, denominador, x, signo):
    if signo % 2 == 0:
        res = (suma - (x**potencia / math.factorial(denominador)))
    else:
        res = (suma + (x**potencia / math.factorial(denominador)))
    return res

 
x=1.047197551
valor_verdadero=0.5
valor_aproximado=1
potencia=2
denominador=2
termino=1
suma=1
signo=2
sys.stdout.write(f"{'Termino':^10} | {'Valor Aproximado':^20} | {'Et':^15} | {'Et%':^15} | {'Ea%':^15}\n")
et = calcular_et(valor_verdadero,1)
et_porcentual = calcular_et_porcentual(et,valor_verdadero)
sys.stdout.write(f"{termino:^10} | {valor_aproximado:^20} | {et:^15} | {et_porcentual:^15.2f} | {'':^15}\n")
contador=2
for i in range(6):
    termino+=1
    aprox_ant=valor_aproximado
    valor_aproximado = serie(suma,potencia,denominador,x,signo)
    suma=valor_aproximado
    potencia+=2
    denominador+=2
    signo+=1
    et = calcular_et(valor_verdadero,valor_aproximado)
    et_porcentual = calcular_et_porcentual(et,valor_verdadero)
    ea = calcular_relativo_proporcional(valor_aproximado,aprox_ant)
    sys.stdout.write(f"{termino:^10} | {valor_aproximado:^20.7f} | {et:^15.8f} | {et_porcentual:^15.6f} | {ea:^15.6f}\n")

  





    
   
    



