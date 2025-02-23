# ******************
# TODO EN ALFABÉTICO
# ******************


def run(text: str) -> bool:
    # TU CÓDIGO AQUÍ
    ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'

    for char in text.lower():
        if char not in ALPHABET:
            return False

    return True

if __name__ == '__main__':
    run('hello-world')