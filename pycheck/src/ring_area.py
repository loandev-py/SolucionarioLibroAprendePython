# ***************
# ÁREA DEL ANILLO
# ***************


def run(z: float) -> float:
    # TU CÓDIGO AQUÍ
    white_area = (3.14*(((3*z)/2)**2))-(3.14*((z/2)**2))

    return round(white_area,2)


if __name__ == '__main__':
    run(6)