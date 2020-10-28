import numpy as np
import pandas as pd
import random
import jogo_treino
      
chance_mut = 0.3   
chance_cross = 0.35  
numero_ind = 15
melhores_ind = 3

def popu(n):
    grupo =[]
    teste = jogo_treino.Jogando()
    contador = 0
    while contador < n:
        lista_base= [1,2,3,4,5,6,7,8]
        random.shuffle(lista_base)
        teste.jogada(lista_base)
        if lista_base in [[2, 7, 8, 1, 6, 4, 5, 3], [7, 2, 1, 8, 3, 5, 4, 6],
                    [2, 7, 8, 1, 5, 3, 6, 4], [7, 2, 1, 8, 4, 6, 3, 5]]:
            pass
        elif teste.resposta < 0.5:
            pass
        elif lista_base in grupo:
            pass
        else:
            grupo.append(lista_base)
            contador = contador + 1
    return grupo
                                           
def calcular_treino(joga, individuo):
                         
    play = joga
    play.jogada(individuo)
    
    return play.resposta

def ordenar_lista(lista, ordenacao, decrescente=False):

    return [x for _, x in sorted(zip(ordenacao, lista), key=lambda p: p[0], reverse=decrescente)]

    
def crossover(ind1, ind2):
    
    filho = ind1.copy()
    certo, lista_certo, errado, lista_errado = [], [], [], []
    contador = 0
    
    if np.random.uniform(0, 1) < chance_cross:
        
        filho = []
        
        for item in range(len(ind1)):
            if ind1[item] == ind2[item]:
                    certo.append(item)
                    lista_certo.append(ind1[item])
            else:
                    errado.append(item)
                    lista_errado.append(ind2[item])

        while contador < 8:
            
            if contador in certo:
                    filho.append(ind1[contador])
            else:
                    random.shuffle(lista_errado)
                    filho.append(lista_errado[0])
                    lista_errado.remove(lista_errado[0])
            contador = contador + 1
	
    return filho

def mutacao(ind):
    
    if np.random.uniform(0, 1) < chance_mut:
        random.shuffle(ind)
    filho = ind
    return filho

def proxima_geracao(grupo, treino):

    ordenados = ordenar_lista(grupo, treino)
    proxima_ger = ordenados[:melhores_ind]

    while len(proxima_ger) < numero_ind:

        ind1, ind2 = random.choices(grupo, k=2)
        filho = crossover(ind1, ind2)
        filho = mutacao(filho)
        proxima_ger.append(filho)

    return proxima_ger

jogo = jogo_treino.Jogando()
grupo = popu(numero_ind)
treino = []
geracao = 0

while np.count_nonzero(treino) != 12: #apenas 3 ind vitoriosos na geração

    treino = []
    for ind in grupo:
        treino.append(calcular_treino(jogo, ind))

    grupo = proxima_geracao(grupo, treino)
    
    lista = list(range(100,10000000,100))
    if geracao in lista:
        print('-------------------')
        print(geracao) #mostra a cada 100 gerações
        print('-------------------')
    else:
        pass
    a = treino.copy()
    a.sort()  
    print(a[0:8])#mostra 8 melhores resultados do jogo
    
    geracao = geracao+1
    
treino = []
                         
for ind in grupo:
    treino.append(calcular_treino(jogo, ind))

ordenada = ordenar_lista(grupo, treino)
treino.sort()

print('-------------------')
contador = 0
while contador < len(grupo):
    texto = "%s, %s" % (str(treino[contador]),str(ordenada[contador]))
    print(texto.rjust(40)) #ultimo grupo
    contador = contador+1
print('-------------------')

input()