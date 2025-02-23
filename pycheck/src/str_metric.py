# ********************************
# UNA MÉTRICA PARA CADENA DE TEXTO
# ********************************


def run(text: str) -> int:
    # TU CÓDIGO AQUÍ
    t_text = len(text)
    voc = sum(1 for char in text if char.lower() in 'aeiou')
    metric = t_text * voc

    return metric


if __name__ == '__main__':
    run('ordenador')