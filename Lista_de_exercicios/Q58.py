print('Detector de anagramas')
p1 = input('Digite a primeira palavra:')
p2 = input('Digite a segunda palavra:')

# transforma a string em uma lista de letras
p1 = list(p1.lower())
p2 = list(p2.lower())

# pega as letras unicas num conjunto de letras
# sem repetição
l1 = set(p1)
l2 = set(p2)

contador1=dict()
contador2=dict()
# montando a contagem de letras
for l in l1:
    contador1[l] = p1.count(l)
for l in l2:
    contador2[l] = p2.count(l)

eh_anagrama = True
for k in contador1.keys():
    if contador1.get(k) == contador2.get(k):
        pass
    else:
        eh_anagrama = False
        break
   
# teste para saber se as duas palavras tem o mesmo numero de chaves
# se não tiverem é pq tb não são anagramas
if len(contador1.keys()) != len(contador2.keys()):
    eh_anagrama= False
    
if eh_anagrama:
    print('As duas palavras são anagramas')
else:
    print('As duas palavras não são anagramas')

