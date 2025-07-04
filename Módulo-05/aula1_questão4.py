#Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação
#  apresentada a seguir: Data: 15/03/2023, Hora: 14:05

import datetime

agora = datetime.datetime.now()

print(f"Data: {agora.day:02d}/{agora.month:02d}/{agora.year}")
print(f"Hora: {agora.hour:02d}:{agora.minute:02d}")