from NodoArvore import NodoArvore
from ordenator import Ordenator
import os

ordenador = Ordenator()

class ArvoreB:
    def __init__(self, ordem):
        self.contador_paginas = 0
        self.raiz = NodoArvore('pagina0.txt')
        self.ordem = ordem

    def inserir(self, nodo, elemento):
        nodo.carrega_pagina_em_memoria()
        
        if(len(nodo.filhos)==0):
            nodo.pagina.append(elemento)
            nodo.tamanho_da_pagina += 1
            ordenador.heap_sort(nodo.pagina)

            if(nodo.tamanho_da_pagina > 2 * self.ordem):
                self.divide_nodo(nodo)
            else:
                nodo.escreve_pagina_em_memoria()
        else:
            if self.verifica_se_e_o_maior_da_pagina(nodo.pagina, elemento):
                self.inserir(nodo.filhos[len(nodo.filhos) - 1], elemento)
            
            for i in range(len(nodo.pagina)):
                if(elemento < nodo.pagina[i]):
                    self.inserir(nodo.filhos[i], elemento)

    def verifica_se_e_o_maior_da_pagina(self, pagina, elemento):
        eMaior = True
        for i in range(len(pagina)):
            if(elemento < pagina[i]):
                eMaior = False
        return eMaior

    def buscar(self, nodo, elemento):
        if not nodo:
            print(f"O elemento {elemento} não foi encontrado na árvore.")
            return None
        i = 0

        nodo.carrega_pagina_em_memoria()
        while i < len(nodo.pagina) and elemento > nodo.pagina[i]:
            i += 1

        if i < len(nodo.pagina) and elemento == nodo.pagina[i]:
            print(f"O elemento {elemento} está no arquivo {nodo.arquivo_da_pagina} na linha {i+1}")
            return nodo

        if len(nodo.filhos) == 0:
            return None
        
        nodo.pagina = []

        return self.buscar(nodo.filhos[i], elemento)
    
    def remover(self, nodo, elemento):
        nodo.carrega_pagina_em_memoria()
        i = 0
        while i < len(nodo.pagina) and elemento > nodo.pagina[i]:
            i += 1

        if i < len(nodo.pagina) and elemento == nodo.pagina[i]:
            if len(nodo.filhos) == 0:
                nodo.pagina.pop(i)
                nodo.escreve_pagina_em_memoria()
            else:
                filho = nodo.filhos[i]
                filho_proximo = nodo.filhos[i + 1]
                if len(nodo.pagina) > self.ordem:
                    antecessor = self.buscar_antecessor(filho)
                    nodo.pagina[i] = antecessor
                    self.remover(filho, antecessor)
                elif len(filho_proximo.pagina) > self.ordem:
                    sucessor = self.buscar_sucessor(filho_proximo)
                    nodo.pagina[i] = sucessor
                    self.remover(filho_proximo, sucessor)
                else:
                    self.mesclar_nodos(nodo, i, filho, filho_proximo)
                    self.remover(filho, elemento)
        else:
            nodo.pagina = []
            nodo.filhos[i].carrega_pagina_em_memoria()
            if len(nodo.filhos) == 0:
                print(f"O elemento {elemento} não existe na árvore B.")
                return
            elif len(nodo.filhos[i].pagina) < self.ordem:
                self.revalidar_nodo(nodo, i)

            self.remover(nodo.filhos[i], elemento)
    '''
        - busca_antecessor*
        - busca_sucessor*
        - mesclar_nodos*
        - revalidar_nodo
        - ceder_elemento_irmao_esquerdo-
        - ceder_elemento_irmao_direito-
        - divide_nodo
        atualizar
    '''
    def buscar_antecessor(self, nodo):
        while not len(nodo.filhos) == 0:
            nodo = nodo.filhos[-1]

        nodo.carrega_pagina_em_memoria()
        elemento = nodo.pagina[-1]
        nodo.pagina = []

        return elemento
    
    def buscar_sucessor(self, nodo):
        while not len(nodo.filhos) == 0:
            nodo = nodo.filhos[0]
        nodo.carrega_pagina_em_memoria()
        elemento = nodo.pagina[0]
        nodo.pagina = []

        return elemento

    def mesclar_nodos(self, nodo, i, filho, filho_proximo):
        filho.carrega_pagina_em_memoria()
        filho_proximo.carrega_pagina_em_memoria()

        filho.pagina.append(nodo.pagina[i])
        filho.pagina.extend(filho_proximo.pagina)
        filho.filhos.extend(filho_proximo.filhos)
        nodo.pagina.pop(i)
        nodo.filhos.pop(i + 1)

        if len(nodo.pagina) == 0:  
            self.raiz = filho_proximo
        
        nodo.escreve_pagina_em_memoria()
        filho.escreve_pagina_em_memoria()
        os.remove(filho_proximo.arquivo_da_pagina)

    def revalidar_nodo(self, nodo, i):
        nodo.filhos[i - 1].carrega_pagina_em_memoria()
        nodo.filhos[i + 1].carrega_pagina_em_memoria()
        if i > 0 and len(nodo.filhos[i - 1].pagina) > self.ordem:
            self.ceder_elemento_irmao_esquerdo(nodo, i)
        elif i < len(nodo.filhos) - 1 and len(nodo.filhos[i + 1].pagina) > self.ordem:
            self.ceder_elemento_irmao_direito(nodo, i)
        else:
            if i > 0:
                self.mesclar_nodos(nodo, i - 1, nodo.filhos[i - 1], nodo.filhos[i])
                i -= 1
            else:
                self.mesclar_nodos(nodo, i, nodo.filhos[i], nodo.filhos[i + 1])
        nodo.filhos[i-1].pagina = []
        nodo.filhos[i+1].pagina = []

    def ceder_elemento_irmao_esquerdo(self, nodo, i):
        nodo.carrega_pagina_em_memoria()
        filho = nodo.filhos[i]
        irmao = nodo.filhos[i - 1]

        irmao.carrega_pagina_em_memoria()

        nodo.filhos.insert(0, nodo.filhos[i - 1])
        nodo.pagina[i - 1] = irmao.pagina.pop()
        if not len(filho.filhos) == 0:
            filho.filhos.insert(0, irmao.filhos.pop())
        
        nodo.escreve_pagina_em_memoria()
        irmao().escreve_pagina_em_memoria()
    
    def ceder_elemento_irmao_direito(self, nodo, i):
        nodo.carrega_pagina_em_memoria()

        filho = nodo.filhos[i]
        irmao = nodo.filhos[i + 1]

        irmao.carrega_pagina_em_memoria()
        filho.carrega_pagina_em_memoria()

        filho.pagina.append(nodo.pagina[i])
        nodo.pagina[i] = irmao.pagina.pop(0)
        if not len(filho.filhos) == 0:
            filho.filhos.append(irmao.filhos.pop(0))

        nodo.escreve_pagina_em_memoria()
        irmao.escreve_pagina_em_memoria()
        filho.escreve_pagina_em_memoria()
    
    def divide_nodo(self, nodo):
        indice_do_meio = len(nodo.pagina) // 2
        elemento_do_meio = nodo.pagina[ indice_do_meio ]

        if(nodo.pai == None):
            self.contador_paginas+=1
            pai = NodoArvore("pagina"+str(self.contador_paginas)+".txt")
            nodo.pai = pai
            nodo.pai.filhos.append(nodo)
            self.raiz = pai
        
        nodo.pai.carrega_pagina_em_memoria()
        nodo.pai.pagina.append(elemento_do_meio)
        nodo.pai.tamanho_da_pagina = len(nodo.pai.pagina)
        ordenador.heap_sort(nodo.pai.pagina)

        metade1 = nodo.pagina[:indice_do_meio]
        metade2 = nodo.pagina[indice_do_meio + 1:]

        nodo.pagina = metade1
        nodo.tamanho_da_pagina = len(metade1)

        self.contador_paginas += 1
        novo_nodo = NodoArvore("pagina"+str(self.contador_paginas)+".txt")
        novo_nodo.pagina = metade2
        novo_nodo.tamanho_da_pagina = len(metade2)
        novo_nodo.pai = nodo.pai
    
        nodo.pai.filhos.append(novo_nodo)

        if(len(nodo.filhos) > 0):
            filho_do_meio = len(nodo.filhos) // 2
            metade1 = nodo.filhos[:filho_do_meio]
            metade2 = nodo.filhos[filho_do_meio:]

            nodo.filhos = metade1
            novo_nodo.filhos = metade2

        if(nodo.pai.tamanho_da_pagina > 2 * self.ordem):
            self.divide_nodo(nodo.pai)
        
        nodo.escreve_pagina_em_memoria()
        novo_nodo.escreve_pagina_em_memoria()
        nodo.pai.escreve_pagina_em_memoria()

    def printArvore(self, nodo):
        print(nodo.arquivo_da_pagina)
        for filho in nodo.filhos:
            self.printArvore(filho)