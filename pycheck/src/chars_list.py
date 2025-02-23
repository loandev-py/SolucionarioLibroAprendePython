# **********************
# DESPLEGANDO CARACTERES
# **********************


def run(texts: list) -> list:
    # TU CÓDIGO AQUÍ
   cadena_unida = ''.join(texts)
   lista_caracteres = list(cadena_unida)
   return lista_caracteres

if __name__ == '__main__':
    run(['uno', 'dos', 'tres'])     