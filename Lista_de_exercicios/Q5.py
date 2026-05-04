# programa para calcular area de quadrado, triangulo
# trapezio e informar qual a maior

print('''
        Programa para calcular area de quadrado, triangulo
        trapezio e informar qual a maior
''')
# quadrado
lado = float(input('Informe o lado do quadrado:'))
# triangulo
base = float(input('Informe a base do triangulo:'))
altura = float(input('Informe a altura do triangulo:'))
#trapezio
base_maior = float(input('Informe a base maior do trapezio:'))
base_menor = float(input('Informe a base menor do trapezio:'))
altura_trapezio = float(input('Altura do Trapezio:'))

area_quadrado = lado**2
area_triangulo = (base*altura)/2
area_trapezio = (base_maior + base_menor)*altura_trapezio/2

print(f'Quadrado ={area_quadrado}')
print(f'Triangulo = {area_triangulo}')
print(f'Trapezio ={area_trapezio}')

if area_quadrado > area_triangulo and area_quadrado > area_trapezio:
    print('Quadrado tem maior area')
elif area_triangulo > area_quadrado and area_triangulo > area_trapezio:
    print('Triangulo tem maior area')
else :
    print('Trapezio tem maior area')
    