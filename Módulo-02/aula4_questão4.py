valor = float(input("Digite um valor:"))

notas_100 = valor//100

valor = valor % 100

notas_50 = valor // 50

valor = valor % 50

notas_20 = valor // 20

valor = valor % 20

notas_10 = valor // 10

valor = valor % 10

notas_5 = valor // 5

valor = valor % 5

notas_2 = valor // 2

valor = valor % 2

notas_1 = valor // 1

print (f"{notas_100} Notas de R$ 100,00")
print (f"{notas_50} Notas de R$ 50,00")
print (f"{notas_20} Notas de R$ 20,00")
print (f"{notas_10} Notas de R$ 10,00")
print (f"{notas_5} Notas de R$ 5,00")
print (f"{notas_2} Notas de R$ 2,00")
print (f"{notas_1} Notas de R$ 1,00")