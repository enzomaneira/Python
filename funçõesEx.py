"""
Exercícios Funções


def exercicio_1(n):
    for i in range(n):
        i += 1
        print(str(i) * i)


n = int(input('Digite um número: '))
exercicio_1(n)

valor = []

def n_esima(n):
        i = 1
        while i <= n:
            valor.append(i)
            print(valor)
            i += 1

n_esima(n)


def soma_multiplos(n1, n2, n3):
    return n1 + n2 + n3

n1 = int(input('Insira um numero inteiro: '))
n2 = int(input('Insira um numero inteiro: '))
n3 = int(input('Insira um numero inteiro: '))

print(soma_multiplos(n1, n2, n3))




def pos_neg(n):
    if n > 0:
        return 'P'
    elif n <= 0:
        return 'N'


n = int(input('Insira numero inteiro: '))
print(pos_neg(n))



def soma_imposto(taxa, preco):
    taxa = preco*taxa/100
    preco = preco + taxa
    return f'preço: R$ {preco}'


preco = float(input('Insira preço do produto: '))
print(f'Preço: R$ {preco}')
taxa = float(input('Insira o percentual da taxa sobre o produto: '))
print(f'Taxa: {taxa}%')

print(f'Preço do produto pós taxa: R$ {soma_imposto(taxa, preco)}')



def converte_hora(h, m):
    if h == 0:
        print(f'00:{m} AM')
    elif h == 12:
        print(f'12:{m} PM')
    elif h > 12:
        h = h - 12
        return f'{h}:{m} PM'
    elif h < 12:
        return f'{h}:{m} AM'


h = int(input('Digite as horas: '))
m = int(input('Digite os minutos: '))
print(converte_hora(h, m))

novamente = str(input('Deseja usar novamente?\n'))

while novamente == 'sim':
    h = int(input('Digite as horas: '))
    m = int(input('Digite os minutos: '))
    print(converte_hora(h, m))
    novamente = str(input('Deseja usar novamente?\n'))
print('fim')


def exercicio8(n):
    s = str(n)
    return len(s)

n = int(input('Digite um número: '))
print(f'A quantidade de algarismos é {exercicio8(n)}')


valorT = taxa = valorF = qtd = 0


def valor_pagamento(valorP, dias):
    juros = (0.1 * dias)
    taxa = (valorP * (juros + 3)/100)
    global valorT
    valorT = valorT + taxa
    valorF = valorP + taxa
    return f'Taxa: R$ {taxa}\nValor a ser pago: R$ {valorF}'


valorP = float(input(f'Insira o valor da prestação: '))

while valorP != 0:
    print(f'Valor da prestação: {valorP}')
    dias = float(input('Insira a quantidade de dias de atraso: '))
    print(valor_pagamento(valorP, dias))
    qtd += 1
    valorP = float(input(f'Insira o valor da prestação: '))
print('\n\nRelatório do Dia')
print('----------------')
print(f'Prestações pagas: {qtd}')
print(f'Valor recebido: R$ {valorT}')



def numero_invertido(n):
    inverte=str(n)
    return inverte[::-1]


n = int(input('Insira número inteiro: '))
print(numero_invertido(n))


from random import randint

def craps():
    dado = str(input('Pressione D para jogar o dado\n'))
    if dado == 'd':
        valor = randint(2,12)
        if valor == 1 or valor == 7:
            print(f'Dado: {valor}\nVocê ganhou!')
        elif valor == 12 or valor == 2 or valor == 3:
            print(f'Dado: {valor}\nCraps! Você perdeu')
        elif valor == 4 or valor == 5 or valor == 6 or valor == 8 or valor == 9 or valor == 10:
            i = valor
            print(f'Jogue novamente! Seu número da vitória agora é {valor}')
            dado = str(input('Pressione D para jogar o dado\n'))
            valor = randint(2, 12)
            if valor == i:
                print(f'Você tirou {valor} novamente você ganhou')
            else:
                if valor == 1 or valor == 7:
                    print(f'Dado: {valor}\nVocê ganhou!')
                elif valor == 12 or valor == 2 or valor == 3:
                    print(f'Dado: {valor}\nCraps! Você perdeu')
                elif valor == 4 or valor == 5 or valor == 6 or valor == 8 or valor == 9 or valor == 10:
                    print(f'Dado: {valor}\nJogue novamente!')
                    dado = str(input('Pressione D para jogar o dado\n'))
                    valor = randint(2, 12)


print(craps())



import random



def exercicio_12():
     s = str(input('Palavra: '))
     embaralha = random.sample(s, len(s)) # String vira lista
     a = ''.join(embaralha) # lista vira string
     return f'Palavra embaralhada: {a}'


print(exercicio_12())



def valor_por_omissao(valor):
    if valor == '':
        return int(1)
    else:
        return faixa_minima_maxima(int(valor))


def faixa_minima_maxima(valor):
    if valor < 1:
        return 1
    elif valor > 20:
        return 20
    else:
        return valor


def cria_linha(linha):
    l = '+'
    for x in range(linha):
        l += '-'
    l += '+'
    print(l)


def cria_coluna(linha, coluna):
    for y in range(coluna):
        c = '|'
        c += ' ' * linha
        c += '|'
        print(c)


def desenha_moldura(linha, coluna):
    cria_linha(linha)
    cria_coluna(linha, coluna)
    cria_linha(linha)


linha = input('Diga quantos +----+, entre 1 e 20: ')
coluna = input('Diga quantos |    |, entre 1 e 20: ')
desenha_moldura(valor_por_omissao(linha), valor_por_omissao(coluna))
"""


def gera_combinacoes(lista, n):
    #  gera tupla com todas as combinações possíveis da soma de três números da lista
    #  que seja iguais a 15.
    for i in lista:
        for j in lista:
            if n + i + j == 15 and (n != i and n != j and i != j):
                combinacoes.append((n, i, j))


def gera_quadro(comb, L1):
    linha1 = L1
    for i in range(len(comb)):
        linha2 = comb[i]
        for j in range(len(comb)):
            linha3 = comb[j]

            if (linha1[0] + linha2[0] + linha3[0] == 15) and \
                    (linha1[1] + linha2[1] + linha3[1] == 15) and \
                    (linha1[2] + linha2[2] + linha3[2] == 15) and \
                    (linha1[0] + linha2[1] + linha3[2] == 15) and \
                    (linha1[2] + linha2[1] + linha3[0] == 15):

                if (linha1[0] not in linha2) and \
                        (linha1[1] not in linha2) and \
                        (linha1[2] not in linha2):
                    print(linha1)
                    print(linha2)
                    print(linha3)
                    print()


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinacoes = []

for n in range(1, 10):
    gera_combinacoes(lista, n)

print()

for L1 in combinacoes:
    gera_quadro(combinacoes, L1)

