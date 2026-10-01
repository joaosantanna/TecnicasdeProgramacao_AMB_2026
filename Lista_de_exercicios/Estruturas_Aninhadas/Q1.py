
temperaturas = [[22, 25, 19, 21],
                [30, 32, 31, 29],
                [15, 18, 14, 17]]

medias =[]
for cidade in temperaturas:
    media = sum(cidade)/4
    medias.append(media)
print(f' Medias ')
for p, t in enumerate(medias):
    print(f'{p+1} - {t:.2f}')
    
maior= max(medias)
cidade = medias.index(maior)
print(f' A cidade que teve maior media é a cidade {cidade + 1}')
print(f' Media da cidade {cidade +1} = {maior}')

print('-------'*5)
for p, t in enumerate(temperaturas):
    print(f'{p+1} - {t}')