# ***********************
# SUBCONJUNTOS EN CASCADA
# ***********************


def run(values: list, size: int) -> list:
    # TU CÓDIGO AQUÍ
    cascading = []

    def generar_subcon(indice):
        if indice == len(values) - size + 1:
            return
        
        subconjunto = values[indice:indice +  size]
        cascading.append(subconjunto)
        generar_subcon(indice + 1)
    generar_subcon(0)
    return cascading


if __name__ == '__main__':
    run([1, 2, 3, 4], 3)