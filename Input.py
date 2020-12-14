"""
"""

class FileReader:

    """
    Leitura dos arquivos de entrada
    """

    def __init__(self):
        with open('./files/inp-glc.txt', 'r') as reader:
            self.__glcs = reader.readlines()

        with open('./files/inp-cadeias.txt', 'r') as reader:
            self.__cadeias = reader.readlines()
