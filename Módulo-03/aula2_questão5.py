gênero = input("Qual o seu gênero (m/f)?")
idade = int(input("Qual a sua idade?"))
tempo_serviço = int(input("Qual o seu tempo de serviço?"))

a = (gênero == 'f' and idade >=60) or (gênero == 'm' and idade >= 65)
b = tempo_serviço >= 30
c = idade >= 60 and tempo_serviço >= 25

pode_aposentar = a or b or c
print (f"Já pode se aposentar? {pode_aposentar}")