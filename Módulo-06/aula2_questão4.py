# Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade 
# diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. 
# Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

elem_lista1 = int(input("Digite a quantidade de valores da lista 1: "))
lista1 = []
for i in range (elem_lista1):
    valores_lista1 = int(input("Digite os valores da lista 1: "))
    lista1.append(valores_lista1)
print(lista1)

elem_lista2 = int(input("Digite a quantidade de valores da lista 2: "))
lista2 = []
for i in range (elem_lista2):
    valores_lista2 = int(input("Digite os valores da lista 2: "))
    lista2.append(valores_lista2)
print(lista2)

def intercalar_listas(lista1, lista2):
    intercalada = []
    max_len = max(len(lista1), len(lista2))

    for i in range(max_len):
        if i < len(lista1):
            intercalada.append(lista1[i])
        if i < len(lista2):
            intercalada.append(lista2[i])
    
    return intercalada


lista_intercalada = intercalar_listas(lista1, lista2)

print("Lista intercalada: ", lista_intercalada)