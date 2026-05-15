# calculo do fatorial de um numero

# entradas
n = int(input('Digite um numero para o calculo do fatorial:'))

# processamento
fat = 1
for i in range(n , 0 , -1 ):
    print(f'multiplicando {i}')
    fat = fat * i

print(f'Fatorial de {n} = {fat}')