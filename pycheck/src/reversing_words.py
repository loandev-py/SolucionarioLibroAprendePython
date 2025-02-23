# *************************
# PALABRAS EN ORDEN INVERSO
# *************************


def run(text: str) -> str:
    # TU CÓDIGO AQUÍ
    text_inv = list(reversed(text.split()))
    text_min = [palabra.lower() for palabra in text_inv]
    result = ' '.join(text_min)

    return result

if __name__ == '__main__':
    run('Hello World')