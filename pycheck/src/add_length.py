# *********************
# PALABRAS CON LONGITUD
# *********************


def run(text: str) -> list:
    # TU CÓDIGO AQUÍ
    # Dividir el texto en palabras
    words = text.split()
    
    # Procesar cada palabra y crear el resultado formateado
    result_words = ""
    for word in words:
        result_words += f"{word:<15} {len(word)}"
    
    return result_words.strip()



if __name__ == '__main__':
    run('todo se transforma')