# **********************
# INICIALES DE UN NOMBRE
# **********************


def run(fullname: str) -> str:
    # TU CÓDIGO AQUÍ
    parts = fullname.split(',')

    lastnames = parts[0].strip()
    name = parts[-1].strip()

    initials = []
    for name_element in name.split():
        initials.append(name_element[0].upper())

    for lastname in lastnames.split():
        initials.append(lastname[0].upper())

    return '.'.join(initials) + '.'


if __name__ == '__main__':
    run('Delgado Quintero, sergio')