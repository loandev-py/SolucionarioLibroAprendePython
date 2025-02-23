# ************
# VALOR MÁXIMO
# ************


def run(values: list) -> int:
    # TU CÓDIGO AQUÍ
    

    return -max(-x for x in values)


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])