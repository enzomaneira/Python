"""
Sistemas de Arquivos e Navegação

Path - Caminho completo até o arquivo no diretório

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos
importar e fazer uso do módulo OS.

os -> Operational System

# Criando Arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass


# Forma não funciona no Mac

os.mknod('arquivo-teste0.txt')

os.mknod('/Users/enzomaneira/OneDrive - Fundação São Paulo/Python')


Criar diretórios

os.mkdir('/Users/enzomaneira/OneDrive - Fundação São Paulo/templates')

Renomear arquivos e diretórios

os.rename('ArquivoExistente', 'NovoArquivo.txt')
os.remove('Arquivo.txt')
"""
import os, sys

# getcdw -> pega o current work directory
# Retorna o path absoluto
print(os.getcwd())

# Para mudar diretório podemos usar o chdir()
os.chdir('..')

print(os.getcwd())


os.chdir('..')

print(os.getcwd())


os.chdir('..')

print(os.getcwd())
# Chegou na raiz!

# Podemos checar se um diretório é absoluta ou relativo

print(os.path.isabs('/Users/enzomaneira/OneDrive - Fundação São Paulo'))  # Absoluta
print(os.path.isabs('enzomaneira/OneDrive - Fundação São Paulo'))  # Relativa

print(os.name)  # Mac e Linux = posix


print(sys.platform)

print(os.getcwd())

res = os.path.join(os.getcwd(), '/Users/enzomaneira')

os.chdir(res)

print(os.getcwd())

print(os.listdir())
print(len(os.listdir()))


print(os.path.exists('/Users/enzomaneira'))

import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('enzo maneira\n')
        arquivo.close()
    input()

#  Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
#  um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
#  os arquivos temporários 'vivos' dentro do bloco with

#  OBS: possívelmente, o código acima não irá funcionar se você estiver utilizar
#  o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos temporários

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'MLMob\n')
    tmp.seek(0)
    arquivo.close()
    print(tmp.read())