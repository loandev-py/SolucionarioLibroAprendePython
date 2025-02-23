# ****************
# CONTANDO VOCALES
# ****************


def run(text: str) -> int:
    # TU CÓDIGO AQUÍ
    num_vowels = 0
    for texts in text:
        if texts.lower() in 'aeiouáéíóúü':
            num_vowels += 1

    return num_vowels


if __name__ == '__main__':
    run('El camión chocó contra el árbol')