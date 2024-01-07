from ArvoreB import ArvoreB

ordem = 2

arvoreB = ArvoreB(ordem)

print("Estou inserindo elementos na arvore...")

for i in range(17):
    arvoreB.inserir(arvoreB.raiz, i+1)

arvoreB.printArvore(arvoreB.raiz)

print("Inseri tudo!")