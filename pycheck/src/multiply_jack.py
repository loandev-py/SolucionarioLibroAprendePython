# *************************
# LA MULTIPLICACIÓN DE JACK
# *************************


def run(n: int) -> int:
    # TU CÓDIGO AQUÍ
    result = n * pow(5 , len(str(abs(n))))

    return result


if __name__ == '__main__':
    run(3)