#Vetores
#Exercício fáicl: Crie um vetor com os numeros de 1 a  10 e imprima
vetor= list(range(1,11))
print(vetor)

#Exercício fácil: Crie um vetor com números pares de 2 a 20 e imprima
vetor= list(range(2,21,2))
print(vetor)

#Exercício médio: Calcule a soma dos elementos de um vetor com números de 1 a 100
vetor=list(range(1,101))
soma= sum(vetor)
print(soma)

#Exercíco médio: Encontre o maior e o menor valor em um vetor de números aleatórios entre 1 e 1000, de tamanho 50

import numpy as np
vetor = np.random.randint(1, 1001, size=50)
maior_valor = np.max(vetor)
menor_valor = np.min(vetor)
print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')

#Opção 2
import random
vetor= random.sample(range(1000),50)
maior_valor = np.max(vetor)
menor_valor = np.min(vetor)
print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')

#Opção 3
import random
vetor=[random.randint(1,1000),for_in range(50)]
maior=max(vetor)
menor=min(vetor)
print(f'Maior: {maior}, Menor{menor}')

#Exercício Díficil, crie um vetor com os 10 primeiros números primos

def eh_primo(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
    return True
  
primos = []
num = 2
while len(primos) < 10:
  if eh_primo(num):
    primos.append(num)
  num += 1
print(primos)

#Exercicio Dificil: Inverta a ordem dos elementos de um vetor de tamanho 20, preenchido com numeros aleatorios
import random
vetor = [random.randint(1,100) for _ in range(20)]
vetor_invertido = vetor[::-1]
print(vetor)
print(vetor_invertido)

#Matrizes em Python
#Exercício Fácil: crie uma matriz 3x3 com os números de 1 a 9

import numpy as np
matriz = np.arange(1,10).reshape(3,3)
print(matriz)

#Exercicio Fácil: crie uma matriz identidade 4x4

matriz = np.identity(4)
#np.eye(4) tbm funciona
print(matriz)


#Exercicio Medio: some duas matrizes 2x2
import numpy as np
matriz1 = np.array([[1,2],[3,4]])
matriz2 = np.array([[5,6],[7,8]])
matriz_soma = matriz1 + matriz2
print(matriz_soma)

#Exercicio Medio: multiplique duas matrizes 2x2
import numpy as np
matriz1 = np.array([[1,2],[3,4]])
matriz2 = np.array([[5,6],[7,8]])
matriz_prod = matriz1 * matriz2
#matriz_prod = np.dot(matriz1, matriz2)
print(matriz_prod)

#Exercicio Dificil: calcule a transposta de uma matriz 3x3
import numpy as np
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz_transposta = np.transpose(matriz)
print(matriz_transposta)

#Exercicio Dificil: calcule a determinante de uma matriz 3x3
import numpy as np
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
determinante = np.linalg.det(matriz)
print(determinante)
