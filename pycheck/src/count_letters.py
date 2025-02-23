# ***************
# CONTANDO LETRAS
# ***************


def run(sentence: str) -> dict:
    # Creamos un diccionario vacio para los conteos
    counter = {}

    # Iteramos sobre cada caracter en la misma cadena
    for caracter in sentence:
        # Ignoramos espacios y caracteres no alfabeticos
        if caracter.isalpha():
            # Convertimos el caracter a nimusculas para tener un unico registro
            caracter_min = caracter.lower()
            # Incrementamos el contador en el dicionario
            counter[caracter_min] = counter.get(caracter_min, 0) + 1
            
    return counter


if __name__ == '__main__':
    run('boom')