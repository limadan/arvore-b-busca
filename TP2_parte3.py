from ArvoreB import ArvoreB

ordem = 10000

arvoreB = ArvoreB(ordem)

arquivo_ordenado = open('arquivo-teste-ordenado.txt')

print("Estou inserindo os elementos...")

for linha in arquivo_ordenado:
    numero = float(linha)
    arvoreB.inserir(arvoreB.raiz, numero)

print("Finalizei a inserção!")

arquivo_ordenado.close()

arvoreB.printArvore(arvoreB.raiz)

arvoreB.buscar(arvoreB.raiz, 0.005263392773095177)

arvoreB.remover(arvoreB.raiz, 0.005263392773095177)

arvoreB.buscar(arvoreB.raiz, 0.005263392773095177)

'''
- Percebeu-se que o algoritmo implmentado pela dupla leva muito tempo para montar toda a árvore em memória
- A dupla criou uma amostra menor ainda do arquivo de teste com 5000 registros
- Os 5000 registros foram todos carregados na memória usando o método heap sort para ordenação
- O método de inserção ficou muito demorado, mesmo com o arquivo de 5000 registros, invalidando a hipótese estabelecida
  de que o algoritimo seria menos custoso por as páginas estarem parcialmente ordenadas.

'''