def analisar_diagonal_principal(tab):
    valor = tab[0][0]
    for l in range(3):
        if valor != tab[l][l]:
            return False
    return valor
            
        

tabuleiro = [["X", ".", "O"],
             ["O", "X", "."],
             [".", ".", "X"]]

resposta = analisar_diagonal_principal(tabuleiro)
if resposta == False:
    print('Não teve vencedor')
else:
    print(f' Vencedor = {resposta}')