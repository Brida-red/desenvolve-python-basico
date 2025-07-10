# Crie uma função em Python chamada ```soma_digitos``` que recebe um número inteiro como parâmetro e retorna a 
# soma dos seus dígitos. Por exemplo, para o número 123, a função deve retornar 6, (1 + 2 + 3).
# O desafio aqui é separar os dígitos de um número inteiro usando operações aritméticas
# No programa principal solicite ao usuário que insira um número e utilize a função "soma_digitos" para 
# calcular e exibir a soma dos seus dígitos.

def soma_digitos (n):
    n = abs(n)
    soma = 0
    while n > 0:
        digito = n % 10
        soma = soma + digito
        n = n // 10
    return soma

num = int(input("Digite um número inteiro e positivo: "))
resultado = soma_digitos (num)
print (f"A soma dos dígitos do número fornecido é: {resultado}")
