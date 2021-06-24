"""
Enzo Maneira Canatella

G.A.B.S.D.E

27/03/2001
"""

def cria_menu():
    menu = str(input('1 - Adicionar estágio\n2 - Modificar estágio\n3 - Excluir estágio\n4 - Acessar arquivo\n'))
    return menu


def add_estagio():
    nome = str(input('Insira o nome de descrição da vaga:  '))
    print(f'[Estágio]{nome}')
    empresa = str(input('Insira o nome da empresa:  '))
    print(f'[ESTÁGIO]{nome} - {empresa}')
    desc = str(input('Insira a descrição da empresa:  '))
    print(desc)
    requerimentos = []
    req1 = str(input('Insira os requerimentos necessários para a vaga:  '))
    requerimentos.append(req1)
    for i in range(len(requerimentos)):
        print(requerimentos[i])
    checkadd = input('Deseja adicionar outro requerimento?\n')
    while checkadd == 'sim':
        requerimentos.append(input('Insira outro requerimento:  '))
        for i in range(len(requerimentos)):
            print(requerimentos[i])
        checkadd = input('Deseja adicionar outro requerimento?\n')
    else:
        print(f'1 - [ESTÁGIO]{nome} - {empresa}\n2 - {desc}\n3 - {requerimentos}')
    salario = int(input('Insira o salário oferecido pela vaga:  '))
    print(f'R${salario}')
    benef = []
    benef1 = str(input('Insira o benefício oferecido pelo Estágio:  '))
    benef.append(benef1)
    for i in range(len(benef)):
        print(benef[i])
    checkaddb = input('Deseja adicionar outro benefício?\n')
    while checkaddb == 'sim':
        benef.append(input('Insira outro benefício:  '))
        for i in range(len(benef)):
            print(benef[i])
        checkaddb = input('Deseja adicionar outro beneficío?\n')
    else:
        print(
            f'1 - [ESTÁGIO]{nome} - {empresa}\n2 - {desc}\n3 - REQUERIMENTOS\n{requerimentos}\n4 - Salário:  R${salario}'
            f'\n5 - BENEFÍCIOS\n{benef} ')
    link = str(input('Insira um link para mais informações:  '))
    print(link)
    with open('Estágio.txt', 'a') as arquivo:
        arquivo.write(f'[Estágio]{nome} - {empresa}\n')
        arquivo.write(f'{desc}\n')
        arquivo.write(f'Requerimentos\n')
        for i in range(len(requerimentos)):
            arquivo.write(f'-{requerimentos[i]}\n')
        arquivo.write(f'Salário: {salario}\n')
        arquivo.write(f'Benefícios\n')
        for i in range(len(benef)):
            arquivo.write(f'-{benef[i]}\n')
        arquivo.write(f'Link para mais informações: {link}\n\n\n')


print('Bem Vindx ao G.A.B.S.D.E')
print('------------------------')
roda = str(input('Pressione enter para iniciar\n'))

while roda == '':
    print('----------MENU----------')
    menu = str(input('1 - Adicionar estágio\n2 - Modificar estágio\n3 - Excluir estágio\n4 - Acessar arquivo\n'))
    if menu == '1':
        print(add_estagio())
        roda = str(input('\nPressione enter para voltar ao Menu\n'))
    elif menu == '4':
        with open('Estágio.txt', 'r') as arquivo:
            print(arquivo.read())
            roda = str(input('\nPressione enter para voltar ao Menu\n'))









