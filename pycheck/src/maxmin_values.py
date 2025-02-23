# *********************
# VALOR MÁXIMO Y MÍNIMO
# *********************


def run(values: list) -> tuple:
    # TU CÓDIGO AQUÍ
    maxi = mini = values[0]

    for i in range(1, len(values)):
        if values[i] > maxi:
            maxi = values[i]
        elif values[i] < mini:
            mini = values[i]
    
    return maxi, mini

if __name__ == '__main__':
    run([4, 6, 2, 1, 9, 63, -134, 566])