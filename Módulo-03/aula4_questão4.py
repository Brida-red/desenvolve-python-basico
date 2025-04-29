distância = float(input("Qual a distância em Km a ser percorrida?"))
peso_pacote = float (input("Qual o peso em Kg do pacote?"))

if distância <=100:
    tarifa = 1.0

elif distância <= 300:
    tarifa = 1.5

else:
    tarifa = 2.0

valor_frete = peso_pacote * tarifa

if peso_pacote > 10.0:
    valor_frete = valor_frete + 10

print (f"O valor do frente é de R${valor_frete: ,.2f}")