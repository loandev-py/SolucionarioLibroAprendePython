# ***************
# PRECIO SIN IGIC
# ***************


def run(price_with_igic: float, igic: float) -> float:
    # TU CÓDIGO AQUÍ
    clean_price = price_with_igic - (price_with_igic*(igic/100))

    return clean_price


if __name__ == '__main__':
    run(120, 7)