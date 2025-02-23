# ********************
# DESCUBRIENDO IMPARES
# ********************


def run(values: list) -> list:
    # TU CÓDIGO AQUÍ
    
    return list(dict.fromkeys([x for x in values if x % 2 != 0]))


if __name__ == '__main__':
    run([1, 2, 3, 4, 5])