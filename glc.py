"""
Gabriel Bispo Abacherly - 10284420
"""

from cyk import CYK


"""
Funcao responsavel por realizar a formatacao dos resultados do algoritmo
"""

def main():
    resultados = CYK().algoritmo_cyk()

    with open('out-status.txt', 'w') as writer:
        for resultado in resultados.values():
            for i in range(len(resultado)):
                writer.write(str(resultado[i]))

                if (i != len(resultado) - 1):
                    writer.write(' ')

            writer.write('\n')


if __name__ == "__main__":
    main()