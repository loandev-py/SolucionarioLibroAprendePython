# *************************
# QUITANDO PRIMERO Y ÚLTIMO
# *************************


def run(text: str) -> str:
    # TU CÓDIGO AQUÍ
    stext = text[1:] 
    stext = stext[:-1]

    return stext


if __name__ == '__main__':
    run('What can I do')