# questao 19 divisores de um numero

# entrada
print('Programa para contar os divisores de um numero')
n = int(input('Informe o valor de n:'))

# processamento
contador = 0
for i in range(1 , n + 1 ):
    if n % i == 0:
        print(f'divisor {i}')
        contador = contador + 1
#saida
print(f'o numero {n} tem {contador} divisores')