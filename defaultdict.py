"""
Módulo Collections - Default Dict

Default Dict -> Ao criar um dicionário utilizando-o, informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não exista, essa chave será
criada e o valor default será atribuído.

*Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar variáveis

"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['MLMob'] = 'Enzo Maneira'

print(dicionario)

print(dicionario['outro'])

print(dicionario)