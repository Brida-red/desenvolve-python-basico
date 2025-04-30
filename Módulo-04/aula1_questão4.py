n = int(input("Digite um número:"))
maior = 0

while n > 0:
    x = int(input("digite um número:"))
    if x > maior:
        maior = x
    n = n-1

print ({maior})