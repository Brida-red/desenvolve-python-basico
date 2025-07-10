#- Escreva uma função em Python chamada ```soma_quadrados``` que recebe dois números como parâmetros e retorna a 
# soma dos seus quadrados. 
# No programa principal solicite ao usuário que insira dois números e utilize a função para exibir a soma dos 
# quadrados.

def soma_quadrados (x, y):
    return x**2 + y**2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = soma_quadrados (num1, num2)
print (f"O resultado da soma dos quadrados de {num1} e {num2} é: {resultado}")