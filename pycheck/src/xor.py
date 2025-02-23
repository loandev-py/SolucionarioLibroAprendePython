# ***
# XOR
# ***


def run(v1: bool, v2: bool) -> bool:
    # TU CÓDIGO AQUÍ
    xor = v1 and v2 and not v1

    return xor


if __name__ == '__main__':
    run(False, False)