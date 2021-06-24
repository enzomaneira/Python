"""
Módulo Collections - Counter

Colletions -> High-Performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.

"""

from collections import Counter

lista = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5]

#Utilizando o counter
res = Counter(lista)

print(type(res))

print(res)

print(Counter('Enzo Maneira'))

texto = 'De acordo com o TMZ, o suspeito disse aos policiais que a casa de DeRozan não era seu alvo pretendido '
'ele estava tentando chegar à casa de Kylie Jenner, mas cometeu um erro. '
'O homem acabou sendo preso e recebeu uma acusação de roubo.'

palavras = texto.split()

res = Counter(palavras)

print(res)

print(res.most_common(5))
