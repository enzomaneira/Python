print('Verificador de triângulo\n')

l1 = float(input('Informe o tamanho do primeiro lado: '))
l2 = float(input('Informe o tamanho do segundo lado: '))
l3 = float(input('Informe o tamanho do terceiro lado: '))


if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print('Não é um triângulo')
elif l1 == l2 and l1 == l3:
    print('Triângulo Equilátero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Triângulo Escaleno')
else:
    print('Triângulo Isóceles')


