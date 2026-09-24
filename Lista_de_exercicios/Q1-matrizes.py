leituras = [[22, 25, 19, 21], [30, 32, 31, 29], [15, 18, 14, 17]]
medias =list()

for lista_temperaturas in leituras:
    medias.append(sum(lista_temperaturas)/len(lista_temperaturas))

print('Medias de temperaturas em cada cidade')
print(medias)
maior = max(medias)
cidade = medias.index(maior)
print(f' A cidade com maior temperatura é a cidade {cidade} com {medias[cidade]} Ceucius')