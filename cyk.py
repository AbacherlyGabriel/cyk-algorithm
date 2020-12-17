"""
Gabriel Bispo Abacherly - 10284420
"""

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
        regras_de_substituicao = {variavel: [] for variavel in variaveis}                                           # Inicializando dicionario

        for regra in regras:
            regra_lista = regra.split()                                                                             # Split da string que contem a regra

            variavel = regra_lista[0]                                                                               # Definicao da variavel
            substituicoes = regra_lista[2:]                                                                         # Definicao da subtituicao
            
            regras_de_substituicao[variavel].append(substituicoes)                                                  # Adicionando regra ao dicionario

        variavel_inicial = list(regras_de_substituicao.keys())[0]                                                   # Obtendo a variavel inicial

        return regras_de_substituicao, variavel_inicial                                                             # Retorando dict e a variavel inicial

    """
    Inicializacao da tabela de resultados dado o tamanho da cadeia de teste
    """

    def criar_tabela(self, tam_cadeia):
        tabela = []                                                                                                 # Instanciando a tabela

        for i in range(tam_cadeia):
            tabela.append([])                                                                                       # Adicionando linhas

            for j in range(tam_cadeia):
                tabela[i].append([])                                                                                # Adicionando colunas

        return tabela                                                                                               # Retornando tabela inicializada

    """
    Busca por regras especificadas no parametro da funcao

    As buscas podem ser por regras de uma determinada variavel
    (se o parametro "variavel" nao for nulo) ou 
    por todas as substituicoes da GLC (se o parametro "variavel" for nulo)
    """

    def busca(self, regras=None, variavel=None, simbolo=None):
        if (regras is not None) and (simbolo is not None):                                                          # Validando o tipo de busca
            substituicoes = regras.values()                                                                         # Obtendo a lista de regras
            
            if (variavel is not None):
                substituicoes = regras[variavel]                                                                    # Obtendo a lista de regras dada uma variavel

            for lista_substituicoes in substituicoes:                                                               # Busca pelo simbolo especificado nos parametros da funcao
                for substituicao in lista_substituicoes:
                    if simbolo in substituicao:
                        return True                                                                                 # Retornnando True, se o simbolo foi encontrado

        return False                                                                                                # Retornando False, caso contrario
        
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

        resultados = {glc: [] for glc in range(qtd_glcs)}                                                           # Dict responsavel por armazenar os resultados do algoritmo

        for glc in range(qtd_glcs):
            qtd_variaveis, qtd_terminais, qtd_regras = map(int, self.gramaticas[index_especs].split())              # Especificacoes das GLCs
            
            variaveis = self.gramaticas[index_variaveis].split()                                                    # Variaveis das GLCs
            terminais = self.gramaticas[index_terminais].split()                                                    # Terminais das GLCs
            regras = self.gramaticas[index_regras:index_regras + qtd_regras]                                        # Regras das GLCs

            regras_de_substituicao, variavel_inicial = self.regras_to_dict(variaveis, regras)                       # Conversao da lista de regras em um dicionario

            qtd_cadeias = int(self.cadeias[index_cadeias])                                                          # Quantidade de cadeias de teste

            """
            Leitura das cadeias de teste e execucao do algoritmo
            """

            while qtd_cadeias > 0:
                index_cadeias += 1                                                                                  # Atualizando indice
                qtd_cadeias -= 1                                                                                    # Atualizando quantidade de cadeias

                cadeia = self.cadeias[index_cadeias].split()                                                        # Lista contendo os simbolos da cadeia
                tam_cadeia = len(cadeia)                                                                            # Armazendo o tamanho da cadeia

                """
                Validando se o teste eh a cadeia vazia, alem de checar
                se a substituicao faz parte do conjunto de regras
                """

                if ('&' in cadeia) and (tam_cadeia == 1):
                    if (self.busca(regras=regras_de_substituicao, simbolo='&')):                                    # Busca por regras contendo a cadeia vazia
                        resultados[glc].append(1)                                                                   # Cadeia aceita
                    else:
                        resultados[glc].append(0)                                                                   # Cadeia rejeitada

                else:
                    tabela = self.criar_tabela(tam_cadeia)                                                          # Tabela contendo os resultados do algoritmo

                    """
                    Analisando subcadeias de tamanho 1:

                    Busca, para cada variavel, por regras do tipo A => b,
                    onde b eh uma subcadeia de tamanho 1

                    Se a regra for encontrada, adiciona-se A em tabela(i, i)  
                    """

                    for i in range(tam_cadeia):
                        for variavel in variaveis:
                            if (self.busca(regras_de_substituicao, variavel, cadeia[i])):
                                tabela[i][i].append(variavel)

                    """
                    Analisando subcadeias dos demais tamanhos
                    """

                    for tam_substring in range(2, tam_cadeia + 1):                                                  # Definicao do tamanho da subcadeia                                                                            
                        for start in range(tam_cadeia - tam_substring + 1):                                         # Definicao da posicao inicial da subcadeia
                            end = start + tam_substring - 1                                                         # Definicao da posicao final da subcadeia

                            for split in range(end):                                                                # Posicao de quebra da subcadeia
                                
                                """
                                Para cada variavel, busca-se por regras do tipo A => BC

                                Ao encontra-las, verifica-se se tabela(start, split) contem B e
                                se tabela(split + 1, end) possui C.

                                Em casos positivos, A eh adicionada a tabela(start, end)
                                """

                                for variavel in variaveis:
                                    for regra in regras_de_substituicao[variavel]:
                                        for terminal in terminais:
                                            if terminal not in regra:
                                                if len(regra) == 2:
                                                    if (regra[0] in tabela[start][split]) and (regra[1] in tabela[split + 1][end]):
                                                        tabela[start][end].append(variavel)

                                                    break

                    """
                    Validando se, apos a construcao da tabela, a variavel inicial
                    encontra-se em tabela(1, n), onde n representa o tamanho da cadeia de teste
                    """

                    if variavel_inicial in tabela[0][tam_cadeia - 1]:
                        resultados[glc].append(1)                                                                   # Cadeia aceita
                    else:
                        resultados[glc].append(0)                                                                   # Cadeia rejeitada

            index_especs += qtd_regras + 3                                                                          # Atualizando indice
            index_variaveis += qtd_regras + 3                                                                       # Atualizando indice
            index_terminais += qtd_regras + 3                                                                       # Atualizando indice
            index_regras += qtd_regras + 3                                                                          # Atualizando indice
            index_cadeias += 1                                                                                      # Atualizando indice
            
        return resultados                                                                                           # Retornando resultados
