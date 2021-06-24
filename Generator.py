"""
Geradores

 - Geradores são Iteradores

Outras Informações:
 - Geradores podem ser criados com funções geradoras
 - Funções geradoras utilizam a palavra reservada Yeld
 - Geradores podem ser cirados por Expressões Geradoras
"""

#  Exemplo de função geradora

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta_ate(10)

print(gen)





