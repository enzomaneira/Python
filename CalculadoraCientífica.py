import math

print('MENU CALCULADORA\n')
print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potenciação\n6 - Radiciação\n')
menu = int(input('Selecione opção: '))

if menu == 1:
    n1 = int(input('Informe primeiro número: '))
    n2 = int(input('Informe segundo numero: '))
    r = n1 + n2
    print(f'{n1} + {n2} = {r}')
elif menu == 2:
    n1 = int(input('Informe primeiro número: '))
    n2 = int(input('Informe segundo numero: '))
    r = n1 - n2
    print(f'{n1} - {n2} = {r}')
elif menu == 3:
    n1 = int(input('Informe primeiro número: '))
    n2 = int(input('Informe segundo numero: '))
    r = n1 * n2
    print(f'{n1} x {n2} = {r}')
elif menu == 4:
    n1 = int(input('Informe primeiro número: '))
    n2 = int(input('Informe segundo numero: '))
    r = n1 / n2
    print(f'{n1} / {n2} = {r}')
elif menu == 5:
    n1 = int(input('Informe primeiro número: '))
    n2 = int(input('Informe segundo numero: '))
    r = n1 ** n2
    print(f'{n1} elevado a {n2} = {r}')
elif menu == 6:
    n = int(input('Informe número: '))
    r = math.sqrt(n)
    print(f'Raiz quadrada de {n} = {r} ')
else:
    print('Erro!')