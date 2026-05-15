# entrada - nao tem ... tudo definido na questao

soma = 0

for i in range(100,201): # vai de 100 a 200
    if i % 7 == 0:
        soma = soma + i
        print(f' {i} é multiplo de 7')

print(f'Soma dos multiplos de 7 entre 100 e 200 = {soma}')