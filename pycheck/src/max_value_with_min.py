# ************
# VALOR MÁXIMO
# ************


def run(values: list) -> int:
    # TU CÓDIGO AQUÍ
    max_value = values[0]
    for num in values[1:]:
        if num > max_value:
            max_value = num

    return max_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])