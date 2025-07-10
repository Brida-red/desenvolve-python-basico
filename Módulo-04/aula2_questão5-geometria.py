#Você está desenvolvendo um programa para auxiliar em cálculos de geometria básica. Crie as seguintes funções:
# A função ```calcula_perimetro_triangulo()``` que recebe três inteiros correspondentes aos lados de um triângulo e 
# retorna o perímetro do triângulo, ou seja, a soma dos seus lados.
# A função ```calcula_perimetro_circulo()``` que recebe um inteiro referente ao raio do círculo e retorna o perímetro 
# do círculo, dado por $2 \pi r$. Use a constante $\pi$ da biblioteca ```math```.
# A função ```calcula_perimetro_retangulo()``` que possui um parâmetro obrigatório ```lado1``` e um opcional 
# ``lado2```, ambos inteiros. Se o valor opcional não for fornecido, significa que se trata de um quadrado. 
# Sua função deve calcular e retornar o perímetro do retângulo, ou seja, a soma de seus lados. 
# Para o quadrado, é dado por $4 \times lado1$
# Para o retângulo é dado por $2 \times lado1 + 2 \times lado2$
# No programa principal apresente um menu com as opções disponíveis do seu sistema e uma quarta opção ```Sair```. 
# Solicite ao usuário a opção desejada, solicite as entradas correspondentes à opção escolhida, invoque a respective 
# função e apresente o seu retorno. Seu programa deve retornar ao menu até que o usuário escolha a opção ```Sair```

import math

def calcula_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def calcula_perimetro_circulo(raio):
    return 2 * math.pi * raio

def calcula_perimetro_retangulo(lado1, lado2=0):
    if lado2 == 0:
        return 4 * lado1  
    else:
        return 2 * lado1 + 2 * lado2 

while True:
        print("\n1 - Calcular perímetro triângulo")
        print("2 - Calcular perímetro círculo")
        print("3 - Calcular perímetro retângulo")
        print("4 - Sair\n")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            print("Digite os três lados do triângulo:")
            l1 = int(input())
            l2 = int(input())
            l3 = int(input())
            perimetro = calcula_perimetro_triangulo(l1, l2, l3)
            print(f"O perímetro é: {perimetro}")
        
        elif opcao == "2":
            raio = int(input("Digite o raio do círculo: "))
            perimetro = calcula_perimetro_circulo(raio)
            print(f"O perímetro é: {perimetro:.2f}")
        
        elif opcao == "3":
            print("Informe os dois lados do retângulo. Se for um quadrado, digite 0 para o segundo valor:")
            lado1 = int(input())
            lado2 = int(input())
            perimetro = calcula_perimetro_retangulo(lado1, lado2)
            print(f"O perímetro é: {perimetro}")
        
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")