from math import isqrt

def criba(n):
    primos = [0,1] * (n//2 + 1)
    primos[:3] = [0,0,0]

    limite = isqrt(n) + 1

    for p in range(3, limite, 2):
        if primos[p] == 1:
            primos[p*p:n:p+p] = [0]*len(range(p*p, n, p+p))

    primos[2] = 1
    return primos[:n+1]


rango = int(input())
consultas = []
maximo = 0

for _ in range(rango):
    ini, fin = map(int, input().split())
    consultas.append((ini,fin))
    if fin > maximo:
        maximo = fin

tabla = criba(maximo)

acum = [0]*(maximo+1)

for i in range(1,maximo+1):
    acum[i] = acum[i-1] + (1 if tabla[i] else 0)

for ini,fin in consultas:
    print(acum[fin] - acum[ini-1])