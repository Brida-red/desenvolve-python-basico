classe = input ("Escolha a classe (mago, guerreiro ou arqueiro)") 
pontos_força = int(input ("Digite os pontos de força"))
pontos_magia = int(input ("Digite os pontos de magia"))
mago = pontos_força <= 10 and pontos_magia >= 15
guerreiro = pontos_força >= 15 and pontos_magia <= 10
arqueiro = (pontos_força > 5) and (pontos_magia > 5) and (pontos_força <= 15) and (pontos_magia <= 15)
pontos_atribuidos = mago or guerreiro or arqueiro 
print = input(f"Pontos de atributo consistentes com a classe escolhida:{pontos_atribuidos}")