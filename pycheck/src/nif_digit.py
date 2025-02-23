# *************************
# DÍGITO DE CONTROL DEL NIF
# *************************


def run(nif: str) -> str:
    # TU CÓDIGO AQUÍ
    xnif = int(nif)
    znif = xnif%23
    wnif = 'TRWAGMYFPDXBNJZSQVHLCKE'[znif]

    return nif+wnif


if __name__ == '__main__':
    run('78654355')