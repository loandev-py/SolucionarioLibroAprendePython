# ****************************************
# ENCONTRANDO EL PRIMER Y EL ÚLTIMO DÍGITO
# ****************************************


def run(text: str) -> tuple:
    # TU CÓDIGO AQUÍ
    digit = [caracter for caracter in list(text) if caracter.isdigit()]
    first_digit = int(digit[0])
    last_digit = int(digit[-1])

    return first_digit, last_digit


if __name__ == '__main__':
    run('1abc2')