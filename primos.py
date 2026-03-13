import sys
MAX = 10000001
es_primo = [True] * MAX
es_primo[0] = es_primo[1] = False
def criba():
    for p in range(2, int(MAX**0.5) + 1):
        if es_primo[p]:
            for i in range(p * p, MAX, p):
                es_primo[i] = False
criba()
def resolver():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T_casos = int(input_data[0])
    pos = 1
    for _ in range(T_casos):
        if pos + 1 < len(input_data):
            a = int(input_data[pos])
            b = int(input_data[pos+1])
            
            inicio = min(a, b)
            fin = max(a, b)
            contador = 0
            for i in range(inicio, fin + 1):
                if es_primo[i]:
                    contador += 1
            print(contador)
            pos += 2
if __name__ == "__main__":
    resolver()