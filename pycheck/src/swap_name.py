# ****************
# NOMBRE VICEVERSA
# ****************


def run(fullname: str) -> str:
    # TU CÓDIGO AQUÍ
    name, *last_name = fullname.split(" ")
    swapname = " ".join(last_name) + " " + name

    return swapname


if __name__ == '__main__':
    run('John McClane')