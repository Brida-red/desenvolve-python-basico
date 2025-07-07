#Seu programa deve apresentar para o usuário a lista de emojis disponíveis com o texto correspondente a cada emoji. 
# Em seguida, solicite uma frase codificada ao usuário e apresente ela decodificada com a visualização de emojis 
# (emojizada). Conheça a função emoji.emojize()

import emoji

coração = emoji.emojize(':red_heart:')
positivo = emoji.emojize(':thumbs_up:')
pensativo = emoji.emojize(':thinking_face:')
festivo = emoji.emojize(':partying_face:')
computador = emoji.emojize(':laptop:')
livro = emoji.emojize(':open_book:')

print("Emojis Disponíveis:")
print (f"{coração}  - :red_heart:")
print(f"{positivo} - :thumbs_up:")
print(f"{pensativo} - :thinking_face:")
print(f"{festivo} - :partying_face:")
print(f"{livro} - :open_book:")
print (f"{computador} - :laptop:")

frase = emoji.emojize(input("Digite uma frase e ela será emojizada: "))
frase_emojizada = frase
print (frase)
