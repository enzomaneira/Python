"""
List Comprehension

 - Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
 iterável.

 # Sintaxe

 [ dado for in iterável ]

  # Obs: para entender melhor o que está acontecendo, devemos dividir a expressão em duas partes:
  - Primeira parte: for numero in numeros
  - Segunda parte: numero * 10

 Podemos adicionar estruturas condicionais lógicas às nossas List Comprehension

Listas Aninhadas

 - Algumas linguagens de programação(C/Java) possuem uma estrutura de dados chamada arrays:
      - Unidimensionais (arrays/vetores):
      - Multidimensionais (matrizes):

Em Python nós temos as Listas

lista = [1, 'b', 3.14, True, 5]

Dictionary Comprehension

 Sintaxy

 {chave:valor for valor in iteravel}
"""
numeros = [1, 2, 3, 4, 5, 6]

res = [numero * 10 for numero in numeros]
print(res)

res2 = [numero / 2 for numero in numeros]
print(res2)

def funcao(valor):
    return valor * valor

res3 = [funcao(numero) for numero in numeros]
print(res3)


numerosDobrados = []

for numero in [1, 2, 3, 4, 5]:
    numerosDobrados.append(numero * 2)

print(numerosDobrados)

print([numero * 2 for numero in [1, 2, 3, 4, 5]])

nome = 'Enzo Maneira'

print([letra.upper() for letra in nome])

amigos = ['Dé', 'Livia', 'Brand', 'Gabs', 'Victoria', 'Mariah', 'Thiago']

def maisculo(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

print([maisculo(amigo) for amigo in amigos])

print([numero * 3 for numero in range(1, 10)])

print([bool(valor) for valor in [0, [], '', True, 1, 3, 15]])

print([str(numero) for numero in range(1, 6)])

pares = ([numero for numero in numeros if numero % 2 == 0])
impares = ([numero for numero in numeros if numero % 2 !=0])

print(f'Par: {pares}')
print(f'Ímpar: {impares}')

# Qualquer número par módulo 2 é 0 e 0 em Python é falso
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(f'Par: {pares}')
print(f'Ímpar: {impares}')

res4 = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res4)

listas = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]] # Matrizes 3 x 3

print(listas)
print(type(listas))

print(listas[0][1]) # 2
print(listas[2][1]) # 8

for lista in listas:
    for num in lista:
        print(num)

[[print(valor) for valor in lista] for lista in listas]

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

velha = [['x' if numero % 2 == 0 else 'o' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Dicionary Comprehension

numDic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

quadrado = {chave: valor ** 2 for chave, valor in numDic.items()}

print(quadrado)

num = [1, 2, 3, 4, 5]

quadradoLista = {valor: valor ** 2 for valor in num}
print(quadradoLista)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mix = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mix)

res5 = {valor: ('par' if valor % 2 == 0 else 'impar') for valor in valores}
print(res5)
