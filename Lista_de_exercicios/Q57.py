frase = input('digite sua frase:')
letras = list(frase)
# tirando espaco em branco virgulas e acentos
indesejadas =list(' ,?!')

for l in indesejadas:
    freq = letras.count(l)
    for i in range(freq):
        letras.remove(l)
        
letras_unicas = set(letras)
resultado = dict()

for l in letras_unicas:
    resultado[l] = letras.count(l)

print('Contador de letras:')
for c, v in resultado.items():
    print(f'{c} -{v}')