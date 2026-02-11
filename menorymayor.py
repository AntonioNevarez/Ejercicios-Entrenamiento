import sys

def solve():
    datos = list(map(int,sys.stdin.read().split()))
    mayor = (max(datos))
    menor = (min(datos))

    sys.stdout.write(f"{menor} {mayor}\n") # Borra las +, permite poner {} a las variables

if __name__ == '__main__':
    solve()