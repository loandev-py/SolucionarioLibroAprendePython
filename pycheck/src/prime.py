# **************
# NÚMEROS PRIMOS
# **************


def run(n: int) -> bool:
    # TU CÓDIGO AQUÍ
    isprime = True
    for i in range(2, n):
        if n % i == 0:
            isprime = False
            break

    return isprime


if __name__ == '__main__':
    run(2)