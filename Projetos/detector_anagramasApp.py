import PySimpleGUI as sg
from util_anagrama import processar_palavras

sg.theme('Reddit')


desenho =[
        [sg.Push(),sg.Text('Detector de Anagramas',font=('Helvetica',18)),
         sg.Push()],
        [sg.Text('Primeira Palavra:',size=(15,1)),
         sg.InputText(key='-P1-')],
        [sg.Text('Segunda Palavra:',size=(15,1)),
         sg.InputText( key='-P2-')],
        [sg.Text('>>>',key='-SAIDA-')],
        [sg.Submit(),sg.Button('Limpar Campos'),sg.Button('Sair')]
    ]

janela = sg.Window('Anagrama detect ',layout=desenho,
                   font=('Helvetica',14))

while True:
    
    evento,valores = janela.Read()
    
    if evento in ('Sair',sg.WIN_CLOSED):
        break
    elif evento == 'Submit':
        p1 = valores['-P1-']
        p2 = valores['-P2-']
        resposta = processar_palavras(p1,p2)
        if resposta == True:
            janela['-SAIDA-'].update(f'>>> {p1} e {p2} são Anagramas')
        else:
            janela['-SAIDA-'].update(f'>>> {p1} e {p2} não são Anagramas')
    
    elif evento == 'Limpar Campos':
        janela['-P1-'].update('')
        janela['-P2-'].update('')
    else:
        print('Comando não cadastrado')
    
    
janela.close()
