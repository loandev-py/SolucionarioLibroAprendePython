# ********************
# MÁXIMO COMÚN DIVISOR
# ********************


def run(a: int, b: int) -> int:
    # TU CÓDIGO AQUÍ
    while b!=0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    run(1, 1)