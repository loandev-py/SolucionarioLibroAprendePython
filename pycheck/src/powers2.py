# **************
# POTENCIAS DE 2
# **************


def run(num_powers: int) -> list:
    # TU CÓDIGO AQUÍ
    resultado = []
    for i in range (num_powers + 1):
        resultado.append(2 ** i)

    return resultado

if __name__ == '__main__':
    run(0)