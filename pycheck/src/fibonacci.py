# *********
# FIBONACCI
# *********


def run(n: int) -> float:
    # TU CÓDIGO AQUÍ
    if n <= 1:
        return n
    else: return run(n - 1) + run(n-2)


if __name__ == '__main__':
    run(1)