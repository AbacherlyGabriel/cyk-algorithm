from Input import FileReader

"""
Implementacao do algoritmo CYK para Gramaticas Livres do Contexto
"""

class CYK:

    """
    Acessando listas que contem as especificacoes das GLCs e das cadeias de teste 
    """

    def __init__(self):
        self.gramaticas = FileReader().glcs
        self.cadeias = FileReader().cadeias

    """
    """

    def algoritmo_cyk(self):
        #print(self.gramaticas)
        #print(self.cadeias)

        qtd_glcs = int(self.gramaticas[0])          # Quantidade de GLCs

        for glc in range(qtd_glcs):
            print(f'glc {glc}')


# Testes
CYK().algoritmo_cyk()