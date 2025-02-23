# *******************
# NO ERES CONSECUTIVO
# *******************


def run(values: list) -> int:
    # TU CÓDIGO AQUÍ
    for i in range(len(values)):
        if values[i] != i + values[0]:
            return values[i]
    return None
            


if __name__ == '__main__':
    run([1, 2, 3, 4, 6, 7, 8])