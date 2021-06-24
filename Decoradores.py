"""
Decoradores

 - Funções que envolvem outras funções e aprimora seus comportamentos
 - Sintaxe: '@'
"""

# Decoradores como funções

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia\n')
    return sendo

def saudacao():
    print('Seja bem vindo')

teste = seja_educado(saudacao)

teste()

def saudando(funcao):
    def ando():
        print('Bem vindo bro')
        funcao()
        print('Prazer te conhcer')
    return ando

@saudando
def mob():
    print('É a mob')

mob()


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def dando_oi(nome):
    return f'Oi eu sou {nome}!'


@gritar
def ordenar(prato, acompanhamento):
    return f'Eu vou querer {prato} com {acompanhamento}'


print(ordenar('Bife a parmegiana', 'Batata Frita'))
print(dando_oi('Enzo'))
print(f'\n\n---------------------')
"""
Preservando Metadados

 - Dados intrisecos em arquivos
 
wraps -> funções que envolvem elementos com diversas finalidades

"""

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        """Logando"""
        print(f'Você esta chamando a função {funcao.__name__}')
        print(f'Documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """"Soma dois numeros"""
    return a + b

print(soma(14, 6))
print(soma.__name__)
print(soma.__doc__)


# Resolução
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        print(f'\n---------------------')
        """Logando"""
        print(f'Você esta chamando a função {funcao.__name__}')
        print(f'Documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def Soma(a, b):
    """Soma dois numeros"""
    return a + b

print(Soma(20, 74))

print(Soma.__name__)
print(Soma.__doc__)

"""
Forçando tipo de dados com decoradores

zip 

a = (1, 3, 5)
b = (2, 4, 6)

c = zip(a, b)
(1, 2), (3, 4), (5, 6)
"""

def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vzs):
    for vez in range(vzs):
        print(msg)

repete_msg('Mob', '3')

@forca_tipo(float, float)
def divide(a, b):
    return a/b

divide(15, 3)