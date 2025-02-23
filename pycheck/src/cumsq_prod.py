# *******************************
# PRODUCTO ACUMULADO EN CUADRADOS
# *******************************


def run(n: int) -> int:
    # TU CÓDIGO AQUÍ
    result = 1
    for i in range(1, n+1):
        result *= i ** 2

    return result


if __name__ == '__main__':
    run(1)