# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    # TU CÓDIGO AQUÍ
    return len(set(items))==1


if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])