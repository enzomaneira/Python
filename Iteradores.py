"""
Iteradores

Iterator ->
 - Objeto de programação que pode ser iterado
 - Objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterables ->
 - Um objeto que irá retornar um iterator quando a função iter() for chamada.

"""

nome = 'Enzo'  # Iterable
nums = [1, 2, 3, 4, 5, 6]  # Iterable

it1 = iter(nome)
it2 = iter(nums)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

for letra in nome:
    print(f'{letra}')
