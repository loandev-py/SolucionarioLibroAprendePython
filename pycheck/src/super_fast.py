# **********************
# ANIMALES SUPER RÁPIDOS
# **********************


def run(speed_km_h: float) -> float:
    # TU CÓDIGO AQUÍ
    speed_cm_s = speed_km_h*(1000/36)

    return int(speed_cm_s)


if __name__ == '__main__':
    run(1.08)