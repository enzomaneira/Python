import math

a = float(input('Informe valor a: '))
b = float(input('Informe valor b: '))
c = float(input('Informe valor c: '))

delta = (b*b) - 4*a*c
print(f'Delta = {delta}')

if a == 0 or delta < 0:
    print('Equação impossível de ser realizada')
elif delta > 0:
    print('Equação tem 2 raízes')
    raiz = math.sqrt(delta)
    x1 = (-b + raiz)/(2 * a)
    x2 = (-b - raiz) / (2 * a)
    print(f'Raiz 1 = {x1}\nRaiz 2 = {x2}')
elif delta == 0:
    print('Equação tem apenas 1 raiz')
    raiz = math.sqrt(delta)
    x = (-b + raiz) / (2 * a)
    print(f'Raiz = {x}')
else:
    print('Erro!')
