# *****************
# DISTANCIA HAMMING
# *****************


def run(text1: str, text2: str) -> int:
    # TU CÓDIGO AQUÍ
    if len(text1) != len(text2):
        return -1
    
    distancia = sum(c1!= c2 for c1, c2 in zip(text1, text2))

    return distancia


if __name__ == '__main__':
    run('0001010011101', '0000110010001')