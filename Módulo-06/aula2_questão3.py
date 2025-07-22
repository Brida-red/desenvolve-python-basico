# Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista 
# interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
# Ambas as listas
# A lista intersecção ordenada
# A quantidade de vezes que cada elemento aparece em cada lista

import random

lista1, lista2 = [], []
for i in range(20):
    lista1.append(random.randint (0, 50))
    lista2.append(random.randint (0, 50))
print(sorted(lista1))
print(sorted(lista2))

intersecção = []
for elemento in lista1:
    if elemento in lista2 and elemento not in intersecção:
        intersecção.append(elemento)

intersecção.sort()
for i in intersecção:
    print(f"{i}: ({lista1.count(i)}, {lista2.count(i)})")