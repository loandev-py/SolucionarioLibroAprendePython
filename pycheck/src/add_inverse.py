# **************
# SUMA INVERTIDA
# **************


def run(numbers: list) -> int:
    # TU CÓDIGO AQUÍ
    add_inv = 0
    add_inv_neg = 0
    add_inv_pos = 0 
    for x in numbers:
        if x < 0:
            add_inv_neg += x
        elif x > 0:
            add_inv_pos -= x
    add_inv = add_inv_pos - add_inv_neg

    return add_inv


if __name__ == '__main__':
    run([1, 2, 3, 4, 5])