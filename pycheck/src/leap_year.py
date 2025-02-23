# **************
# AÑOS BISIESTOS
# **************


def run(year: int) -> bool:
    # TU CÓDIGO AQUÍ
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 

    return is_leap_year


if __name__ == '__main__':
    run(1900)