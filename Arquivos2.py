"""
Lendo Arquivos CSV

CVS - Comma Separated Values - Valores separados por virgula

# Separador por vírgula

1, 2, 3, 4, 5, 6

# Não ideal

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)

 - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
 - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # pula cabeçalho
    for linha in leitor_csv:
       print(f'{linha[0]} nasceu no/a {linha[1]} e mede {linha[2]} centímetros')  # cada linha é uma lista

Escrevendo Arquivos CSV

writer() -> cria objeto
writerow() -> escreve uma linha

Conhecendo Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização

# Leitura

with open('animais.pickle', 'rb') as arquivo:
    Gato.cachorro = pickle.load(arquivo)
    print(f'O gato se chama {Gato.Animal__nome}')
    Gato.mia()
    print(f'O tipo do gato é {type(Gato)}')

    print(f'O cachorro se chama {Cachorro.Animal__nome}')
    Cachorro.late()
    print(f'Tipo do cachorro é {type(Cachorro)}')

JSON - JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
"""

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_cvs = writer(arquivo)
    filme = None
    escritor_cvs.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = (input('Informe o título do filme: '))
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme: ')
            escritor_cvs.writerow([filme, genero, duracao])


# Pickle

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.__Animal__nome} está miando...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.__Animal__nome} está latindo...')


romeu = Gato('Romeu')
fiel = Cachorro('Fiel')

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((romeu, fiel), arquivo)

import json

ret = json.dumps(['produtos'], {'Playstation 5': ('2TB', 'Novo', '220V', 2340)})

print(type(ret))
print(ret)




