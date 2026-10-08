from random import randint
from time import time
numeros = list()


numero_busca = randint(1,5000)

inicio = time()
for i in range(50_000):
    numeros.append(randint(1,5000))

print(f'Numero sorteado para a busca: {numero_busca}')
posicoes = list()

for p, n in enumerate(numeros):
    if n == numero_busca:
        posicoes.append(p)
fim = time()

print('Posicoes onde o numero esta presente')        
for p in posicoes:
    print(p)
print(f'Tempo de processamento = {fim - inicio} segundos')
    
    
    
