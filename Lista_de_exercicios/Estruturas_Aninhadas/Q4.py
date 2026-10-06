dados_mistos = [[1, 2], [3], [4, 5, 6], [7, 8]]

lista = []

for sublista in dados_mistos:
    for n in sublista:
        lista.append(n)

print(lista)