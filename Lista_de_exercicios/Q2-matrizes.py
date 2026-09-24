tabuleiro = [["X", ".", "O"], ["O", "X", "."], [".", ".", "X"]]
for l in tabuleiro:
    print(l)

# verificando se temos vencedor
valor = tabuleiro[0][0] # coordenada 0 0 ja verificada
diferente = False
for i in range(1,3):
    if tabuleiro[i][i] != valor:
        diferente = True
        break
if not diferente:
    print(f'O vencedor é o jogador {valor}')

# desafio , use o choice de random para preencher todo o tabuleiro aleatoriamente
# e no final imprima o tabuleiro e verifique se alguem venceu 
    