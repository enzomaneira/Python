"""
Mapas
-Conhecidos em python como dicionários
"""

receita = {'Jan': 100, 'Fev': 200, 'Mar': 150}

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} a receita foi de {receita[chave]} reais')

for chave in receita.keys():
    print(receita[chave])

for valor in receita.values():
    print(valor)

#Desempacotamento de dicionários

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

#Soma, Valor Max, Valor Min, Tamanho (int ou float)

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))


