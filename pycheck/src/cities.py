# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict:
    # Dividir la cadena por punto y coma
    cities = cinfo.split(';')

    # Crear un diccionario vacio para almacenar los resultados
    result = {}

    # Procesar cada cuidad y su poblacion
    for citie in cities:
        # Ignorar cualquier ciudad sin poblacion
        if ':' in citie:
            citie, population = citie.split(':')

        # Converir la poblaco¿ion en entero
        try:
            population = int(population)
        except ValueError:
            print(f"Error: No se pudo convertir '{population}' a entero para la ciudad '{citie}'.")
        # Agregar la cuidad y su poblacion al diccionario
        result [citie] = population    

    return result


if __name__ == '__main__':
    run('Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000')