# Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros 
# (com pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5, … )

elem_lista = int(input("Digite a quantidade de elementos da lista (mínimo de 4): "))
lista = []
for i in range(elem_lista):
    valores_lista = int(input("Digite os valores que irão compor sua lista: "))
    lista.append(valores_lista)
# lista original 
print(lista)

# 3 primeiros elementos
lista[0:3]
print(lista[0:3])

# 2 últimos elementos
lista[-3:-1]
print(lista[-3:-1])

# lista invertida
lista[::-1]
print(lista[::-1])

# elementos de índice par
lista[0:-1:2]
print(lista[:-1:2])

# elementos de índice ímpar
lista[1:-1:2]
print(lista[1:-1:2])