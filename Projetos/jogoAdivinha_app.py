from random import randint
segredo = randint(1,100)

tentativas = 0
print('Jogo do acerte o numero - adivinhe o numero entre 1 e 100')

while True:
    chute = int(input('Digite um numero entre 1 e 100:'))
    tentativas = tentativas + 1
    if chute == segredo:
        print(f'Parabens voce acertou em {tentativas}')
        break
    else:
        if chute > segredo:
            print(f'Errou numero menor que {chute}')
        else:
            print(f'Errou numero maior que {chute}')