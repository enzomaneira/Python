numero = int(input('Digite a quantidade que deseja sacar\n- '))

cem = int(numero / 100)
numero = numero % 100

cinquenta = int(numero / 50)
numero = numero % 50

vinte = int(numero / 20)
numero = numero % 20

dez = int(numero / 10)
numero = numero % 10

cinco = int(numero / 5)
numero = numero % 5

um = numero

print(f'Notas de R$100: {cem}\nNotas de R$50: {cinquenta}\nNotas de R$20: {vinte}\n'
      f'Notas de R$10: {dez}\nNotas de R$5: {cinco}\nMoedas de R$1: {um}')



