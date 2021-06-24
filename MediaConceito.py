nome = input('Nome do aluno: ')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2)/2

if media < 4:
    conceito = 'F'
    print(f'Aluno: {nome}\nN1: {n1}\nN2: {n2}\nMédia: {media}\nConceito: {conceito}\nREPROVADO')
elif media >= 2 and media < 4:
    conceito = 'E'
    print(f'Aluno: {nome}\nN1: {n1}\nN2: {n2}\nMédia: {media}\nConceito: {conceito}\nREPROVADO')
elif media >= 4 and media < 6:
    conceito = 'D'
    print(f'Aluno: {nome}\nN1: {n1}\nN2: {n2}\nMédia: {media}\nConceito: {conceito}\nREPROVADO')
elif media >= 6 and media < 7.5:
    conceito = 'C'
    print(f'Aluno: {nome}\nN1: {n1}\nN2: {n2}\nMédia: {media}\nConceito: {conceito}\nAPROVADO')
elif media >= 7.5 and media < 9:
    conceito = 'B'
    print(f'Aluno: {nome}\nN1: {n1}\nN2: {n2}\nMédia: {media}\nConceito: {conceito}\nAPROVADO')
elif media >= 9 and media <=10:
    conceito = 'A'
    print(f'Aluno: {nome}\nN1: {n1}\nN2: {n2}\nMédia: {media}\nConceito: {conceito}\nAPROVADO')
else:
    print('Erro!')