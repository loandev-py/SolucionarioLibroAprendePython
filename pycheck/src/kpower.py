# *********************************
# COMPROBANDO IGUALDAD DE POTENCIAS
# *********************************


def run(n: int) -> tuple:
    # TU CÓDIGO AQUÍ
    left_side = (n * (n + 1) / 2) ** 2

    right_side = (n * (n + 1) / 2) ** 2

    return left_side, right_side


if __name__ == '__main__':
    run(1)