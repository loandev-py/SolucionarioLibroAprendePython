# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************


def run(items: list) -> list:
    # TU CÓDIGO AQUÍ
    result = []
    visto = set()

    for elemento in items:
        if elemento not in visto:
            result.append(elemento)
            visto.add(elemento)

    return result


if __name__ == '__main__':
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])