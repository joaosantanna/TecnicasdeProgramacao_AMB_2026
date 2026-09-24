print('Contador de letras')
frase = input('Digite uma frase:')

frase = list(frase)
print(f'Todas as letras {frase}')

letras = set(frase)
print(f'Letras unicas{letras}')

contador_letras = {}
for l in letras:
    if l != ' ':
        contador_letras[l] = frase.count(l)
print(f' contagem das letras {contador_letras}')
        