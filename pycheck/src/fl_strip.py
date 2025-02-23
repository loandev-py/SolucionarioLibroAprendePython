# ****************
# TROCEADO EXTREMO
# ****************


def run(numbers: str) -> str:
    # TU CÓDIGO AQUÍ
    num = numbers.split(',')
    num = num[1:-1]
    
    strip_numbers = ' '.join(num)

    return strip_numbers


if __name__ == '__main__':
    run('1,2,3')