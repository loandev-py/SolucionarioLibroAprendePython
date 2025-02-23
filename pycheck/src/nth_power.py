# *************
# N ELEVADO A N
# *************


def run(values: list, power: int) -> int:
    # verificar si la lista esta vacia o N es cero
    if not values or power == 0:
        return -1
    
    # verificar si N esta dentro del grango de la lista
    if power < len(values):
        # calcular y retornar el resultado
        return values[power] **  power
    else:
        # retorna -1 si esta fuera del rango
        return -1


if __name__ == '__main__':
    run([1, 2, 3, 4], 2)