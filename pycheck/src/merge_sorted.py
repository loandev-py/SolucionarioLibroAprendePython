# ***************
# MEZCLA ORDENADA
# ***************


def run(values1: list, values2: list) -> list:
    # TU CÓDIGO AQUÍ
    combined = values1 + values2

    not_dupli = list(dict.fromkeys(combined))

    result = []

    for num in not_dupli:
        inserte = False
        for i in range(len(result)):
            if num < result[i]:
                result.insert(i, num)
                inserte = True
                break
        if not inserte:
            result.append(num)
    return result

if __name__ == '__main__':
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])