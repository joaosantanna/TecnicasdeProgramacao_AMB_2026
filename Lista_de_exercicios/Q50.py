from random import randint

numeros=list()
for i in range(50):
    n = randint(100,1000)/10
    numeros.append(n)

media = sum(numeros)/len(numeros)
print(f'Media = {media:.2f}')
print('Numeros abaixo da media')
for numero in numeros:
    if numero < media:
        print(numero ,end=',')

print('\nNumeros acima da media')
for numero in numeros:
    if numero > media:
        print(numero ,end=',')
