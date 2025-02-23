# *********************
# ENCONTRANDO ISOGRAMAS
# *********************


def run(text: str) -> bool:
    # TU CÓDIGO AQUÍ
    cleaned_string = ''.join(c for c in text if c != '-')   #verifica que el texto contenga o no -

    lower_string = cleaned_string.lower()

    unique_chars = set(lower_string)
    return len(lower_string) == len(unique_chars)


if __name__ == '__main__':
    run('lumberjacks')