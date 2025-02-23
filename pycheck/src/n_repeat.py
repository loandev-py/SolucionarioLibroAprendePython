# *************
# SUMA REPETIDA
# *************


def run(n: int) -> int:
    # TU CÓDIGO AQUÍ
    
    if n >= 0 and n <= 10:
        result = n + ((n * 10) + n) + (((n * 100)+(n*10)+n))
   
    return result


if __name__ == '__main__':
    run(3)