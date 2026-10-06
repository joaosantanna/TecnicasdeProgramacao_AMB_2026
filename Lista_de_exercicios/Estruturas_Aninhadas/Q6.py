inventario = {
    "armas": ["espada", "arco"],
    "pocoes": {"cura": 5, "mana": 2},
    "ouro": 150
    }

print(inventario)
armas = inventario['armas']
armas.append('Adaga')
inventario['pocoes']['cura'] -= 1
print(inventario['ouro'])
print(inventario)