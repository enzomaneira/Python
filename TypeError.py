"""
Manipulação de erro
"""

def colore(texto, cor):
    cores = ('amarelo', 'azul', 'verde', 'vermelho')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso em {cor}')

colore(5, 'verde')

"""
0 block try/except

Utilizamos o bloco try/excpet para tratar erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o usuário receba mensagens inesperadas.

A forma geral mais simples é:
   try:
       //execução do problema
   except:
       //o que deve ser feito em casa de problema       
"""

def enzo():
    print('maneiraprog')

# Exemplo 1 - Tratando erro genérico

try:
    enzo()
except:
    print('deu algum problema')

# Tenta executar a função, caso de problema aparece a mensagem

# Exemplo 2 - Tratando erro específico

try:
    enzo()
except TypeError:
    print('Você esta utilizando uma função inexistente')

try:
    enzo()
except NameError:
    print('Você esta utilizando uma função inexistente')

# Exemplo 3 - tratando um erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

try:
    enzo()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')

"""
Try / Except / Else / Finally

Toda entrada deve ser tratada!

Else -> Executa somente se não ocorrer o erro.

Finally -> Geralmente utilizado para fechar ou deslocar recursos
Bloco é sempre executado. Independente se ouve exceção ou não.
"""

# Else

try:
    num = int(input('Informe numero: '))
except ValueError:
    print('valor incorreto')
else:
    print(f'Você digitou {num}')

# Finally

try:
    num = int(input('Informe numero: '))
except ValueError:
    print('valor digitado é inválido')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando finally')

"""
Python Debugger 

 - Para usar é necessário chamar a função breakpoint()
 
Comandos Básicos do PDB
 - l (listar onde estamos no código)
 - n (pular linha)
 - p (imprime variável)
 - c (continua a execução - finaliza debugging)
"""

nome = 'Angel'
sobrenome = 'Romero'
breakpoint()
nomeCompleto = nome + ' ' + sobrenoma
time = 'Corinthians'
final = nomeCompleto + 'jogou no' + time
print(final)














