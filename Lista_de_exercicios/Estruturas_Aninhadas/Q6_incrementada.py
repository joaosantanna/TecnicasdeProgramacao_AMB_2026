inventario = {
    "armas": ["espada", "arco"],
    "pocoes": {"cura": 5, "mana": 2},
    "ouro": 150
    }

while True:
    
    print('''
        Micro RPG
        0- sair
        1 - adicionar nova arma
        2 - atualizar pocoes
        3 - listar ouro
        4 - lista inventario completo
    ''')
    op = int(input('>'))
    if op == 0:
        break
    if op == 1:
        nova_arma = input('Informe nova arma:')
        armas = inventario['armas']
        armas.append(nova_arma)
        print(inventario['armas'])
    if op == 2:
        escolha = input('Atualizar cura ou mana?')
        valor = int(input('Valor para atualizar:'))
        inventario['pocoes'][escolha] += valor
        print(inventario['pocoes'])
    if op == 3:
        print(f' Quantidade de ouro:{inventario["ouro"]}')
    if op == 4:
        print('Inventario mini RPG')
        print(f'Armas {inventario["armas"]}')
        print(f'Poções {inventario["pocoes"]}')
        print(f'Ouro {inventario["ouro"]}')
        