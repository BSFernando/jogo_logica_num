import random
import pandas
import operator

class Jogando():
    def jogada(self, lista):
        
        self.cima = lista[0]
        self.baixo = lista[1]
        self.meio_cima = lista[2]
        self.meio_baixo = lista[3]
        self.esq_cima = lista[4]
        self.esq_baixo = lista[5]
        self.dir_cima = lista[6]
        self.dir_baixo = lista[7]
        self.respostas = [[2, 7, 8, 1, 6, 4, 5, 3], [7, 2, 1, 8, 3, 5, 4, 6], 
                         [2, 7, 8, 1, 5, 3, 6, 4], [7, 2, 1, 8, 4, 6, 3, 5]]
        self.regras()

    def regras(self):

        self.lista_pos_redor = [[self.meio_cima, self.esq_cima, self.dir_cima], 
                [self.meio_baixo, self.esq_baixo, self.dir_baixo],
                [self.cima, self.esq_cima, self.dir_cima, self.meio_baixo,
                 self.esq_baixo, self.dir_baixo],[self.baixo, self.esq_baixo,
                self.dir_baixo, self.meio_cima, self.esq_cima, self.dir_cima],
                [self.cima, self.meio_cima, self.meio_baixo, self.esq_baixo],
                [self.baixo, self.meio_cima, self.meio_baixo, self.esq_cima],
                [self.cima, self.meio_cima, self.meio_baixo, self.dir_baixo],
                [self.baixo, self.meio_cima, self.meio_baixo, self.dir_cima]]

        self.lista_pos = [self.cima, self.baixo, self.meio_cima, self.meio_baixo, 
                        self.esq_cima, self.esq_baixo, self.dir_cima, self.dir_baixo]
        self.confere()
    
    def confere(self):
        
        lista_base = [1,2,3,4,5,6,7,8]
        
        for num in range(len(self.lista_pos)):
            if ((self.lista_pos[num] + 1) in (self.lista_pos_redor[num])
            or (self.lista_pos[num] - 1) in (self.lista_pos_redor[num])
            or (self.lista_pos[num]) in (self.lista_pos_redor[num])):
                valor = 0
                break
            else:
                valor = 1
                pass
            
        if valor == 0:
            self.resultado_conf(False)
        else:
            self.resultado_conf(True)

    def minus(self, lista_1, lista_2):
        return sum(map(abs,(list(map(operator.sub,lista_1, lista_2)))))
    
    def resultado_conf(self, resultado):
        
        if resultado == False:
            confere = []
            for item in self.respostas:
                confere.append(self.minus(self.lista_pos,item))
            resposta = min(confere)                 
            self.resposta = resposta/32
            return self.resposta
            
        else:
            confere = []
            for item in self.respostas:
                confere.append(self.minus(self.lista_pos,item))
            resposta = min(confere)                 
            self.resposta = resposta/32
            return self.resposta
