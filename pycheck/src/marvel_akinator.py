# *******************************
# ADIVINANDO PERSONAJES DE MARVEL
# *******************************


def run(can_fly: bool, is_human: bool, has_mask: bool) -> str:
    # TU CÓDIGO AQUÍ
    if can_fly == True:
        if is_human == True:
            if has_mask == True:
                character = 'Ironman'
            else:
                character = 'Captain Marvel'
        elif is_human == False:
            if has_mask == True:
                character = 'Ronan Accuser'
            else:
                character = 'Vision'
    elif can_fly == False:
        if is_human == True:
            if has_mask == True:
                character = 'Spiderman'
            else:
                character = 'Hulk'
        elif is_human == False:
            if has_mask == True:
                character = 'Black Bolt'
            else:
                character = 'Thanos'

    return character


if __name__ == '__main__':
    run(True, True, True)