# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************


def run(matrix: list) -> int:
    # TU CÓDIGO AQUÍ
    n =  len(matrix)
    if not all(len(row) == n for row in matrix):
        return None
    total = 0
    for i in range(n):
        total += matrix[i][i]

    return total

if __name__ == '__main__':
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])