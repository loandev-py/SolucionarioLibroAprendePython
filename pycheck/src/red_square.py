# ****************
# EL CUADRADO ROJO
# ****************


def run(arc_A: float) -> float:
    # TU CÓDIGO AQUÍ
    r=arc_A/(3.14/2)
    area = r*r

    return round(area,10)


if __name__ == '__main__':
    run(1)