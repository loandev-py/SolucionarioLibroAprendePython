# ******************
# CALCULADORA LÓGICA
# ******************


def run(values: list, oper: str) -> bool:
    # TU CÓDIGO AQUÍ
    def apply_and_or(a, b):
        return a and b if oper == 'and' else a or b
    
    if len(values) <= 1:
        return values[0] if values else False
    
    result = apply_and_or(values[0], values[1])

    for i in range(2, len(values)):
        result = apply_and_or(result, values[i])

    return result


if __name__ == '__main__':
    run([True, True, False], 'and')