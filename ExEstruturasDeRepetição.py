""""
user = input('Insira o nome usuário: ')
print(f'Userário: {user}')

senha = input('Insira a senha: ')

confsenha = input('Insira senha novamente: ')

while senha != confsenha:
   print('senhas incompativeis')
   confsenha = input('Insira senha novamente: ')
else:
    print('Cadastrado com sucesso')


print('Cadastro')

user = str(input('Insira nome do usuário: '))

while (len(user) <= 3):
    print('Usuário deve ter mais de 3 caracteres')
    user = str(input("Insira usuário novamente: "))
else:
    print(f'Usuário: {user}')

idade = int(input('Insira sua idade: '))

while idade > 150 or idade < 0:
   print('Idade Inválida')
   idade = int(input('Insira idade novamente: '))
else:
    print(f'Idade: {idade}')

salario = int(input('Insira seu salário:  '))

while salario < 0:
    print('Salário Inválido')
    salario = int(input('Insira seu salário: '))
else:
    print(f'Salário: {salario}')

sexo = str(input('Insira seu sexo: '))

while sexo != 'M'and sexo != 'F':
    print('Sexo Inválido')
    sexo = str(input('Insira seu sexo: '))
else:
    print(f'Sexo: {sexo}')

print(f'Usuário: {user}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo}')


angelandia = float(input('Insira a população de Angelândia:  '))
cA = float(input('Insira o crescimento anual(%) de Angelandia: '))

boloville = float(input('Insira a população de Boloville:  '))
cB = float(input('Insira o crescimento anual(%) de Boloville: '))

crescA = cA * 0.01
crescB = cB * 0.01

ano = 2020

tempo = 0

print(f'-----------RELATÓRIO {ano}-----------')
print(f'População Angelåndia: {angelandia}\nCrescimento anual: {cA}%\nPopulação Boloville: {boloville}\n'
          f'Crescimento Anual: {cB}%\nTempo de demora: {tempo} anos\nDiferença: {boloville - angelandia}\n\n ')

while angelandia < boloville:
    angelandia = angelandia + angelandia*crescA
    boloville = boloville + boloville*crescB
    ano = ano + 1
    tempo = tempo + 1
    print(f'-----------RELATÓRIO {ano}-----------')
    print(f'População Angelåndia: {angelandia}\nCrescimento anual: {cA}%\nPopulação Boloville: {boloville}\n'
          f'Crescimento Anual: {cB}%\nTempo de demora: {tempo} anos\nDiferença: {boloville - angelandia}\n\n ')
else:
    print(f'-----------RELATÓRIO {ano}-----------')
    print(f'População Angelåndia: {angelandia}\nCrescimento anual: {cA}%\nPopulação Boloville: {boloville}\n'
          f'Crescimento Anual: {cB}%\nTempo de demora: {tempo} anos\nDiferença: {boloville - angelandia}\n\n ')


num = 1

while num < 20:
    print(num, end=' ')
    num = num + 1
else:
    print(num)



n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
n4 = int(input('Insira o quarto número: '))
n5 = int(input('Insira o quinto número: '))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
if n5 > maior:
    maior = n5


print(f'Maior número = {maior}')



num = 1

while num < 150:
    num = num + 1
    if num % 2 == 0:
        print(num, end='  ')



n1 = int(input('Insira o primeiro número:  '))
n2 = int(input('Insira o segundo número:  '))

for i in range(n1,n2,1):
    print(i)

print("Soma dos números: ", i + i)


print('----------------GERADOR DE TABUADA----------------')
num = int(input('Insira um número de 1 a 10: '))

print(f'Tabuada do {num}:\n')

mult = 1


while mult <= 10:
    print(f'{num} x {mult} = {num*mult}')
    mult = mult + 1
else:
    print('fim')



print('Informe 10 numeros: ')
a = int(input('numero 1: '))
b = int(input('numero 2: '))
c = int(input('numero 3: '))
d = int(input('numero 4: '))
e = int(input('numero 5: '))
f = int(input('numero 6: '))
g = int(input('numero 7: '))
h = int(input('numero 8: '))
i = int(input('numero 9: '))
j = int(input('numero 10: '))
ctp = 0
cti = 0
while True:
    if a % 2 == 0:
        print(a, 'é par')
        ctp = ctp + 1
    else:
        print(a, 'é impar')
        cti = cti + 1
    if b % 2 == 0:
        print(b, 'é par')
        ctp = ctp + 1
    else:
        print(b, 'é impar')
        cti = cti + 1
    if c % 2 == 0:
        print(c, 'é par')
        ctp = ctp + 1
    else:
        print(c, 'é impar')
        cti = cti + 1
    if d % 2 == 0:
        print(d, 'é par')
        ctp = ctp + 1
    else:
        print(d, 'é impar')
        cti = cti + 1
    if e % 2 == 0:
        print(e, 'é par')
        ctp = ctp + 1
    else:
        print(e, 'é impar')
        cti = cti + 1
    if f % 2 == 0:
        print(f, 'é par')
        ctp = ctp + 1
    else:
        print(f, 'é impar')
        cti = cti + 1
    if g % 2 == 0:
        print(g, 'é par')
        ctp = ctp + 1
    else:
        print(g, 'é impar')
        cti = cti + 1
    if h % 2 == 0:
        print(h, 'é par')
        ctp = ctp + 1
    else:
        print(h, 'é impar')
        cti = cti + 1
    if i % 2 == 0:
        print(i, 'é par')
        ctp = ctp + 1
    else:
        print(i, 'é impar')
        cti = cti + 1
    if j % 2 == 0:
        print(j, 'é par')
        ctp = ctp + 1
    else:
        print(j, 'é impar')
        cti = cti + 1
    print('Total de numeros pares: ', ctp)
    print('Total de numeros impares: ', cti)
    break


n = int(input("Qual termo da série de Fibonacci deseja encontrar: "))
ultimo=1
penultimo=1


if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)


num = int(input('Insira o número para fatorar: '))

fat = 1
i = 2

while i <= num:
    fat = fat*i
    i = i + 1

    print(f'O valor de {num}! = {fat}')




soma = 0
lista = []

ask = str(input('Deseja continuar?\n'))

while ask == 'sim':
    num=int(input('Digite o numero: '))
    ask = str(input('Deseja continuar?\n'))
    if num < 1000 or num > 0:
        soma += num
        lista.append(num)
    else:
        break

print(f'Soma: {soma}')
print('Menor Valor: ', min(lista))
print('Maior Valor: ', max(lista))



ask = str(input('Deseja começar?\n'))
num = int(input('Insira um número: '))

while ask == 'sim':
    es = num % 2
    if res==1 and num%3==2:
        print(f'{num} é primo')
        ask = str(input('Deseja continuar?\n'))
    else:
        print(f'{num} não é primo')
        ask = str(input('Deseja continuar?\n'))
else:
    print('Fim')



num = int(input('Insira um número: '))

i = 3
x = 1

print('1 é primo\n')
print('2 é primo\n')

while i <= num:
    if i % 2 == 1 and i % 3 == 2:
        print(f'{i} é primo\nNúmeros de divisões feitas {x}\n')
        i = i + 1
        x = x + 1
    else:
        print(f'{i} não é primo\n')
        i = i + 1



cand1 = str(input('Insira o nome do primeiro candidato: '))
print(cand1)
num1 = int(input(f'Insira o número do candidato {cand1}: '))
cnt1 = 0
cand2 = str(input('Insira o nome do segundo candidato candidato: '))
print(cand2)
num2 = int(input(f'Insira o número do candidato {cand2}: '))
cnt2 = 0
cand3 = str(input('Insira o nome do terceiro candidato: '))
print(cand3)
num3 = int(input(f'Insira o número do candidato {cand3}: '))
cnt3 = 0

numelect = int(input('Quantos eleitores terão?\n'))

cont = 0

voto = 0

while cont < numelect:
    voto = int(input(f'Olá eleitor Número {cont + 1}\nInsira o número do candidato que deseja votar:\n'
                 f'{num1} - {cand1}\n{num2} - {cand2}\n{num3} - {cand3}\n'))
    while voto != num1 and voto != num2 and voto != num3:
        voto = int(input(f'Número inserido não existente. Por favor digite novamente:\n'
                     f'{num1} - {cand1}\n{num2} - {cand2}\n{num3} - {cand3}\n'))
    else:
       if voto == num1:
           cnt1 = cnt1 + 1
           print(f'Voto para {cand1} computado com sucesso!')
           cont = cont + 1
       elif voto == num2:
           cnt2 = cnt2 + 1
           print(f'Voto para {cand2} computado com sucesso!')
           cont = cont + 1
       elif voto == num3:
           cnt3 = cnt3 + 1
           print(f'Voto para {cand3} computado com sucesso!')
           cont = cont + 1
else:
    print('Votação Encerrada com Sucesso!')
    print(f'{cand1}({num1}) = {cnt1}\n{cand2}({num2}) = {cnt2}\n{cand3}({num3}) = {cnt3}\n ')
    if cnt1 > cnt2 and cnt1 > cnt3:
        p = 100*cnt1/numelect
        print(f'{cand1} ELEITO COM {cnt1} VOTOS\nPorcentagem: {p}%')
    elif cnt2 > cnt1 and cnt2 > cnt3:
        p = 100 * cnt2 / numelect
        print(f'{cand2} ELEITO COM {cnt2} VOTOS\nPorcentagem: {p}%')
    elif cnt3 > cnt2 and cnt3 > cnt1:
        p = 100 * cnt1 / numelect
        print(f'{cand3} ELEITO COM {cnt3} VOTOS\nPorcentagem: {p}%')


#coleção de cds

cds = {}

qtd = int(input('Insira a quantidade de CDs possuídos: '))

check = str(input(f'{qtd} é a quantidade certas de CDs?\n'))

while check != 'sim':
    qtd = int(input('Insira a quantidade de CDs possuídos novamente: '))
    check = str(input(f'{qtd} é a quantidade certas de CDs?\n'))
else:
    print(f'Quantidade de CDs armazenada')

cont = 0

while cont < qtd:
    nome = str(input(f'Insira o nome do CD {cont + 1}: '))
    valor = float(input(f'Quanto custou o CD {nome}?\n'))
    cds[nome] = valor
    print(cds)
    cont = cont + 1
else:
    print(cds)
    total = sum(map(lambda cds:float(cds),cds.values()))
    media = total/qtd
    print(f'Total gasto em CDs: R${total}\nMédia gasta por CD: R${media}')

#Loja 1,99

qtd = int(input('Olá, insira a quantidade de produtos comprados:  '))

final = 1.99

cont = 1

while cont < qtd:
    final = final + 1.99
    cont = cont + 1
else:
    print(f'{qtd} Produtos\nPreço Final: R${final}')



#loja de conveniencia



cont = 1

print('Insira o preço do produto\n')
produto = float(input(f'Produto {cont}: '))
print(f'R${produto}')
final = produto

while produto != 0:
    cont = cont + 1
    produto = float(input(f'Produto {cont}: '))
    print(f'R${produto}')
    final = final + produto
else:
    print(f'Preço da compra: R${final}')
    pay = float(input('Quanto será pago?\n'))
    troco = pay - final
    print(f'O troco deverá ser de R${troco}')


n = int(input("Digite o valor de n: "))
fat = 1
i = 2
k = 1
a = n

while i <= n:
    fat = fat * i
    i = i + 1
else:
    print(f'{n}! = {fat}')
    while k < i - 1:
        r = a*(n - k)
        print(f'{a}x{n - k} = {r}')
        a = r
        k = k + 1
    else:
        print('ok')



#Metereolista

dic = {}
r = str(input('Digite SIM para iniciar\n'))
i = 0

while r == 'sim':
    i = i + 1
    cidade = str(input('Insira a cidade: '))
    temp = float(input('Agora insira a temperatura: '))
    dic[cidade] = temp
    print(dic)
    r = str(input('Digite SIM para adicionar outra cidade\nDigite FIM para finalizar\n'))
else:
    print(f'Temperatura Mínima: {min(dic)}')
    print(f'Temperatura Mínima: {max(dic)}')
    total = sum(filter(lambda elem: elem, (map(lambda dic: float(dic), dic.values()))))
    media = (total)/i
    print(f'Média de Temperatura: {media}C')



n = int(input('Insira o número que deseja fazer a tabuada: '))
c = int(input('Insira o número em que deseja inicar a tabuada: '))
f = int(input('Insira o número em  que deseja terminar a tabuada: '))
i = 0
print(f'Tabuada do {n}\nComeçando por {c}\nTerminando em {f}')

while i < c-1:
    print('loading')
    i = i + 1
else:
    while i < f:
        i = i + 1
        print(f'{n}x{i} = {n*i}')



#Academia

cliente = []

wcode = 1

while (wcode):
  wcode = int(input("Informe o codigo do cliente ou 0 para terminar\n"))
  if wcode:
    waltura = float(input("Informe a altura em metros:  "))    wpeso = float(input("Informe o peso em quilos:  "))
    cliente.append({'Codigo': wcode, 'Altura': waltura, 'Peso': wpeso})
    print(cliente)

mais_alto = -1
mais_baixo = 999
mais_gordo = -1
mais_magro = 999

for x in cliente:
  if x['Altura'] > mais_alto:
    qual_mais_alto = x['Codigo']
    mais_alto = x['Altura']
  if x['Altura'] < mais_baixo:
    qual_mais_baixo = x['Codigo']
    mais_baixo = x['Altura']
  if x['Peso'] > mais_gordo:
    qual_mais_gordo = x['Codigo']
    mais_gordo = x['Peso']
  if x['Peso'] < mais_magro:
    qual_mais_magro = x['Codigo']
    mais_magro = x['Peso']

print(cliente)
print(f'O cliente mais alto é {qual_mais_alto} e  mede {mais_alto}')
print(f'O cliente mais baixo é {qual_mais_baixo} e  mede {mais_baixo}')
print(f'O cliente mais pesado é {qual_mais_gordo} e  pesa {mais_gordo}')
print(f'O cliente menos pesado é {qual_mais_magro} e  pesa {mais_magro}')



ano = int(input('Insira o ano de início promoção: '))
salario = float(input('Insira o salário incial: '))
porcentagem = float(input('Insira a porcentagem do aumento anual: '))
aumento = 0.01*porcentagem

fim = int(input('Insira o ano que deseja prever o salário: '))

while ano < fim:
    ano = ano + 1
    salario = salario*aumento + salario
    aumento = aumento*2
    porcentagem = porcentagem*2
    print(f'Ano: {ano}\nSalário: {salario}\nAumento: {porcentagem}%\n\n')



cidades = []

wcode = 1

ct = 0

soma_carros = soma_acidente = soma_2k = qual_menos_carros = 0

while (wcode):
  wcode = int(input("Informe o codigo da cidade ou 0 para terminar\n"))
  if wcode:
    wcarros = float(input("Informe a quantidade de carros na cidade:  "))
    wacidente = float(input("Informe o número de acidentes no último ano:  "))
    cidades.append({'Codigo': wcode, 'Carros': wcarros, 'Acidente': wacidente})
    print(cidades)
    ct = ct + 1

soma_carros += wcarros
soma_acidente += wacidente

mais_carros = -1
menos_carros = 999
mais_acidente = -1
menos_acidente = 999


for x in cidades:
  if x['Carros'] > mais_carros:
    qual_mais_carros = x['Codigo']
    mais_carros = x['Carros']
  if x['Carros'] < menos_carros:
    qual_menos_carros = x['Codigo']
    menos_carros = x['Carros']
  if x['Acidente'] > mais_acidente:
    qual_mais_acidente = x['Codigo']
    mais_acidente = x['Acidente']
  if x['Acidente'] < menos_acidente:
    qual_menos_acidente = x['Codigo']
    menos_acidente = x['Acidente']

print(cidades)
print(f'A cidade com mais carros é {qual_mais_carros} e  tem {mais_carros} carros')
print(f'A cidade com menos carro é {qual_menos_carros} e tem {menos_carros} carros')
print(f'A cidade com mais acidentes é {qual_mais_acidente} e teve {mais_acidente} acidentes no último ano')
print(f'A cidade com menos acidentes é {qual_menos_acidente} e teve {menos_acidente} acidentes no último ano')

media = soma_carros/ct

print(f'A média de carros nas cidades é de: {media} carros ')

ct2 = 0

if wcarros > 2000:
  soma_2k += wacidente
  ct2 = ct2 + 1
  media_2k = soma_2k/ct2

print(f'A média de acidentes nas cidades com mais de 2 mil carros é de {media_2k} acidentes')


"""

""""

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00



carrinho = []
preço = 0

print('---------------Bem Vindx a Lanchonete Maneira---------------')
print('Especificação   Código  Preço\nCachorro Quente 100     R$ 1,20\n'
      'Bauru Simples   101     R$ 1,30'
      '\nBauru com ovo   102     R$ 1,50\nHambúrguer      103     R$ 1,20\n'
      'Cheeseburguer   104     R$ 1,30\nRefrigerante    105     R$ 1,00')

inicio = input('Pressione Y para fazer o pedido\n')

while inicio == 'y':
  pedido = int(input('Insira o código do lanche desejado: '))
  if pedido == 100:
    wqtd = int(input('Quantas unidades deseja?\n'))
    preço = preço + 1.20*wqtd
    wpedido = 'Cachorro Quente'
    carrinho.append({'Pedido': wpedido, 'Quantidade': wqtd})
    inicio = input('Pressione Y para fazer outro pedido\n')
  if pedido == 101:
    wqtd = int(input('Quantas unidades deseja?\n'))
    preço = preço + 1.30 * wqtd
    wpedido = 'Bauru Simples'
    carrinho.append({'Pedido': wpedido, 'Quantidade': wqtd})
    inicio = input('Pressione Y para fazer outro pedido\n')
  if pedido == 102:
    wqtd = int(input('Quantas unidades deseja?\n'))
    preço = preço + 1.50 * wqtd
    wpedido = 'Bauru com Ovo'
    carrinho.append({'Pedido': wpedido, 'Quantidade': wqtd})
    inicio = input('Pressione Y para fazer outro pedido\n')
  if pedido == 103:
    wqtd = int(input('Quantas unidades deseja?\n'))
    preço = preço + 1.20 * wqtd
    wpedido = 'Hamburguer'
    carrinho.append({'Pedido': wpedido, 'Quantidade': wqtd})
    inicio = input('Pressione Y para fazer outro pedido\n')
  if pedido == 104:
    wqtd = int(input('Quantas unidades deseja?\n'))
    preço = preço + 1.30 * wqtd
    wpedido = 'Cheeseburguer'
    carrinho.append({'Pedido': wpedido, 'Quantidade': wqtd})
    inicio = input('Pressione Y para fazer outro pedido\n')
  if pedido == 105:
    wtd = int(input('Quantas unidades deseja?\n'))
    preço = preço + 1 * wqtd
    wpedido = 'Refrigerante'
    carrinho.append({'Pedido': wpedido, 'Quantidade': wqtd})
    inicio = input('Pressione Y para fazer outro pedido\n')

conf = input(f'Este é seu pedido?\n{carrinho}')

if conf == 'sim':
  print(f'O seu pedido deu R${preço}')
  pagar = int(input('Insira o valor da nota com que irá pagar\n'))
  troco = pagar - preço
  print(f'Seu troco será de {troco}')


"""

#Gabarito prova
gabarito = []

total_alunos = soma_notas = ct = 0


#Professor coloca o gabarito

r1 = input('Insira a letra correta da questão 1: ')
r2 = input('Insira a letra correta da questão 2: ')
r3 = input('Insira a letra correta da questão 3: ')
r4 = input('Insira a letra correta da questão 4: ')
r5 = input('Insira a letra correta da questão 5: ')
r6 = input('Insira a letra correta da questão 6: ')
r7 = input('Insira a letra correta da questão 7: ')
r8 = input('Insira a letra correta da questão 8: ')
r9 = input('Insira a letra correta da questão 9: ')
r10 = input('Insira a letra correta da questão 10: ')



#Mecanica para inicio do looping
inicio = input('aperte S para iniciar a correção\n')

#Pergunta as respostas dada pelos alunos contando os acertos
while inicio != 'f':
  total_alunos = total_alunos + 1
  ct = 0
  wnome = str(input('Nome do Aluno: '))
  q1 = input('Insira resposta da questão 1: ')
  if q1 == r1:
    ct = ct + 1
  q2 = input('Insira resposta da questão 2: ')
  if q2 == r2:
    ct = ct + 1
  q3 = input('Insira resposta da questão 3: ')
  if q3 == r3:
    ct = ct + 1
  q4 = input('Insira resposta da questão 4: ')
  if q4 == r4:
    ct = ct + 1
  q5 = input('Insira resposta da questão 5: ')
  if q5 == r5:
    ct = ct + 1
  q6 = input('Insira resposta da questão 6: ')
  if q6 == r6:
    ct = ct + 1
  q7 = input('Insira resposta da questão 7: ')
  if q7 == r7:
    ct = ct + 1
  q8 = input('Insira resposta da questão 8: ')
  if q8 == r8:
    ct = ct + 1
  q9 = input('Insira resposta da questão 9: ')
  if q9 == r9:
    ct = ct + 1
  q10 = input('Insira resposta da questão 10: ')
  if q10 == r10:
    ct = ct + 1
  gabarito.append({'Nome': wnome, 'Nota': ct})
  print(gabarito)
  inicio = str(input('Pressione S para corrigir a prova de outro aluno e F para finalizar o programa\n'))

print(total_alunos)
soma_notas += ct
print(soma_notas)
media = soma_notas/total_alunos


print(f'A média da turma foi {media}\n')


maior_nota = -1
menor_nota = 999

for x in gabarito:
  if x['Nota'] > maior_nota:
    qual_maior_nota = x['Nome']
    maior_nota = x['Nota']
  if x['Nota'] < menor_nota:
    qual_menor_nota = x['Nome']
    menor_nota = x['Nota']

print(f'Maior Nota = {maior_nota} : {qual_maior_nota}\n')
print(f'Menor Nota = {menor_nota} : {qual_menor_nota}\n')














