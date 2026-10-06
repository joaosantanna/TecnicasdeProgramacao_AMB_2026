alunos = {
    "Ana": {"Mat": 8.5, "Prog": 9.0},
    "Bruno": {"Mat": 6.0, "Prog": 7.5},
    "Carla": {"Mat": 9.5, "Prog": 10.0},
    "Pedro": {"Mat": 7.5, "Prog": 8.6}
}

nome = input('Informe o nome do aluno:')
resposta = alunos.get(nome)
if resposta == None :
    print('Aluno não consta no banco de dados')
else:
    print(f'Aluno : {nome}')
    media = sum(resposta.values())/2
    print(f'Media ={media}')