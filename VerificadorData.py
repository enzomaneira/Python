print('Verificador de data\n')

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

bi = ano % 4
check = []

if mes > 0 and mes < 13:
    check.append(1)
else:
    print('Data inválida')


if 1 in check and ano < 2021 and ano > 0:
    check.append(2)
else:
    print('Data inválida')

if 2 in check and dia > 0:
    check.append(3)
else:
    print('Data inválida!')

if 3 in check and mes == 1 and dia < 32:
    print(f'{dia}/0{mes}/{ano}')
elif 3 in check and mes == 2 and bi == 0 and dia < 30:
    print(f'{dia}/0{mes}/{ano}')
elif 3 in check and mes == 2 and bi !=0 and dia < 29:
    print(f'{dia}/0{mes}/{ano}')
elif 3 in check and mes == 3 and dia < 32:
    print(f'{dia}/0{mes}/{ano}')
elif 3 in check and mes == 4 and dia < 31:
    print(f'{dia}/0{mes}/{ano}')
elif 3 in check and mes == 5 and dia < 32:
    print(f'{dia}/0{mes}/{ano}')
elif 3 in check and mes == 6 and dia < 31:
    print(f'{dia}/0{mes}/{ano}')
elif 3 in check and mes == 7 and dia < 32:
    print(f'{dia}/0{mes}/{ano}')
elif 3 in check and mes == 8 and dia < 32:
    print(f'{dia}/0{mes}/{ano}')
elif 3 in check and mes == 9 and dia < 31:
    print(f'{dia}/0{mes}/{ano}')
elif 3 in check and mes == 10 and dia < 32:
    print(f'{dia}/{mes}/{ano}')
elif 3 in check and mes == 11 and dia < 31:
    print(f'{dia}/{mes}/{ano}')
elif 3 in check and mes == 12 and dia < 32:
    print(f'{dia}/{mes}/{ano}')
else:
    print('Erro! Data inválida')

if dia == 14 and mes == 4:
    print('ManeiraDay')
elif dia == 17 and mes == 10 and ano == 2001:
    print('Aniversário da Li')
elif dia == 8 and mes == 7:
    print('Aniversário Brand')
elif dia == 10 and mes == 1:
    print('Aniversário Vic')
elif dia == 14 and mes == 3:
    print('Aniversário Gabs')
elif dia == 5 and mes == 10:
    print('DéVersário')
elif dia == 15 and mes == 11:
    print('Aniversário Mariah')
elif dia == 24 and mes == 1:
    print('Aniversário Isabela')
elif dia == 2 and mes == 2:
    print('Aniversário Thiago')
elif dia == 18 and mes == 7:
    print('Aniversário Pedote')
elif dia == 14 and mes == 8:
    print('Aniversário Miguelzinho')
