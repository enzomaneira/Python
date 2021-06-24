"""
Módulo Collections - Deque

Lista de alta perfomance
"""
from collections import deque

deq = deque('Enzo')
print(deq)

#Add elementos

deq.append('M')
print(deq)

deq.appendleft('ML')
print(deq)

#Remover elementos

print(deq.pop())
print(deq)

print(deq.popleft())
print(deq)

#Testando

deq.appendleft('CEO = ML')
print(deq.pop())
deq.append('ø')
print(deq)


