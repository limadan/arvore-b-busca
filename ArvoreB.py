from NodoArvore import NodoArvore
from ordenator import Ordenator

ordenador = Ordenator()

class ArvoreB:
    def __init__(self, ordem):
        self.raiz = NodoArvore()
        self.ordem = ordem

    def inserir(self, nodo, elemento):
        if(len(nodo.filhos)==0):
            nodo.pagina.append(elemento)
        else:
            if self.verifica_se_e_o_maior_da_pagina(nodo.pagina, elemento):
                self.inserir(nodo.filhos[len(nodo.filhos) - 1], elemento)
            
            for i in range(len(nodo.pagina)):
                if(elemento < nodo.pagina[i]):
                    self.inserir(nodo.filhos[i], elemento)

        ordenador.insercao(nodo.pagina)
        
        if(len(nodo.pagina) > 2 * self.ordem):
            self.divide_nodo(nodo)

    def verifica_se_e_o_maior_da_pagina(self, pagina, elemento):
        eMaior = True
        for i in range(len(pagina)):
            if(elemento < pagina[i]):
                eMaior = False
        return eMaior

    def buscar(self, nodo, elemento):
        if not nodo:
            return None  # Elemento não encontrado

        i = 0
        while i < len(nodo.pagina) and elemento > nodo.pagina[i]:
            i += 1

        if i < len(nodo.pagina) and elemento == nodo.pagina[i]:
            return nodo  # Elemento encontrado no nodo atual

        if len(nodo.filhos) == 0:
            return None  # Elemento não encontrado

        return self.buscar(nodo.filhos[i], elemento)

    def remover(self):
        pass

    def divide_nodo(self, nodo):
        indice_do_meio = len(nodo.pagina) // 2
        elemento_do_meio = nodo.pagina[ indice_do_meio ]

        if(nodo.pai == None):
            pai = NodoArvore()
            nodo.pai = pai
            nodo.pai.filhos.append(nodo)
            self.raiz = pai
        
        nodo.pai.pagina.append(elemento_do_meio)
        ordenador.insercao(nodo.pai.pagina)

        metade1 = nodo.pagina[:indice_do_meio]
        metade2 = nodo.pagina[indice_do_meio + 1:]

        nodo.pagina = metade1

        novo_nodo = NodoArvore()
        novo_nodo.pagina = metade2
        novo_nodo.pai = nodo.pai
    
        nodo.pai.filhos.append(novo_nodo)

        if(len(nodo.filhos) > 0):
            filho_do_meio = len(nodo.filhos) // 2
            metade1 = nodo.filhos[:filho_do_meio]
            metade2 = nodo.filhos[filho_do_meio:]

            nodo.filhos = metade1
            novo_nodo.filhos = metade2

        if(len(nodo.pai.pagina) > 2 * self.ordem):
            self.divide_nodo(nodo.pai)

    def printArvore(self, nodo):
        print(nodo.pagina)
        for filho in nodo.filhos:
            self.printArvore(filho)