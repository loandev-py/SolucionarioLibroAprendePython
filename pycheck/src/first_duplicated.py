# *************************
# PRIMER ELEMENTO DUPLICADO
# *************************


def run(numbers: list) -> int:
    # TU CÓDIGO AQUÍ
    fdup = set()

    for num in numbers:
        if num in fdup:
            return num
        fdup.add(num)

    return -1


if __name__ == '__main__':
    run([2, 3, 5, 3, 2])