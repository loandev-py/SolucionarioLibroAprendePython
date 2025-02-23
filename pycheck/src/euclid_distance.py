# ******************
# DISTANCIA EUCLÍDEA
# ******************
import math

def run(x1: float, y1: float, x2: float, y2: float) -> float:
    # TU CÓDIGO AQUÍ
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return distance


if __name__ == '__main__':
    run(3, 5, -7, -4)