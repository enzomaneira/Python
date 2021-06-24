"""
Módulo Collections - Ordered Dict


"""
#Em um dicionário a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3}

from collections import OrderedDict

dicionario0 = OrderedDict({'a': 1, 'b': 2, 'c': 3})

for chave, valor in dicionario0.items():
    print(f'chave={chave}: valor={valor}')
