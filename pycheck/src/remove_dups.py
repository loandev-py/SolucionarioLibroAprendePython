# *********************
# ELIMINANDO DUPLICADOS
# *********************


def run(nums_dups: list) -> list:
    # TU CÓDIGO AQUÍ
    #convertimos la lista a un conjunto para eliminar duplicados
    unique_set = set(nums_dups)

    # convertimos el conjunto nuevamente a una lista y la ordenamos segun la original
    return sorted(unique_set, key=nums_dups.index)


if __name__ == '__main__':
    run([2, 3, 2, 2, 1, 5, 4, 2, 4, 9])