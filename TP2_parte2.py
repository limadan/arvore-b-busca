from ArvoreB import ArvoreB

ordem = 2

arvoreB = ArvoreB(ordem)

print("Estou inserindo elementos na arvore...")


arvoreB.inserir(arvoreB.raiz, 1)
arvoreB.inserir(arvoreB.raiz, 2)
arvoreB.inserir(arvoreB.raiz, 3)
arvoreB.inserir(arvoreB.raiz, 4)
arvoreB.inserir(arvoreB.raiz, 5)
arvoreB.inserir(arvoreB.raiz, 6)
arvoreB.inserir(arvoreB.raiz, 7)
arvoreB.inserir(arvoreB.raiz, 8)
arvoreB.inserir(arvoreB.raiz, 9)
arvoreB.inserir(arvoreB.raiz, 10)


print("Inseri tudo!")

print("Árvore B antes das remoções")
arvoreB.printArvore(arvoreB.raiz)

arvoreB.remover(arvoreB.raiz, 6)

print("Árvore após remoções")
arvoreB.printArvore(arvoreB.raiz)

arvoreB.remover(arvoreB.raiz, 7)

print("Árvore após remoções")
arvoreB.printArvore(arvoreB.raiz)

arvoreB.remover(arvoreB.raiz, 50)