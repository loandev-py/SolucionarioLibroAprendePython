# ************************
# DÍGITOS EN ORDEN INVERSO
# ************************

def run(number: int) -> list:
    # TU CÓDIGO AQUÍ
    chain = str(number)[::-1]

    return [int(d) for d in chain]


if __name__ == '__main__':
    run(35231)