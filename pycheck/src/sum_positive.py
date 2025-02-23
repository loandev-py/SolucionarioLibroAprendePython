# **********************
# SUMANDO SOLO POSITIVOS
# **********************


def run(numbers: list) -> int:
    # TU CÓDIGO AQUÍ
    suma = 0
    for i in numbers:
        if i > 0:
            suma += i
    return suma 
    
if __name__ == '__main__':
    run([1, -4, 7, 12])