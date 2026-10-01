estoque = [["Teclado", 10, 150.0],
           ["Mouse", 0, 85.0],
           ["Monitor", 5, 900.0],
           ["Fone", 0, 120.0]
           ]
disponiveis =[]

for item in estoque:
    if item[1] > 0 :
        disponiveis.append(item)
        
print('Itens disponiveis na loja')
for item in disponiveis:
    print(item)