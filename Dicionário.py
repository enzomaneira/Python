"""
Dicionários

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves.

print(type({}))

Sobre Dicionários:
   - Chave e Valor são separados por dois pontos "Chave:Valor"
   - Tanto chave quanto valor pode ser qualquer tipo de dado
   - Podemos misturar tipos de dados
   -Não podem existir chaves repitidas
"""

#Forma 1

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

#Acessando via chave
print(paises.get('br'))

pais = paises.get('ru')

if pais:
    print(f'País {pais} encontrado')
else:
    print('País não encontrado')

#Podemos definir um padrão para caso não encontrarmos o objeto com a chave informada

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {pais}')

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

#Podemos adicionar qualquer tipo de dado como chaves

#Tuplas são boas escolhas de chaves pois são imutáveis

localidades = {
    (12.342, 49.381): 'Escritório São Paulo',
    (12.421, 13.423): 'Escritório no Rio de Janeiro'
}

print(localidades)
print(type(localidades))

#Adicionando elementos

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

receita['abr'] = 250

print(receita)

receita['jan'] = 110

print(receita)

#Removendo elementos

ret = receita.pop('mar')
print(ret)

print(receita)

