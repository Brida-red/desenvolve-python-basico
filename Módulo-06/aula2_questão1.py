# Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. 
# Em seguida imprima na ordem estabelecida:
# A lista ordenada, sem modificar a lista original
# A lista original
# O índice do maior valor da lista
# O índice do menor valor da lista

import random

lista = []
for i in range(20):
    valores = random.randint (-100,100)
    lista.append(valores)

print(sorted(lista))
print(lista)
print("O maior valor da lista está no índice: ", lista.index(max(lista)))
print("O menor valor da lista está no índice: ", lista.index(min(lista)))
