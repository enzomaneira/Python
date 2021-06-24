"""
Checagem de Tipo
"""

idade = 42

print(type(idade))

idade = 'Quarentena e dois'

print(type(idade))

Variavel = False
# Variavel = True  não funciona

# if Variavel:
#     resultado = 1 + 'Mob'
# else:
 #    resultado = 1 + 21

# print(resultado)

class CisneNegro:

    def __len__(self):
        return 42

livro = CisneNegro()

print(len(livro))

nome = 'Enzo Maneira'
lista = [12, 34, 55, 49]
dicio = {'Corinthians': 30, 'São Paulo': 19, 'Santos': 24, 'Palmeiras': 21}

print(len(nome))
print(len(lista))
print(len(dicio))

idade = 42
peso = 91.2

# print(len(idade))   não funciona
# print(len(peso))    não funciona

def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'

print(cumprimentar('Enzo'))

def cabecalho(texto: str, alinhamento: bool =True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()} ".center(50, '#')

print(cabecalho('MLMob'))

print(cabecalho('MLMob', alinhamento=False))

import math

def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

print(circunferencia.__annotations__)

nome: str = 'Enzo'
# idade: int = 20
ativo: bool = True

nomes: list = [1, 2, 3]

from typing import List, Dict

nums: List[int] = [3, 5, 9]

opcoes: Dict[str, bool] = {'enzo': True, 'miguel': False}

print(nums)
print(opcoes)

import random

cartas = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
naipes = '♢ ♠ ♡ ♣'.split()

def criar_baralho(aleatorio=False):
    "Cria baralho com 52 cartas"
    baralho = [(n, c) for c in cartas for n in naipes]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

baralho = criar_baralho(aleatorio=True)

def distribuir_cartas(baralho):
    "Distribui cartas de acordo com o baralho gerado"
    return f'{(baralho[0::4])}\n{(baralho [1::4])}\n{(baralho[2::4])}\n{(baralho[3::4])}'

print(distribuir_cartas(baralho))



