nome = input('Bem vindx ao Portal Tabajara\nNos informe seu nome: ')

salario = int(input(f'Olá {nome}!\nAgora nos informe seu salário atual: '))

if salario <= 280:
    aumento = (salario/5)
    novo = aumento + salario
    print(f'{nome} seu salário de {salario} aumentou em 20% com valor equivalente a {aumento} e foi para {novo} ')
elif salario > 280 and salario <= 700:
    aumento = salario*0.15
    novo = aumento + salario
    print(f'{nome} seu salário de {salario} aumentou em 15% com valor equivalente a {aumento} e foi para {novo} ')
elif salario > 700 and salario <= 1500:
    aumento = salario/10
    novo = aumento + salario
    print(f'{nome} seu salário de {salario} aumentou em 10% com valor equivalente a {aumento} e foi para {novo} ')
elif salario > 1500:
    aumento = salario*0.05
    novo = aumento + salario
    print(f'{nome} seu salário de {salario} aumentou em 5% com valor equivalente a {aumento} e foi para {novo} ')
else:
    print('Error!')