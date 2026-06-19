print('Programa que acha os divisores de um numero n')
n = int(input('Informe o valor de n:'))

print('Divisores')
# vai iniciar a busca no proprio numero e vai decaindo
# os valores de i ate chegar no numero 1 ...
# exemplo se o numero for 20 ... vai dividir 20/20 , depois
# 20/19 , depois 20/18 ... ate chegar no 20/1 . toda vez que
# essa o resto da divisão for 0(zero) é pq o numero i é um divisor
# de n ...
for i in range(n,0,-1): 
    if n % i == 0 :
        print(i)