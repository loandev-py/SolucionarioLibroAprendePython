# ****************
# SUMA HETEROGÉNEA
# ****************


def run(items: list) -> int:
    
    #convertir la cadena a numeros enteros
    list_convert = [int(item) for item in items]

    # sumar todos los elementos de las lista convertida
    total_sum = sum(list_convert)

    return total_sum


if __name__ == '__main__':
    run([1, '2', 3, '4', 5])