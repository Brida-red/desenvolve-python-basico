ano = int (input ("Digite o ano para saber se é bissexto"))

if (ano % 4 == 0 and ano % 100 != 100) or ano % 400 ==0:
    print ("O ano é Bissexto!")
else:
    print ("O ano não é Bissexto!")