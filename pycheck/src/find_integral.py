# *********************
# ENCUENTRA LA INTEGRAL
# *********************


def run(symbol: str) -> str:
    # TU CÓDIGO AQUÍ
    coma = symbol.find(',')
    coef = int(symbol[:coma])
    exp = int(symbol[coma+1:])
    red = int((coef/(exp + 1)))
    integral = str(red) + 'x^' + str(exp+1)

    return integral


if __name__ == '__main__':
    run('3,2')