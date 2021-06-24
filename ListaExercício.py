"""

Listas



vetor = [1, 4, 9, 22, 18]

i = 0
while i < len(vetor):
    print(vetor[i])
    i = i + 1


vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(vetor[::-1])


lista = []

i = 0
consoantes = 0

while i <= 10:
    lista.append(str(input('Insira uma letra: ')))
    char = lista[i]
    i = i + 1
    if(char not in ('a','e','i','o','u')):
        consoantes += 1
    if (char not in ('a', 'e', 'i', 'o', 'u')):
        print(lista)

print(consoantes)


lista = []
par = []
impar = []

i = 0

for i in range(20):
    lista.append(int(input('Insira um número: ')))
    num = lista[i]
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(lista)
print(par)
print(impar)



mediaList = []
finalList = []
notaAluno = 0
i = 1
nota = 0

for i in range(10):
    n1 = float(input('Insira N1: '))
    n2 = float(input('Insira N2: '))
    n3 = float(input('Insira N3: '))
    n4 = float(input('Insira N4: '))
    media = (n1 + n2 + n3 + n4)/4
    print(media)
    mediaList.append(media)
    media = mediaList[i]
    i = i + 1
    if media >= 7:
        finalList.append(media)
        print(finalList)

print('FINISH')


vetor = []


for i in range(5):
    pot = 0
    i = i + 1
    num = int(input('Insira número no vetor: '))
    vetor.append(num)
    produto = 0
    for num in vetor:
        produto *= num



print(vetor)
print(sum(vetor))
print(produto)



idades = []
alturas = []

for valor in range(0, 5):
    idades.append(int(input("Digite a idade: ")))
    alturas.append(float(input("Digite a altura: ")))

for valor in range(0, 5):
    print("Idades na ordem inversa: ")
    print(idades[len(idades)-1-valor])


for valor in range(0, 5):
    print("Alturas na ordem inversa: ")
    print(alturas[len(alturas)-1-valor])



vetorA = []
vetorB = []

for i in range(0,10):
    vetorA.append(int(input('Insira número: ')))
    num = vetorA[i]
    num = num * num
    vetorB.append(num)

print(vetorB)


vetorA = []
vetorB = []


for i in range(0,10):
    vetorA.append(input('Insira elemento no Vetor A: '))

print(vetorA)

for i in range(0,10):
    vetorB.append(input('Insira elemento no Vetor B: '))

print(vetorB)

vetorC = []

j = 0

for j in range(0,10):
    vetorC.append(vetorA[j])
    vetorC.append(vetorB[j])

print(vetorC)




idade = []
altura = []

i = 0
soma = 0

for i in range(0, 30):
    idade.append(float(input('Insira idade: ')))
    altura.append(float(input('Insira altura: ')))

while i < len(altura):
    soma += altura[i]
    i = i + 1
    media = soma/len(altura)

k = 0
qtd = 0

while k < len(idade):
    if idade[k] > 13 and altura[k] < media:
        qtd = qtd + 1
    k = k + 1
print(f'Quantidade de alunos com mais de 13 anos e altura acima da média:   {qtd} alunos')



temperatura = []
meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
'Novembro', 'Dezembro']
media = 0
acimaMedia = {}
for i in range(len(meses)):
    temperatura.append(float(input(f'Informe a Temperatura media de {meses[i]} :\n')))
    media += temperatura[i]

media = media/len(meses)

for i in range(len(meses)):
    if (temperatura[i] > media):
        acimaMedia.update({meses[i]: temperatura[i]})
        i += 1

print(acimaMedia)


lista = []
acimaMedia = []
i = k = soma = 0
maior7 = []

num = int(input('Insira um número inteiro: '))

while num >= 0:
    lista.append(num)
    num = float(input('Insira um número inteiro: '))
else:
    print(f'Quantidade de elementos {len(lista)}')
    print(lista)
    lista.reverse()
    print(lista)
    lista.reverse()
    print(sum(lista))
    soma = sum(lista)
    media = soma/len(lista)
    print(media)
    for i in range(len(lista)):
        if lista[i] > media:
            acimaMedia.append(lista[i])
            i += 1
    print(acimaMedia)
    print(len(acimaMedia))
    for k in range(len(lista)):
        if lista[k] > 7:
            maior7.append(lista[k])
            k += 1
    print(maior7)
    print(len(maior7))
    print('Fim')


listaA = []
listaB = []
listaC = []
listaD = []
listaE = []
listaF = []
listaG = []
listaH = []
listaI = []

venda = 1

while venda > 0:
    venda = float(input('Insira o valor de venda da semana: '))
    salario = (venda * 0.09) + 200
    if (salario > 200) and (salario < 299):
        listaA.append(salario)
        print(listaA)
    if (salario > 299) and (salario < 399):
        listaB.append(salario)
        print(listaB)
    if (salario > 400) and (salario < 499):
        listaC.append(salario)
        print(listaC)
    if (salario > 500) and (salario < 599):
        listaD.append(salario)
        print(listaD)
    if (salario > 600) and (salario < 699):
        listaE.append(salario)
        print(listaE)
    if (salario > 700) and (salario < 799):
        listaF.append(salario)
        print(listaF)
    if (salario > 800) and (salario < 899):
        listaG.append(salario)
        print(listaG)
    if (salario > 900) and (salario < 999):
        listaH.append(salario)
        print(listaH)
    if salario > 1000:
        listaI.append(salario)
        print(listaI)

print(f'Vendedores que ganharam até 299: {len(listaA)}')
print(f'Vendedores que ganharam entre 300 e 299: {len(listaB)}')
print(f'Vendedores que ganharam entre 400 e 299: {len(listaC)}')
print(f'Vendedores que ganharam entre 500 e 299: {len(listaD)}')
print(f'Vendedores que ganharam entre 600 e 299: {len(listaE)}')
print(f'Vendedores que ganharam entre 700 e 299: {len(listaF)}')
print(f'Vendedores que ganharam entre 800 e 299: {len(listaG)}')
print(f'Vendedores que ganharam entre 900 e 299: {len(listaH)}')
print(f'Vendedores que ganharam mais de 1000: {len(listaI)}')

saltos = []

nome = str(input('Nome do atleta: '))


while nome != '':
    i = 0
    ct = 1
    for i in range(5):
        saltos.append(float(input(f'Insira a distância do salto {ct}: ')))
        i += 1
        ct += 1
    else:
        soma = sum(saltos)
        media = soma / len(saltos)
        print('\nResultado Final\n')
        print(f'Atleta: {nome}')
        print(f'Saltos: {saltos}')
        print(f'Média dos saltos: {media}m\n\n')
        nome = str(input('Nome do atleta: '))


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


vetorAbono = []
vetorSalario = []

inicio = str(input('Pressione Enter para inciar\n'))

if inicio == '':
    salario = float(input('Salário atual do funcionário: '))

    while salario != 0:
        vetorSalario.append(salario)
        if salario < 500:
            valorAbono = 100
            vetorAbono.append(valorAbono)
            salario = float(input('Salário atual do funcionário: '))
        else:
            valorAbono = salario * 20 / 100
            vetorAbono.append(valorAbono)
            salario = float(input('Salário atual do funcionário: '))

print('Salário    Abono')
print('-----------------')
i = 0
abonoMin = vetorAbono.count(100)

while i < len(vetorSalario):
    print(f'R${vetorSalario[i]} - R${vetorAbono[i]}')
    i += 1
print(f'\nForam processados {len(vetorSalario)} colaboradores\n')
print(f'Total gasto com abonos: R${sum(vetorAbono)}')
print(f'Foram entregues {abonoMin} valores mínimos de abono\n')
print(f'Maior valor pago em abono: {max(vetorAbono)}')
"""

listaNome = []
listaKm = []

print('Comparativo Consumo de Combustível\n')

ct = 1

inicio = str(input('Pressione Enter para Iniciar\n\n'))

if inicio == '':
    for j in range(5):
        print(f'Veículo {ct}')
        nome = str(input('Nome: '))
        listaNome.append(nome)
        km = float(input('Km por litro: '))
        listaKm.append(km)
        ct += 1


print('\nRelatório Final')
i = 0

while i < len(listaNome):
    sub = listaKm[i]
    milKm = 1000 / sub
    print(f'{i + 1} - {listaNome[i]}     -   {listaKm[i]} Km/L - '
          f'{round(milKm, 1)} litros - R$ {round(milKm * 2.25, 2)}')
    i += 1

maior = -1
k = 0
c = 0

for c in range(5):
    if maior < listaKm[k]:
        maior = listaKm[k]
        indice = k
        k += 1
    else:
        k += 1

print(f'O menor consumo é do {listaNome[indice]}')











