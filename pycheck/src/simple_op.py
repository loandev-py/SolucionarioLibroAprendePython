# ********************************
# RESOLVIENDO UNA OPERACIÓN SIMPLE
# ********************************


def run(num1: int, num2: int, op: str) -> float:
    # TU CÓDIGO AQUÍ
    match op:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 / num2
        case '&':
            if num1 == 0 and num2 == 0:
                return None
            elif num1 == 0:
                return num2
            elif num2 == 0:
                return num1
            else:
                result = num1 & num2
        
    return result


if __name__ == '__main__':
    run(5, 2, '+')