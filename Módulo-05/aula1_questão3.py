#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 
# e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. 
# Interrompa a execução somente quando o usuário acertar o palpite.

import random
num_aleat = random.randint (1,10)

while True:
    palpite = int(input("Digite um número de 1 a 10: "))

    if palpite == num_aleat:
        print("Você acertou! Parabéns!")
        break

    if palpite < num_aleat / 2:
        print("O seu palpite é muito baixo.")
    else:
        print("O seu palpite é muito alto.")

    
    

