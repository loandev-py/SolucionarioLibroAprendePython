# *****************
# ORDENANDO NÚMEROS
# *****************


def run(numbers: list) -> list:
    # TU CÓDIGO AQUÍ
    sorted_numbers = numbers.copy()

    n = len(sorted_numbers)

    for i in range(n - 1):
        min_idx = i

        for j in range(i +1, n):
            if sorted_numbers[j] < sorted_numbers[min_idx]:
                min_idx = j
        
        sorted_numbers[i], sorted_numbers[min_idx] = sorted_numbers[min_idx], sorted_numbers[i]

    return sorted_numbers


if __name__ == '__main__':
    run([4, 2, 9, 7, 1, 8])