# ********************
# REORGANIZANDO FECHAS
# ********************


def run(input_date: str, base_year: int) -> str:
    # TU CÓDIGO AQUÍ
    parts = input_date.split('/')
    if len(parts) != 2:
        raise ValueError("la entrada debe tener el formato /<dia>/<año-con-dos-cifras>")
    day = int (parts[0])
    year_2figures = int(parts[1])

    if year_2figures <- base_year:
        year_4figures = str(base_year + year_2figures)
    else: year_4figures = str(base_year - (10000 - year_2figures))

    output_date = f'{day}-{year_4figures}'

    return output_date


if __name__ == '__main__':
    run('12/31/23', 2000)