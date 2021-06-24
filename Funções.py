"""
Definindo Funções
 - Funções são pequenos trechos de código que realizam uma determinada função

Obs: Se você escreve uma função que executa variás tarefas;
é melhor faze-la de um jeito simples

Exemplo:
 - print()
 - len()
 - max()
 - min()
 - count()

 Em Python a forma geral de definir função é:

def nome_da_função(parâmetros de entrada):
    bloco_da_função

Onde:

nome_da_função -> sempre com letras maiusculas e palavras separadas por underline
parâmetros_de_entrada -> opcionais, podendo ter mais de um, separados por virgulas
bloco_da_função -> também chamada de corpo da função, é onde o processamento da função acontece.
Neste bloco pode ter ou não o retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python
que estamos definindo uma função

OBS: Em Python quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções em Python que retornam valores, devem retornar estes valores com a palavra reservada return

Sobre a palavra reservada 'return':

1 - Ela finaliza a função, ela sai da execução da função.
2 - Podemos ter, em uma função, diferentes return
3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores

Funções com parâmetro (de entrada)

 - Funções que recebem dados para ser processados dentro da mesma

 Se a gente pensar em um programa qualquer:

entrada -> processamento -> saída

Temos funções que:
 - Não tem entrada
 - Não tem saída
 - Possuem entrada, mas não saída
 - Possuem saída, mas não entrada
 - Possuem entrada e saída

 OBS: Em funções Python os parâmetro com valor default são colocados após os valores que
 não são default.

 OBS: Se tivermos uma variável local com o mesmo nome de uma global, a local tera preferência.

Documentando funções com Doc Strings

 OBS: Podemos ter acesso a documentação de uma função em Python
 utilizando a propriedade especial __doc__

Podemos também acessar pela função help()

Entendendo o *args

 - O *args é um parâmetro como outro qualquer. Isso significa que você poderá
 chamar de qualquer coisa, desde que comece com asterísco.

Exemplo

 *xis

Mas por convenção utilizamos *args para defini-lo

O que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras, informados como entrada em uma tupla.
Então desde já lembre-se que tuplas são imutáveis.

**kwargs

Este é só mais um parâmetro que coloca os valores extras em uma tupla, e **kwargs
exige que coloquemos parâmetros nomeados, e trasnferes esses para um dicionário.

Nas nossas funções podemos ter NESTA ORDEM:

 - Parâmetros obrigatórios
 - *args
 - Parâmetros default
 - **kwargs

"""

#Exemplo

cores = ['verde', 'azul', 'amarelo', 'branco']

print(cores)

curso = 'Curso Python'

print(curso)

cores.append('roxo')

cores.clear()
print(cores)

#Definindo a primeira função

#def diz_oi():
  #  print('oi')

# Obs: 1- veja que dentro das nossas funções podemos utilizar outras funções
# 2 - A função faz apenas uma tarefa
# 3 - A função não recebe nenhum parâmetro de entrada
# 4 - Veja que está função não retorna nada

#Chamando função
# diz_oi()    # Nunca esqueça o paratenses

#def cantar_parabens():
  #  print('Parabéns pra você')
 #   print('Nessa data querida')
  #  print('Muitas felicidades')
  #  print('Muitos anos de vida')

#for n in range(2):
    #cantar_parabens()

#Funções com retorno

numeros = [1, 2, 3]

ret = numeros.pop()
print(ret)

ret_pr = print(numeros)
print(ret_pr)



def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()

print(f'Retorno {ret}')

#Refatorando a 1 função

def diz_oi():
    return 'Oi'

alguem = 'Pedro'

print(diz_oi() + alguem)

def nova_função():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_função())


def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1)
print(num2)
print(num3)
print(num4)

#Vamos criar uma função para jogar uma moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randomico entra 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())

def quadrado(numero):
    return numero ** 2

print(quadrado(2))

ret = quadrado(6)
print(ret)

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}')

cantar_parabens('Enzo')

def soma(a, b):
    return a + b

def multiplicacao(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplicacao(4, 5))
print(multiplicacao(2, 8))

print(outra(3, 2, 'Enzo'))

# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Enzo', 'Maneira'))

# A diferença entre parâmetros e argumentos

# Parâmetros são variáveis declaradas na definição da função
# Argumentos são dados passados durante a execução de uma função

# A ordem dos parâmetros importa

print(nome_completo(sobrenome='Maneira', nome='Enzo'))

# Funcões com parâmetro padrão

print('Enzo')

print() # Na função print o parâmetro é opcional

# quadrado() # Na função quadrado o parâmetro é obrigatório

def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))   # 2 ao cubo
print(exponencial(2))    #Como potencial é igual a 2, o parâmetro potencia é opcional

def soma(num1, num2):
    return num1 + num2

print(soma(4, 6))
# print(soma(4))   type error
# print(soma())    type error

def mostra_informação(nome='Enzo', instrutor=False):
    if nome == 'Enzo' and instrutor:
        return 'Bem vindo instruto Enzo'
    elif nome == 'Enzo':
        return 'Pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informação())
print(mostra_informação(instrutor=True))
print(mostra_informação(True))
print(mostra_informação('Miguel'))
print(mostra_informação(nome='Ale'))

# Quais tipos de dados podemos usar como valores default para parâmetro?
# - Qualquer um: string, int, float, booleanos, listas, tuplas, dicionários, funções, etc

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

instrutor = 'Enzo'

def fala_oi():
    instrutor = 'Maneira'
    return f'Oi {instrutor}'

print(fala_oi())

total = 0

def incrementa():
    global total    # Utilizando variável global dentro de uma função

    total += 1
    return total

print(incrementa())

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()

print(fora())
print(fora())
# print(dentro()) type error

# Documentando funções com Doc Strings

def diz_tchau():
    """ Uma função simples que retorna a string tchau """
    return 'Tchau!'

# *args

def soma_todos_numeros(*args):
    return(sum(args))

numeros = 1, 5, 7, 12
print(soma_todos_numeros(2, 4, 7))
 # print(soma_todos_numeros(numeros)) type error

# Desempacotador
numeros = [12, 5, 8, 20]
num1, num2, num3, num4 = numeros
print(soma_todos_numeros(*numeros))

# asteríscos serve para informar que estamos passando
# como argumento uma coleção de dados, assim ele sabe que
# precisa desempacotar

def verifica_info(*args):
    if 'Enzo' in args and 'Maneira' in args:
        return 'Olá Enzo'
    return 'Eu não sei quem você é...'

print(verifica_info())
print(verifica_info(1, True, 'Maneira', 'Enzo'))
print(verifica_info(1, 'Maneira', 3.14))


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(enzo='Rosa', livia='Azul', brand='verde', michelle='roxo')

# OBS: nem os parâmetro *args e **kwargs são obrigatórios

cores_favoritas()
cores_favoritas(enzo='rosa')

def cumprimento_especial(**kwargs):
    if 'enzo' in kwargs and kwargs['enzo'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Enzo!'
    elif 'enzo' in kwargs:
        return f"{kwargs['enzo']} enzo"
    return 'Não sei quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(enzo='Python'))
print(cumprimento_especial(enzo='Oi'))
print(cumprimento_especial(enzo='especial'))

def minha_função(nome, idade, *args, solteiro=True, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_função('Enzo', 19, 1, 6, 10, solteiro=True, java=False, python=True)

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Enzo', 'sobrenome': 'Maneira'}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 4, 5]
tupla = 1, 4, 5
conjunto = {1, 4, 5}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicinario = dict(a=1, b=2, c=3)

# OBS: os nomes das chaves no dicionário precisam ser os mesmos dos parâmetros

soma_multiplos_numeros(**dicinario)

def soma_multiplos_numeros2(a, b, c, **kwargs):
    print(a + b + c)

soma_multiplos_numeros2(**dicionario, lang='Python')
