"""
Data e Hora

método buitin integrado datetime
"""

import datetime

print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print(datetime.datetime.now())
print(repr(datetime.datetime.now()))

inicio = datetime.datetime.now()

print(inicio)

inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)
print(inicio)

evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))
print(evento)

nascimento = input('Informe data de nascimento dd/mm/aaaa: ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(evento.year)
print(evento.month)
print(evento.day)

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2021, 4, 14, 0)

tempo_para_evento = aniversario - data_hoje

print(tempo_para_evento)

print(tempo_para_evento.days)

print(f'Faltam {tempo_para_evento.days} dias e {tempo_para_evento.seconds//60//60} horas')

data_da_compra = data_hoje

regra_boleto = datetime.timedelta(days=3)
vencimento_boleto = data_hoje + regra_boleto
print(vencimento_boleto)

hoje = datetime.datetime.today()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())
# 0 = segunda 1 = terça ...

#aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)

import datetime
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.datetime.today()

print(formata_data(hoje))

import timeit

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

import functools

def teste(n):
    soma = 0
    for num in range(n + 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))
