# *********************
# VOLUMEN DE UNA ESFERA
# *********************


def run(radius: float) -> float:
    # TU CÓDIGO AQUÍ
    volume = (radius**3)*(3.14)*(4/3)

    return volume


if __name__ == '__main__':
    run(5)