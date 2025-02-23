# *****************************
# RELLENANDO VALORES PENDIENTES
# *****************************


def run(numbers: list) -> list:
    # TU CÓDIGO AQUÍ
    fnumbers = {}

    for num in numbers:
        if num in fnumbers:
            fnumbers[num] += 1
        else:
          fnumbers[num] = 1

    valors_missings = []
    for num, counts in fnumbers.items():
        if counts > 1:
            valors_missings.extend([num] * (counts - 1))

    return valors_missings


if __name__ == '__main__':
    run([0, 1, 3, 5]) 