class Ordenator:
    def __init__(self):
        pass
    
    def selecao(self, v):
        cont=0
        for i in range(0, len(v)-1):
            cont+=1
            min_index = i
            for j in range(i + 1, len(v)):
                cont+=1
                if v[j].compara(v[min_index]) < 0:
                    min_index = j
                    cont+=1
            x = v[min_index]
            v[min_index] = v[i]
            v[i] = x
            cont+=3
        return cont
    
    def insercao(self, v):
        cont=0
        for i in range(1, len(v)):
            cont+=1
            for j in range(i, 0, -1):
                cont+=1
                if v[j] < (v[j - 1]):
                    aux = v[j]
                    v[j] = v[j - 1]
                    v[j - 1] = aux
                    cont+=3
        return cont
    
    def shell_sort(self, v):
        cont=0
        salto = 1
        salto = salto * 2 + 1
        while(salto < len(v)):
             salto = salto * 2 + 1
        salto//=2
        while salto!=1:
            for i in range(salto, len(v)):
                cont+=1
                for j in range(i, 0, -salto):
                    cont+=1
                    if v[j].compara(v[j - salto]) < 0:
                        aux = v[j]
                        v[j] = v[j - salto]
                        v[j - salto] = aux
                        cont+=3
            salto//=2
        cont_insercao = self.insercao(v)

        return cont + cont_insercao

    def bubble_sort(self, v):
        cont_bolha=1
        for i in range(len(v)):
            cont_bolha+=1
            for j in range(len(v)):
                cont_bolha+=1
                if v[j].compara(v[i]) > 0:
                    aux = v[j]
                    v[j] = v[i]
                    v[i] = aux
                    cont_bolha+=3
        return cont_bolha

    def quick_sort(self, v, index_esquerda, index_direita): #passa como parametro (vetor_x, 0, len(vetor_x)-1)
        cont = 0

        i = index_esquerda
        j = index_direita
        pivo = ((index_direita - index_esquerda )//2) + index_esquerda
        
        cont+=3

        while i<=j:
            #print("i: ", i)
            #print("j: ", j)
            #print("vetor: ", v)
            #print("pivo: ", pivo)

            cont+=1
            if (v[i] < v[pivo]) and (v[j] > v[pivo]):
                i+=1
                j-=1
                cont+=3
                #print("i: ", i)
                #print("j: ", j)
                #print("vetor: ", v)
                #print("pivo: ", pivo)
            elif (v[i]< v[pivo]) and (v[j]<v[pivo]):
                i+=1
                cont+=2
                #print("i: ", i)
                #print("j: ", j)
                #print("vetor: ", v)
                #print("pivo: ", pivo)
            elif (v[i] > v[pivo]) and (v[j] > v[pivo]):
                j-=1
                cont+=2
                #print("i: ", i)
                #print("j: ", j)
                #print("vetor: ", v)
                #print("pivo: ", pivo)
            elif(v[i] >= v[pivo]) and (v[j] < v[pivo]):
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
                i+=1
                j-=1
                cont+=5
                #print("i: ", i)
                #print("j: ", j)
                #print("vetor: ", v)
                #print("pivo: ", pivo)
            else:
                break
                #aux = v[i]
                #v[i] = v[j]
                #v[j] = aux
                #i+=1
                #j-=1
                #cont+=5
                #print("i: ", i)
                #print("j: ", j)
                #print("vetor: ", v)
                #print("pivo: ", pivo)
        
        if(index_direita - index_esquerda + 1 > 3):
            cont+=1
            cont+=self.quick_sort(v, index_esquerda, j)
            cont+=self.quick_sort(v, i, index_direita)
        return cont
        
#heap sort
    def heap_sort(self, v):
        cont = 0
        tamanho_vetor = len(v)

        cont+=1
        for i in range(tamanho_vetor // 2 - 1, -1, -1):
            cont+=1
            cont+=self.constroi_heap(v, tamanho_vetor, i)

        for i in range(tamanho_vetor - 1, 0, -1):
            aux = v[0]
            v[0] = v[i]
            v[i] = aux
            cont+=3
            cont+=self.constroi_heap(v, i, 0)
        return cont

    def constroi_heap(self, v,n, i):
        cont=0
        pai = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2
        cont+=3

        if esquerda < n and v[esquerda]>(v[pai]):
            pai = esquerda
            cont+=2

        if direita < n and v[direita]>(v[pai]):
            pai = direita
            cont+=2

        if pai != i:
            aux= v[pai]
            v[pai] = v[i]
            v[i] = aux
            cont+=3
            cont+=self.constroi_heap(v, n, pai)
        return cont

    def merge_sort(self, v):
        cont = 0
        if len(v) > 1:
            meio = len(v) // 2 
            esquerda = v[:meio]
            direita = v[meio:]
            cont+=3
            cont+=self.merge_sort(esquerda)
            cont+=self.merge_sort(direita)

            i = j = k = 0
            cont+=3

            while i < len(esquerda) and j < len(direita):
                cont+=1
                if esquerda[i].compara(direita[j]) < 0:
                    v[k] = esquerda[i]
                    i += 1
                    cont+=2
                else:
                    v[k] = direita[j]
                    j += 1
                    cont+=2
                k += 1
                cont+=1

            while i < len(esquerda):
                v[k] = esquerda[i]
                i += 1
                k += 1
                cont+=3

            while j < len(direita):
                v[k] = direita[j]
                j += 1
                k += 1
                cont+=3
            
            return cont
        return 0