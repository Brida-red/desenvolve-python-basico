n_respondentes = int(input("Digite a quantidade de respondentes: "))

soma = 0
cont = 0

while cont < n_respondentes:
    idade = int(input("Digite as idades dos respondentes: "))
    soma = soma + idade
    cont = cont + 1

print (f"A média das idades dos respondentes é {soma/n_respondentes} anos.")