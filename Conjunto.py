"""
Conjuntos

- Teoria dos conjuntos da matemática

- Conjuntos são chamados de Sets

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, não são indexados;

Conjuntos são bons para armazenar elementos mas não nos importamos com sua ordem.
Quando não há preocupação com chaves, valores e itens duplicados.

OS conjuntos (Sets) são referenciados em python com chaves {}

Diferenças entre conjuntos (Sets) e Mapas (Dicionários) em Python
     - Um dicionário tem chave/valor;
     - Um conjunto tem apenas valor;
"""

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)
print(type(s))
#Obs: ao criar um conjunto ao add um valor ja existente, o mesmo será ignorado sem gerar erros

s = {1, 2, 3, 4, 5}
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

#Além de não existir valor duplicado, também não existe ordem

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto = {conjunto} com {len(dicionario)} elementos')

for valor in s:
    print(valor)

#Usos interessantes com sets

#Imagine que foi feito um formulario de cadastro de visitantes
#Visitantes informam manualmente cidades de onde vieram

#Cada cidade foi add em uma lista python, já que em uma lista é possível add novos elementos e ter repetição

cidades = ['Santos', 'Belo Horizonte', 'São Paulo', 'Santos', 'Rio de Janeiro', 'Santos', 'Cuiabá']

print(cidades)
print(len(cidades))

#Para saber quantas cidades diferentes possuem na lista usamos conjunto

print(len(set(cidades)))

#Add elementos em um conjunto

s = {1, 2, 3}
print(s)

s.add(4)
s.add(4) #Duplicidade não gera erro, somente é ignorada
print(s)

s.discard(2) #Valor a ser removido (conjuntos não são indexados)
print(s)

n = s.copy()
print(n)

n.add(6)
print(n)
print(s)

#Métodos matemáticos

estudantesPython = {'Enzo', 'Mello', 'Bat', 'Gordão', 'Stef'}
estudantesJava = {'Stef', 'Lucas', 'Felps', 'Mello'}

#Precisamos gerar um conjunto com nomes de estudantes unicos

#Forma 1 - Utilizando boolean

unicos1 = estudantesPython.union(estudantesJava)
print(unicos1)

#Forma 2
unicos2 = estudantesPython | estudantesJava
print(unicos2)

#Conjunto de estudante que estão em ambos cursos

ambos1 = estudantesPython.intersection(estudantesJava)
print(ambos1)

ambos2 = estudantesPython & estudantesJava
print(ambos2)

apenasJava = estudantesJava.difference(estudantesPython)
print(apenasJava)

apenasPython = estudantesPython.difference(estudantesJava)
print(apenasPython)

print(sum(s))
print(max(s))
print(min(s))
print(len(s))


