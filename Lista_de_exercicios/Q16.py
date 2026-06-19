print('Programa para determinar o signo do zodiaco do usuario')
dia = int(input('Dia de nascimento:'))
mes = int(input('Mes de nascimento:'))

if mes == 4:
    if dia <= 20 :
        print('Aries')
    else:
        print('Touro')
if mes == 5:
    if dia <= 20 :
        print('Touro')
    else:
        print('Gemeos')
if mes == 6:
    if dia <= 20 :
        print('Gemeos')
    else:
        print('Cancer')
if mes == 7:
    if dia <= 21 :
        print('Cancer')
    else:
        print('Leão')
# so implementei uma parte da tabela , veja a logica
# e implemente o restante :-)