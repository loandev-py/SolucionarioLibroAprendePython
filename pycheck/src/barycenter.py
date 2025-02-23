# **************************
# BARICENTRO DE UN TRIÁNGULO
# **************************


def run(A: list, B: list, C: list) -> tuple:
    # TU CÓDIGO AQUÍ
    bari_x = round((A[0] + B[0] + C[0]) / 3, 4)
    bary_y = round((A[1] + B[1] + C[1]) / 3,4)

    return bari_x, bary_y

if __name__ == '__main__':
    run([4, 6], [12, 4], [10, 10])