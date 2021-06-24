numero = int(input('Digite um numero menor que 1000\n- '))

cent = (numero % 1000)/100
dez = (numero % 100)/10
uni = numero % 10

if numero > 100 and numero < 1000:
   print(f'{numero} tem:\n{round(cent-0.5)} centenas\n{round(dez-0.5)} dezenas\n{uni} unidades')
elif numero < 100 and numero > 9:
    print(f'{numero} tem:\n{round(dez - 0.5)} dezenas\n{uni} unidades')
elif numero < 10:
    print(f'{numero} tem:\n{uni} unidades')
else:
    print('Número maior que mil')
