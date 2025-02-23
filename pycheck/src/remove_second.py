# *************************
# NO ME INTERESAN LOS PARES
# *************************


def run(items: list) -> list:
    return [element for i, element in enumerate(items) if i %2 ==0]


if __name__ == '__main__':
    run([1, 2, 1, 2, 1, 2])