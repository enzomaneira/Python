print('Bem vindx a Barraca ManeiraFrutas\n')

escMo = input('Gostaria de comprar Morango?\n')

if escMo == 'sim':
    qMo = float(input('Quanto kgs de morango deseja comprar?\n'))
else:
    print('Ah, ok!')

escMa = input('E maçã? Quer comprar?\n')

if escMa == 'sim':
    qMa = float(input('Quanto kgs de maçã deseja comprar?\n'))
else:
    print('Ah, ok!')

carrinho = qMa + qMo

if qMa <= 5 and qMa > 0:
    preçoMa = qMa * 1.8
else:
    preçoMa = qMa * 1.5

if qMo <= 5 and qMo > 0:
    preçoMo = qMo * 2.5
else:
    preçoMo = qMo * 2.2

preço = preçoMa + preçoMo

if carrinho > 8 or preço > 25:
    desconto = preço * 0.1
    preçoF = preço - desconto
    print(f'Morango : {qMo}kg\nMaçã: {qMa}kg\nDesconto: R${desconto}\nPreço Final: R${preçoF}')

if carrinho < 8 and preço < 25:
    print(f'Morango : {qMo}kg\nMaçã: {qMa}kg\nPreço Final: R${preço}')
else:
    print('')

