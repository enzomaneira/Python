"""
Utilizando Lambdas

Lambdas são funções sem nome, ou seja, anônimas.
def funcao(x):
    return 3 * x + 1

print(funcao(4))
"""
calc = lambda x: 3 * x + 1

print(calc(4))

nomeCompleto = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nomeCompleto('enzo', 'maneira'))

mob = lambda: 'é a møb'
print(mob())

mobRapa = ['Enzo Maneira', 'Gabriel Brandelero', 'Gabriel Dias', 'André Maestre', 'Victoria Marques',
           'Livia Urdangarin', 'Mariah Barsotti', 'Bernardo Louzada', 'Thiago Cunha', 'Luiz Augusto',
           'Matheus Aialla', 'Enzo Pedote']

print(mobRapa)

mobRapa.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(mobRapa)

def geraFuncaoQuadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

teste = geraFuncaoQuadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

"""
Map

Com map, fazemos mapeamente de valores para uma função
"""
import math

# Forma Comum
def area(r):
    return math.pi * (r ** 2)

print(area(2.6))

raios = [2, 7.3, 1, 3.12, 11, 4, 4.6]

areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Usando map
areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))

# Usando Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# Apos usar a função map() ele zera
"""
Filter

filter() -> Serve para filtrar dados para uma determinada coleção.
"""
import statistics

# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

# Assim como a função map, a filter recebe 2 parâmetros, sendo uma função
# e um iterável

res = filter(lambda valor: valor > media, dados)
print(list(res))

print(f'Novamente {list(res)}')
# Dados excluidos da memória após serem utilizados

paises = ['Brasil', '', 'EUA', '', 'Argentina']
print(paises)

res = filter(None, paises)
print(list(res))

#Diferença entre map() e filter()

# map -> recebe dois parâmetros, uma função e um iterável, e retorno um objeto mapeando a função para cada elemento do iterável
# filter -> recebe dois parâmetros, uma função e um iterável, e retorno um objeto filtrando apenas os elementos de acordo com a função

# Exemplo mais complexos

usuarios = [
    {'user': 'MLEnzo', 'tweets': ['Vai Corinthians', 'sarah la maga joga y joga']},
    {'user': 'Chef g', 'tweets': ['gabsdormindo', 'saudades fvarios', 'é a mob familia']},
    {'user': 'MLBrand', 'tweets': []},
    {'user': 'LiCFO', 'tweets': ['bom dia seguimores']},
    {'user': 'Vic Marx', 'tweets': ['Estágio hoje foi cansativo', 'aiai tem gente que nao cansa']},
    {'user': 'ML420', 'tweets': []}
]

print(usuarios)

# filtrar usuarios inativos

# inativos = list(filter(lambda usuario: len(usuario['tweets']) > 0, usuarios))
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

# Combinar filter e maps

nomes = ['enzo', 'dé', 'gabriel']

lista = list(map(lambda nome: f'Instrutor: {nome}', filter(lambda nome: len(nome) > 5, nomes)))
print(lista)

"""
Any e All

all() - Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
"""

print(all([1, 2, 3, 4]))  # Todos são True

print(all(['Enzo']))  # True

print(all([0, 2, 5, 9]))  # 0 = False

print(all(letra for letra in 'Raffa Moreira mano' if letra in 'abcdefghijklmnopqrstuvwxyz'))

nomes = ['Miguel', 'Michelle', 'Maria']

print(all([nome[0] == 'M' for nome in nomes]))

"""
Any

 - Retorna se algum for verdadeiro
"""

times = ['Santos', 'Corinthians', 'Corinthians', 'São Paulo', 'Palmeiras', 'São Paulo', 'Palmeiras', 'Corinthians']

print(any([time == 'Corinthians' for time in times]))

"""
Generators

Em aulas anteriores nós estudamos:
 - List Comprehension
 - Dictionary Comprehension
 - Set Comprehension

Não vimos:
 - Tuple Comprehension
"""

nomeT = ['Enzo', 'Miguel', 'Alexandre', 'Priscilla']

print(any([nome[0] == 'A'for nome in nomeT]))

# Generator
res = (nome[0] == 'E' for nome in nomeT)
print(type(res))
print(res)

# sizeof
from sys import getsizeof

print(getsizeof('Enzo Maneira'))
print(getsizeof(39402))
print(getsizeof(nomeT))
print(getsizeof(True))
print(getsizeof(False))

"""
Sorted

 - Não confundir com sort() em listas, sorted() pode ser usado em qualquer iterável
"""

numeros = {52, 43, 102, 201, 4, 72}
print(sorted(numeros))
print(sorted(numeros, reverse=True))

usuarios = [
    {'user': 'MLEnzo', 'tweets': ['Vai Corinthians', 'sarah la maga joga y joga']},
    {'user': 'Chef g', 'tweets': ['gabsdormindo', 'saudades fvarios', 'é a mob familia']},
    {'user': 'MLBrand', 'tweets': []},
    {'user': 'LiCFO', 'tweets': ['bom dia seguimores']},
    {'user': 'Vic Marx', 'tweets': ['Estágio hoje foi insuportavel', 'aiai tem gente que nao cansa']},
    {'user': 'ML420', 'tweets': []}
]

print(sorted(usuarios, key=len))
print(sorted(usuarios, key=lambda usuario: usuario['user']))
print(sorted(usuarios, key=lambda usuario: usuario['tweets'], reverse=True))

musicas = [{'título': 'Foreplay', 'tocou': 23},
           {'título': 'Highest Room', 'tocou': 72},
           {'título': 'Bandit', 'tocou': 54},
           {'título': 'Rockstar', 'tocou': 109},
           {'título': 'The Box', 'tocou': 142},]

# Ordem da menos a mais tocadas
print(sorted(musicas, key=lambda musica: musica['tocou']))

print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

print(min(times))

print(min(times, key=lambda times: len(times)))

print(max(musicas, key=lambda musica: musica['tocou'])['título'])
print(max(musicas, key=lambda musica: musica['tocou'])['tocou'])
print(max(musicas, key=lambda musica: musica['tocou']))

print(max(musicas, key=lambda musica: len(musica['título'])))

print('Enzo Maneira'.__len__())

print(abs(-5))
print(abs(-4.24))
print(abs(4.2))

dic = {'a': 1, 'b': 5, 'c': 2, 'd': 10}
print(sum(dic.values()))

"""
Zip

 - Cria iterável chamado zip object que agrega elementos de cada um dos iteráveis passados como entrada em pares
"""

listaz = [1, 2, 3]
listax = [4, 5, 6]

zip1 = zip(listaz, listax)
print(zip1)
print(type(zip1))

# print(list(zip1))
# print(tuple(zip1))
# print(set(zip1))
print(dict(zip1))

lista3 = [7, 8, 9, 10]

zip1 = zip(listaz, listax, lista3)
print(list(zip1))

prova1 = [20, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Enzo', 'Brand', 'Gabs']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)