#Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta
# entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para
#  arredondar o resultado para duas casas decimais.

n1 = float(input("Digite um número decimal: "))
n2 = float (input("Digite outro número decimal: "))

diferença = abs(n1 - n2)
arredond = round (diferença, 2)

print(diferença, arredond)