n = int(input("Digite a quantidade de experimentos realizados: "))
cont = 0
soma_coelho = 0
soma_sapo = 0
soma_rato = 0

while cont < n:
    quantia = int(input("Digite a quantidade de cobaias utilizadas: "))
    tipo = input("Digite o tipo de cobaia utlizada (R, S ou C)")

    if tipo == "R":
        soma_rato = soma_rato + quantia

    elif tipo == "S":
        soma_sapo = soma_sapo + quantia
    
    elif tipo == "C":
        soma_coelho = soma_coelho + quantia

    cont = cont+1

print ("Total de Cobais: ", soma_coelho+soma_rato+soma_sapo )
print ("Total de coelhos: ", soma_coelho)
print ("Total de ratos: ", soma_rato)
print ("Total de sapos: ", soma_sapo)
print (f"A porcentagem de coelhos usados é de: {(soma_coelho * 100) / (soma_coelho+soma_rato+soma_sapo)}%")
print (f"A porcentagem de ratos usados é de: {(soma_rato * 100) / (soma_coelho+soma_rato+soma_sapo)}%")
print (f"A porcentagem de sapos usados é de: {(soma_sapo * 100) / (soma_coelho+soma_rato+soma_sapo)}%")