"""
Gabriel Bispo Abacherly - 10284420

Classe responsável pela leitura dos arquivos de entrada:
Definicao das GLCs e das cadeias de teste
"""

class FileReader:

    """
    Leitura dos arquivos de entrada
    """

    def __init__(self):
        with open('inp-glc.txt', 'r') as reader:
            self.__glcs = reader.readlines()

        with open('inp-cadeias.txt', 'r') as reader:
            self.__cadeias = reader.readlines()

    """
    Acessando lista com as especificacoes das GLCs
    """

    @property
    def glcs(self):
        return self.__glcs

    """
    Acessando lista com as especificacoes das cadeias de teste
    """

    @property
    def cadeias(self):
        return self.__cadeias
