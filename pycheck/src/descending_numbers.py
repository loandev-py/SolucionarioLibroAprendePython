# ****************
# CONTEO REGRESIVO
# ****************


def run(n: int) -> list:
    # TU CÓDIGO AQUÍ
    result = []
    for i in range(n, 0, -1):
        result.append(i)
    return result


if __name__ == '__main__':
    run(5)