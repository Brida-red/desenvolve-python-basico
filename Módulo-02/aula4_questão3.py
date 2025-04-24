produto1 = (input("Ditite o nome do produto 1:"))
preço1 = float(input("Digite o preço unitário do produto 1:"))
quantidade1 = int (input("Digite a quantidade do produto 1:"))
total_1 = preço1 * quantidade1

produto2 = (input("Ditite o nome do produto 2:"))
preço2 = float(input("Digite o preço unitário do produto 2:"))
quantidade2 = int (input("Digite a quantidade do produto 2:"))
total_2 = preço2 * quantidade2


produto3 = (input("Ditite o nome do produto 3:"))
preço3 = float(input("Digite o preço unitário do produto 3:"))
quantidade3 = int (input("Digite a quantidade do produto 3:"))
total_3 = preço3 * quantidade3

preço_total = total_1 + total_2 + total_3

print (f"Total: R$ {preço_total:,.2f}")
