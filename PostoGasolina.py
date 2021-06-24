print('Bem vindx ao Posto Maneira')
tipo = input('Você deseja encher seu carro com Gasolina ou Alcool?\n')

check = []

if tipo == 'gasolina' or tipo == 'Gasolina':
    q = float(input('Quantos litros de gasolina deseja colocar?\n'))
    check.append(1)
elif tipo == 'alcool' or tipo == 'Alcool':
    q = float(input('Quantos litros de alcool deseja colocar?\n'))
    check.append(2)

if 1 in check and q <= 20:
    p = (q*4.2)
    d = p*0.04
    f = p - d
    print(f'Preço: {p}\nDesconto: {d}\nPreço Final: {f}')
elif 1 in check and q > 20:
    p = (q * 4.2)
    d = p * 0.06
    f = p - d
    print(f'Preço: {p}\nDesconto: {d}\nPreço Final: {f}')
else:
    print('')

if 2 in check and q <= 20:
    p = q * 2.8
    d = p*0.03
    f = p - d
    print(f'Preço: {p}\nDesconto: {d}\nPreço Final: {f}')
elif 2 in check and q > 20:
    p = (q * 2.8)
    d = p * 0.05
    f = p - d
    print(f'Preço: {p}\nDesconto: {d}\nPreço Final: {f}')
else:
    print('')


