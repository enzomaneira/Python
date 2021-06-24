print('Solucinador de Determinantes\n')

def GeraMatriz():
       print('Gerando vetor 1\n')
       x = int(input('Insira o número que representa a posição X: '))
       y = int(input('Insira o número que representa a posição Y: '))
       z = int(input('Insira o número que representa a posição Z: '))
       vetor1 = []
       vetor1.append(x)
       vetor1.append(y)
       vetor1.append(z)
       vetorF = f'({vetor1[0]}, {vetor1[1]}, {vetor1[2]})'
       print(vetorF)
       print('Gerando vetor 2\n')
       x = int(input('Insira o número que representa a posição X: '))
       y = int(input('Insira o número que representa a posição Y: '))
       z = int(input('Insira o número que representa a posição Z: '))
       vetor2 = []
       vetor2.append(x)
       vetor2.append(y)
       vetor2.append(z)
       vetorF = f'({vetor2[0]}, {vetor2[1]}, {vetor2[2]})'
       print(vetorF)
       print('Gerando vetor 3\n')
       x = int(input('Insira o número que representa a posição X: '))
       y = int(input('Insira o número que representa a posição Y: '))
       z = int(input('Insira o número que representa a posição Z: '))
       vetor3 = []
       vetor3.append(x)
       vetor3.append(y)
       vetor3.append(z)
       vetorF = f'({vetor3[0]}, {vetor3[1]}, {vetor3[2]})'
       print(vetorF)
       matriz = f'{vetor1[0]}, {vetor1[1]}, {vetor1[2]}\n' \
                f'{vetor2[0]}, {vetor2[1]}, {vetor2[2]}\n' \
                f'{vetor3[0]}, {vetor3[1]}, {vetor3[2]}\n'
       print(matriz)
       esquerda = (vetor1[2] * vetor2[1] * vetor3[0]) + (vetor1[0] * vetor2[2] * vetor3[1]) + (vetor1[1] * vetor2[0] * vetor3[2])
       direita = (vetor1[0] * vetor2[1] * vetor3[2]) + (vetor1[1] * vetor2[2] * vetor3[0]) + (vetor1[2] * vetor2[1] * vetor3[0])
       determinante = direita - esquerda
       return determinante

print(GeraMatriz())
















