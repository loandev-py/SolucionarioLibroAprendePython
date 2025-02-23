# **************
# EL LOBO ACECHA
# **************


def run(farm: list) -> str:
    # TU CÓDIGO AQUÍ
    lobo_index = len(farm) - farm.index('lobo')

    if lobo_index ==1:
        return 'No te quiero ver más por aquí, lobo'
    
    return f'Cuidado oveja {lobo_index - 1}, el lobo te va a comer'


if __name__ == '__main__':
    run(['oveja', 'oveja', 'lobo', 'oveja'])