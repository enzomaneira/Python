"""
Enzo Maneira Canatella

G.A.B.S.D.E

9/01/2001
"""

#Criando dic

estagDic = { }

print('Bem Vindx ao G.A.B.S.D.E\n')

#Criando Variável Nome
nome = str(input('Insira o nome de descrição da vaga:  '))
print(nome)

#checagem de decisão
check = input('A descrição está correta?\n')

#Loop anti-erro
while check != 'sim':
    nome = str(input('Insira o nome de descrição da vaga novamente:  '))
    print(nome)
    check = input('A descrição está correta?\n')
else:
    print(f'[Estágio]{nome}')

#Criando Variável Empresa
empresa = str(input('Insira o nome da empresa:  '))
print(f'[ESTÁGIO]{nome} - {empresa}')

#checagem de decisão
check2 = input('O nome da empresa está correto?\n')

#Loop anti-erro
while check2 != 'sim':
    empresa = str(input('Insira o nome da empresa novamente:  '))
    print(empresa)
    check2 = input('O nome da empresa está correto?\n')
else:
    print(f'[ESTÁGIO]{nome} - {empresa}')

#Criando Variável Descrição
desc = str(input('Insira a descrição da empresa:  '))
print(desc)

#checagem de decisão
check3 = input('A descrição está correta?\n')

#Loop anti-erro
while check3 != 'sim':
    desc = str(input('Insira a descrição da empresa novamente:  '))
    print(empresa)
    check3 = input('A descrição está correta?\n')
else:
    print(f'1 - [ESTÁGIO]{nome} - {empresa}\n2 - {desc}\n')

#Criando Lista de Requerimentos
requerimentos = [ ]
req1 = str(input('Insira os requerimentos necessários para a vaga:  '))
requerimentos.append(req1)
print(requerimentos)

#Checagem de adição de variável
checkadd = input('Deseja adicionar outro requerimento?\n')

#Loop anti-erro
while checkadd == 'sim':
    requerimentos.append(input('Insira outro requerimento:  '))
    print(requerimentos)
    checkadd = input('Deseja adicionar outro requerimento?\n')
else:
    print(f'1 - [ESTÁGIO]{nome} - {empresa}\n2 - {desc}\n3 - {requerimentos}')

#Criando Variável Salário
salario = int(input('Insira o salário oferecido pela vaga:  '))
print(f'R${salario}')

#checagem de decisão
check4 = str(input('O salário está correto?\n'))

#Loop anti-erro
while check4 != 'sim':
    salario = int(input('Insira o salário oferecido pela vaga:  '))
    print(f'R${salario}')
    check4 = str(input('O salário está correto?\n'))
else:
    print(f'1 - [ESTÁGIO]{nome} - {empresa}\n2 - {desc}\n3 - Requerimentos: {requerimentos}\n4 - Salário:  R${salario}\n ')

#Criando Lista com Benefícios
benef = [ ]
benef1 = str(input('Insira o benefício oferecido pelo Estágio:  '))
benef.append(benef1)
for i in range(len(benef)):
    print(benef[i])


# Checagem de adição de variável
checkaddb = input('Deseja adicionar outro benefício?\n')

#Loop anti-erro
while checkaddb == 'sim':
    benef.append(input('Insira outro benefício:  '))
    print(benef)
    checkaddb = input('Deseja adicionar outro beneficío?\n')
else:
    print(f'1 - [ESTÁGIO]{nome} - {empresa}\n2 - {desc}\n3 - REQUERIMENTOS\n{requerimentos}\n4 - Salário:  R${salario}'
        f'\n5 - BENEFÍCIOS\n{benef} ')

#Criando variável link
link = str(input('Insira um link para mais informações:  '))
print(link)

#Checagem de decisão
checklink = str(input('O link está correto?\n'))

#Loop anti-erro
while checklink != 'sim':
    link = str(input('Insira um link para mais informações:  '))
    print(link)
    check4 = str(input('O link está correto?\n'))
else:
    print(f'1 - [ESTÁGIO]{nome} - {empresa}\n2 - {desc}\n3 - REQUERIMENTOS\n{requerimentos}\n4 - Salário:  R${salario}'
          f'\n5 - BENEFÍCIOS\n{benef}\n6 - Para mais informações acesse:\n{link}')







