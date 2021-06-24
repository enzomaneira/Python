"""
Módulos

 - Módulos são outros arquivos em Python

Módulo Random -> Possuí varias funções para gerar um valor pseudo-aleatório
"""

from random import random

for i in range(10):
    print(random(), end=', ')


from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído


from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')

from random import choice

jogadas = 'pedra', 'papel', 'tesoura'

print(f'\n{choice(jogadas)}')

from random import shuffle

cartas = ['A', '2', '3', '4', '5', '6', '7', 'J', 'Q', 'K']

print(cartas)
shuffle(cartas)
print(cartas)

print(cartas.pop())

from random import *  # Busca todo o modulo

for i in range(2):
    print(random())

from random import randint as rdi

for i in range(6):
    print(rdi(1, 61), end=', ')


"""
Módulos costumizados

Como módulos Python nada mais são do que arquivos python todos os arquivos que criamos neste
curso são módulos python prontos para ser utilizados.

def soma_impares():
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total


from funcoes_com_parametros import soma_impares

print(soma_impares(1, 2, 3, 4, 5, 6, 7, 9))
"""

from colorama import init, Fore

init()

print(Fore.MAGENTA + '\nÉ A MØB')

# Entrar em https://pypi.org

"""
Pacote Python -> Diretório contendo uma coleção de módulos
"""

from mob import mob1

print(mob1.curso())


