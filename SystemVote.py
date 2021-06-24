"""
Enzo Maneira Canatella Madalena
20/02/2021
Santos - SP
"""

# Criando com 6 primeiros elementos livres para a contagem dos votos
vetor = [0] * 6

# Criando vetor com as opções disponíveis
opcoes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']

# Declarando variável que vai somar o total de votos
total = 0

print('Qual melhor sistema operacional para uso em um servidor?\n')
inicio = str(input('As possíveis respostas são:\n\n'
                   '1 - Windows\n2 - Unix\n3 - Linux\n4 - Netware\n5 - MacOs\n6 - Outros\n\nPressione '
                   'Enter para iniciar '))

# Looping para votar
if inicio == '':
    resp = int(input('\nResposta: '))
    while resp != 0:
        if resp > 6 or resp < 0:
            print('Respota Inválida\n')
            resp = float(input('\nResposta: '))
        else:
            vetor.append(resp)   # Add voto na lista
            vetor[resp - 1] += 1  # Add voto para o elemento correpondente ao sistema na lista
            total += 1
            resp = int(input('\nResposta: '))

# Mostragem do resultado
print('Sistema Operacional     Votos  %')
print('----------------------------------')
ct = 0
maiorVoto = 0

# Laço criado para imprimir a tabela com os 6 sistemas
for s in range(6):
    c = vetor[ct]    #  Transforma o total de votos do vencedor em uma variável
    print(f'{opcoes[ct]}   {vetor[ct]}   {float(c * 100) / (len(vetor) - 6)}')
    ct += 1
    if vetor[ct] > vetor[maiorVoto]:
        maiorVoto = ct
c = vetor[maiorVoto]
print(f'\nO mais votado foi {opcoes[maiorVoto]} com {vetor[maiorVoto]} votos e'f' porcentagem de '
      f'{float(c * 100)/ (len(vetor) - 6)}%')
