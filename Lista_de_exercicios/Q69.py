frase = input('Digite a frase a ser processada:')
lista_palavras = frase.split(' ')
lista_palavra_unicas = set(lista_palavras)

resultado =dict()

for palavra in lista_palavra_unicas:
    resultado[palavra] = lista_palavras.count(palavra)

print('Lista de palavras e sua frequencia')
for frequencia, palavra in resultado.items():
    print(f'{frequencia} - {palavra}')
