# ************
# VALOR MÍNIMO
# ************


def run(values: list) -> int:
    # TU CÓDIGO AQUÍ
    min_value = values[0]
    for item in values[1:]:
        if item < min_value:
            min_value = item
            
    return min_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])