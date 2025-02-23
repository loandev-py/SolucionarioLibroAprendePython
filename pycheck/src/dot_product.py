# ****************
# PRODUCTO ESCALAR
# ****************


def run(vector1: list, vector2: list) -> float:
    # TU CÓDIGO AQUÍ
    if len(vector1) != len(vector2): 
        return None
                           
    dprod = 0
    for x, y in zip(vector1, vector2):
        dprod += x*y
    return dprod


if __name__ == '__main__':
    run([4, 3, 8, 1], [9, 2, 7, 3]) 