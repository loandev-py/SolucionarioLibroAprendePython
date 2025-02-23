# ***************************
# CALCULANDO POTENCIAS A MANO
# ***************************


def run(x: int, n: int) -> int:
    # TU CÓDIGO AQUÍ
    p = 1
    for _ in range(n):
        p *= x 
    return p


if __name__ == '__main__':
    run(3, 4)