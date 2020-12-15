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
    Formatacao das regras de uma GLC em um dicionario
    """

    def regras_to_dict(self, variaveis, regras):
        regras_de_substituicao = {variavel: [] for variavel in variaveis}

        for regra in regras:
            regra_lista = regra.split()

            variavel = regra_lista[0]
            substituicoes = regra_lista[2:]
            
            regras_de_substituicao[variavel].append(substituicoes)

        #variavel_inicial = list(regras_de_substituicao.keys())[0]
        return regras_de_substituicao

    """
    Inicializacao da tabela de resultados dado o tamanho da cadeia de teste
    """

    def criar_tabela(self, tam_cadeia):
        tabela = []

        for i in range(tam_cadeia):
            tabela.append([])

            for j in range(tam_cadeia):
                tabela[i].append([])

        return tabela

    """
    Busca por regras especificadas no parametro da funcao
    """

    def busca(self, regras=None, variavel=None, terminal=None):
        if (regras is not None) and (terminal is not None):
            substituicoes = regras.values()
            
            if (variavel is not None):
                substituicoes = regras[variavel]

            for lista_substituicoes in substituicoes:
                for substituicao in lista_substituicoes:
                    if terminal in substituicao:
                        return True

        return False

    """
    Implementacao do Algoritmo CYK
    """

    def algoritmo_cyk(self):
        index_especs = 1                                                                                            # Indice das especificacoes das GLCs na lista de entrada
        index_variaveis = 2                                                                                         # Indice das variaveis das GLCs na lista de entrada
        index_terminais = 3                                                                                         # Indice dos terminais das GLCs na lista de entrada
        index_regras = 4                                                                                            # Indice das regras das GLCs na lista de entrada
        index_cadeias = 0                                                                                           # Indice da quantidade de cadeias correspondentes a primeira GLC

        qtd_glcs = int(self.gramaticas[0])                                                                          # Quantidade de GLCs

        for glc in range(qtd_glcs):
            qtd_variaveis, qtd_terminais, qtd_regras = map(int, self.gramaticas[index_especs].split())              # Especificacoes das GLCs
            
            variaveis = self.gramaticas[index_variaveis].split()                                                    # Variaveis das GLCs
            terminais = self.gramaticas[index_terminais].split()                                                    # Terminais das GLCs
            regras = self.gramaticas[index_regras:index_regras + qtd_regras]                                        # Regras das GLCs

            regras_de_substituicao = self.regras_to_dict(variaveis, regras)                                         # Conversao da lista de regras em um dicionario

            qtd_cadeias = int(self.cadeias[index_cadeias])                                                          # Quantidade de cadeias de teste

            print(f'\nglc {glc}')
            print(f'qtd variaveis: {qtd_variaveis}')
            print(f'qtd terminais: {qtd_terminais}')
            print(f'qtd regras: {qtd_regras}')
            print(f'\nvariaveis: {variaveis}')
            print(f'terminais: {terminais}')
            print(f'regras: {regras_de_substituicao}')
            #print(f'variavel inicial: {variavel_inicial}\n')

            """
            Leitura das cadeias de teste e execucao do algoritmo
            """

            while qtd_cadeias > 0:
                index_cadeias += 1                                                                                  # Atualizando indice
                qtd_cadeias -= 1                                                                                    # Atualizando quantidade de cadeias

                cadeia = self.cadeias[index_cadeias].split()                                                        # Lista contendo os simbolos da cadeia
                print(f'\ncadeia: {cadeia}')

                """
                Validando se o teste eh a cadeia vazia, alem de checar
                se a substituicao faz parte do conjunto de regras
                """

                if ('&' in cadeia) and (len(cadeia) == 1):
                    if (self.busca(regras=regras_de_substituicao, terminal='&')):
                        print('cadeia aceita')
                
                else:
                    tabela = self.criar_tabela(len(cadeia))                                                         # Tabela contendo os resultados do algoritmo

                    for i in range(len(cadeia)):
                        for variavel in variaveis:
                            if (self.busca(regras_de_substituicao, variavel, cadeia[i])):
                                tabela[i][i].append(variavel)

                    print(tabela)

            index_especs += qtd_regras + 3                                                                          # Atualizando indice
            index_variaveis += qtd_regras + 3                                                                       # Atualizando indice
            index_terminais += qtd_regras + 3                                                                       # Atualizando indice
            index_regras += qtd_regras + 3                                                                          # Atualizando indice
            index_cadeias += 1                                                                                      # Atualizando indice
            

# Testes
print(CYK().algoritmo_cyk())