#Sabendo que o código a seguir calcula o fatorial de n, escreva uma função chamada ```fatorial()``` que recebe um 
#  inteiro```n``` como parâmetro e retorna o resultado do fatorial de ```n```. 
# No programa principal, peça ao usuário o valor de ```n```, chame a sua função e imprima o retorno.
# fat = 1
# for i in range(1, n+1):
# fat *= i 

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat*=i
    return fat

num = int(input("Digite um valor:"))
meufatorial = fatorial(num)
print(f"O fatorial de {num} é {meufatorial}")