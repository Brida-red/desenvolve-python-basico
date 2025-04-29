idade_jogador = int(input("Digite sua idade"))
jogos_tabuleiro = input("Já jogou pelo menos 03 jogos de tabuleiro? (True/False):") == "True"
jogos_vencidos = int(input("Quantos jogos já venceu?"))

apto = (16 <= idade_jogador <= 18) and jogos_tabuleiro and (jogos_vencidos >= 1)
print (f"Apto para ingressar no clube de jogos de tabuleiro: {apto}")