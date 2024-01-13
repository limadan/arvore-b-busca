import os

class NodoArvore:
    def __init__(self, arquivo_da_pagina):
        diretorio_paginas = "./paginas"
        caminho_completo = os.path.join(diretorio_paginas, arquivo_da_pagina)
        self.arquivo_da_pagina = caminho_completo
        self.pai = None
        self.tamanho_da_pagina = 0
        self.pagina = []
        self.filhos = []

    def carrega_pagina_em_memoria(self):
        self.pagina = []
        try:
            arquivo = open(self.arquivo_da_pagina, "r")
            for linha in arquivo:
                numero = float(linha)
                self.pagina.append(numero)
            self.tamanho_da_pagina = len(self.pagina)
        except:
            arquivo = open(self.arquivo_da_pagina, "a")
            self.pagina = []
    
    def escreve_pagina_em_memoria(self):
        try:
            arquivo = open(self.arquivo_da_pagina, "w")
            arquivo.write("")
            arquivo.close()
        except:
            pass
        arquivo = open(self.arquivo_da_pagina, "a")
        
        for registro in self.pagina:
            arquivo.write(str(registro)+'\n')

        arquivo.close()
        self.pagina = []