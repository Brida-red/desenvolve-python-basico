#- Crie a função ```inverteValor()``` que recebe um inteiro de qualquer tamanho e retorna esse valor invertido usando 
# apenas operações aritméticas
# Crie a função ```verificaInverso()``` que recebe o valor original e o valor invertido e retorna verdadeiro se ambos
# forem igualmente par ou igualmente ímpar. Retorne falso caso contrário.
# No programa principal, peça um valor do usuário e imprima o retorno de ambas as funções.

def inverteValor(numero):
    numero_original = abs(numero)
    invertido = 0
    while numero_original > 0:
        digito = numero_original % 10        
        invertido = invertido * 10 + digito   
        numero_original = numero_original // 10  

    return invertido

def verificaInverso(original, invertido):
    return (original % 2) == (invertido % 2)

numero = int(input("Digite um número inteiro: "))
invertido = inverteValor(numero)
    
é_inverso_mesmo = verificaInverso(numero, invertido)

print(f"Valor invertido: {invertido}")
print(f"O valor é mesmo inverso do número fornecido? {é_inverso_mesmo}")