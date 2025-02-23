# ***************************************
# PRODUCTO CARTESIANO EN CADENAS DE TEXTO
# ***************************************


def run(text1: str, text2: str) -> str:
    # TU CÓDIGO AQUÍ
    result = ''
    for letter1 in text1:
        for letter2 in text2:
            result += letter1 + letter2
    return result


if __name__ == '__main__':
    run('xy', '$#')