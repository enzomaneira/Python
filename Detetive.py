print('Você será submetido a uma série de perguntas sobre um assassinato\n'
      'A perguntas deverão ser respondidas com Sim ou Não')

start = input('Digite I para começar\n')

check = []

if start == 'I':
    p1 = input('Você telefonou para a vítima recentemente?\n')
    p2 = input('Você esteve no local do crime?\n')
    p3 = input('Você mora perto da vítima?\n')
    p4 = input('Você devia alguma quantidade em dinheiro para a vítima?\n')
    p5 = input('Você ja trabalhou para/com a vítima?\n')
else:
    print('Erro')

if p1 == 'sim':
    check.append(1)
else:
    print(' ')

if p2 == 'sim':
    check.append(2)
else:
    print(' ')

if p3 == 'sim':
    check.append(3)
else:
    print(' ')

if p4 == 'sim':
    check.append(4)
else:
    print(' ')

if p5 == 'sim':
    check.append(5)
else:
    print(' ')

if len(check) == 5:
    print('\n\n\nCulpado')
elif len(check) > 2 and len(check) < 5:
    print('\n\nCúmplice')
elif len(check) == 1 or len(check) == 2:
    print('Suspeito')
elif len(check) == 0:
    print('Inocente')
else:
    print('Erro')