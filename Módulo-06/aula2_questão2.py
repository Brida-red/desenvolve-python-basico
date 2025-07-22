# Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. 
# Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em 
# uma lista chamada elementos. Em seguida imprima:
# A lista elementos
# A soma dos valores da lista
# A média dos valores da lista

import random

num_elementos = random.randint (5, 20)
print(num_elementos)

elementos = [random.randint (1,10) for i in range(num_elementos)]
print(elementos)

print(f"A soma dos números da lista é igual a: {sum(elementos)}")
print(f"A média dos números da lista é: {sum(elementos)/len(elementos)}")
