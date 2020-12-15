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
    Implementacao do Algoritmo CYK
    """

    def algoritmo_cyk(self):
        index_especs = 1                                                                            # Indice das especificacoes das GLCs na lista de entrada
        index_variaveis = 2                                                                         # Indice das variaveis das GLCs na lista de entrada
        index_terminais = 3                                                                         # Indice dos terminais das GLCs na lista de entrada
        index_regras = 4                                                                            # Indice das regras das GLCs na lista de entrada
        index_cadeias = 0                                                                           # Indice da quantidade de cadeias correspondentes a primeira GLC

        qtd_glcs = int(self.gramaticas[0])                                                          # Quantidade de GLCs

        for glc in range(qtd_glcs):
            qtd_variaveis, qtd_terminais, qtd_regras = map(int, self.gramaticas[index_especs].split())              # Especificacoes das GLCs
            
            variaveis = self.gramaticas[index_variaveis].split()                                                    # Variaveis das GLCs
            terminais = self.gramaticas[index_terminais].split()                                                    # Terminais das GLCs
            regras = self.gramaticas[index_regras:index_regras + qtd_regras]                                        # Regras das GLCs

            qtd_cadeias = int(self.cadeias[index_cadeias])                                                          # Quantidade de cadeias de teste

            print(f'\nglc {glc}')
            print(f'qtd variaveis: {qtd_variaveis}')
            print(f'qtd terminais: {qtd_terminais}')
            print(f'qtd regras: {qtd_regras}')
            print(f'\nvariaveis: {variaveis}')
            print(f'terminais: {terminais}')
            print(f'regras: {regras}\n')

            """
            Leitura das cadeias de teste e execucao do algoritmo
            """

            while qtd_cadeias > 0:
                index_cadeias += 1                                                                                  # Atualizando indice
                qtd_cadeias -= 1                                                                                    # Atualizando quantidade de cadeias

                cadeia = self.cadeias[index_cadeias].split()                                                        # Lista contendo os simbolos da cadeia

                print(f'cadeia: {cadeia}')

                """
                Validando se o teste eh a cadeia vazia, alem de checar
                se a substituicao faz parte do conjunto de regras
                """

                if ('&' in cadeia) and (len(cadeia) == 1):
                    return True

            index_especs += qtd_regras + 3                                                                          # Atualizando indice
            index_variaveis += qtd_regras + 3                                                                       # Atualizando indice
            index_terminais += qtd_regras + 3                                                                       # Atualizando indice
            index_regras += qtd_regras + 3                                                                          # Atualizando indice
            index_cadeias += 1                                                                                      # Atualizando indice
            

# Testes
print(CYK().algoritmo_cyk())