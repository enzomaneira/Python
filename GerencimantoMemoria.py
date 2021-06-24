"""
Gerencimento de Memória

t1 = Thread(tarfet=contagem_regressiva, args=(CONTADOR//2,))
t2 = Thread(tarfet=contagem_regressiva, args=(CONTADOR//2,))

inicio = time.time()
t1.start()
t2.star()
t1.join()
t2.join()
fim = time.time()

print(f'Tempo em segundos - {fim - inicio}')

https://edabit.com/challenges/python3

"""

import time
from threading import Thread

CONTADOR = 5000000

def contagem_regressiva(n):
    while n > 0:
        n -=1

inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos - {fim - inicio}')


