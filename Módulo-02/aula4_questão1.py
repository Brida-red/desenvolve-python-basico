largura = int(input("Qual a largura do terreno em metros?"))
comprimento = int(input("Qual o cumprimento do terreno em metros?"))
preço_m2 = float(input("Qual o preço do metro quadrado do terreno?"))
# A área em metros quadrados é obtida através da multiplicação da largura pelo comprimento do terreno
área_m2 = largura * comprimento
# O preço total é obtido através da multiplicação da área em metros quadrados pelo preço do metro quadrado
preço_total = área_m2 * preço_m2
print (f"O terreno possui {área_m2}m2 e custa R$ {preço_total:,.2f}")