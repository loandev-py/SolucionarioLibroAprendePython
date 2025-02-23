# ********************
# CUBOIDES Y VOLÚMENES
# ********************


def run(cuboid1: list, cuboid2: list) -> float:
    # TU CÓDIGO AQUÍ
    volumen1 = cuboid1[0] * cuboid1[1] * cuboid1[2]
    volumen2 = cuboid2[0] * cuboid2[1] * cuboid2[2]
    
    vol_diff = abs(volumen1 - volumen2)

    return vol_diff


if __name__ == '__main__':
    run([2, 2, 3], [5, 4, 1])