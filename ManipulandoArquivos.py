"""
Leitura de arquivos

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que
neste caso é o caminho a ser lido. Essa função retorna um _io.TextIOWrapper.

mode r -> MOdo de Leitura. r -> read() -> ler
"""

arquivo = open('texto.txt')

print(arquivo)

print(type(arquivo))

print(arquivo.read())


# OBS: O Python utiliza um recurso para trabalhar com arquivos chamada cursor. Esse cursor,
# funciona como o cursor de quando estamos escrevendo.

ret = arquivo.read()

print(type(ret))

"""
Seek e Cursor

seek() -> É utilizado para movimentar o cursor pelo arquivo
"""

arquivo.seek(0)
print(arquivo.read())

ret = arquivo.readline()

print(type(ret))


print(ret)

print(ret.split(' '))

linhas = arquivo.readlines()

arquivo.seek(0)
print(len(linhas))

# 1 - Abre arquivo
arquivo = open('texto.txt')

arquivo.seek(0)
# 2 - Lê arquivo
print(arquivo.read())

# 3 - Fecha arquivo
arquivo.close()

#  Verifica se fechou arquivo
print(arquivo.closed)

"""
Escrevendo em Arquivos


"""

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos é muito facil\n')
    arquivo.write('é a mob, nada mais nada menos\n')
    arquivo.write('última linha')


# with open('frutas.txt', 'w') as arquivo:
  #  while True:
     #   fruta = input('Informe uma fruta ou digite sair: ')
    #    if fruta != 'sair':
     #       arquivo.write(fruta)
      #      arquivo.write('\n')
    #    else:
       #     break

"""
Modos de Arquivos

r -> Abre para leitura - padrão 
w -> Abre para escrita - sobrescreve caso o arquivo exista
x -> Abre para escrita somemente se o arquivo não existir. Caso o arquivo exista, gera TypeError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização leitura e escrita
"""

try:
    with open('uni.txt', 'x') as arquivo:
        arquivo.write('teste de conteúdo\n')
except FileExistsError:
    print('Arquivo ja existe')

""" 
with open('texto.txt', 'a') as arquivo:
    while True:
        integrante = input('Informe nome do integrante: ')
        if integrante != 'sair':
            arquivo.write(integrante)
            arquivo.write('\n')
        else:
            break
"""

with open('novo.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('Topo\n')
    arquivo.seek(50)
    arquivo.write(' entendeu? ')




"""
String IO

ATENÇÃO: para ler ou escrever dados em arquivos do sistema operacional o software precisa
ter permissão:
        - Permissão de leitura -> para ler o arquivo
        - Permissão de escrita -> para escrever o arquivo

StringIO -> utilizado para ler e criar arquivos na memória
"""

# Primeiro fazemos o import
from io import StringIO

mensagem = 'texto normal'

arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

print(arquivo.read)

arquivo.write('Outro texto')
arquivo.seek(0)
print(arquivo.read())

