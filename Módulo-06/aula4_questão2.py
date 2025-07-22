# Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase (remova espaços em branco)

frase = input("Digite uma frase: ")

vogais = 'aeiou'

lista_vogais = sorted([letra for letra in frase if letra in vogais])

lista_consoantes = [letra for letra in frase if letra not in vogais]

print("Lista de vogais:", lista_vogais)
print("lista de consoantes:", lista_consoantes)