# ************************************
# FORMATEANDO A COLORES EN HEXADECIMAL
# ************************************


def run(intcolor: int) -> str:
    # TU CÓDIGO AQUÍ
    hexcolor = format(intcolor, '06X')

    return hexcolor


if __name__ == '__main__':
    run(45782)