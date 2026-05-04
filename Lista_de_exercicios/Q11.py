# programa para testar se aluno foi
# aprovado ou reprovado

print('Programa verificar aprovação')
nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))
nota3 = float(input('Informe a terceira nota:'))

media = (nota1 + nota2 + nota3)/3

if media >= 6 :
    print(f'Aluno aprovado media = {media}')
else:
    print(f'Aluno reprovado media = {media}')

print('Obrigado por usar meu aplicativo')

