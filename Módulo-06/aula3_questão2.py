# Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o conceito
# de fatiamento de listas para criar uma lista dominios com o nome principal de todos os domínios, conforme exemplo
# a seguir.

URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = [url[4:-4] for url in URLs]
print(dominios)