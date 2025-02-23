# ******************
# POBLACIÓN PROMEDIO
# ******************


def run(pdata: dict) -> dict:
    # Calcular el total de poblacion
    total_population = sum(pdata.values())

    # Xalcular los porcentajes de poblacion relativa
    percentage_population = {city: round((population / total_population) * 100, 3) for city, population in pdata.items()}

    # Calcular la media de poblacion
    population_average = round(total_population / len(pdata), 3)

    # Combinar los resultados en un diccionario
    avg_data = {percentage_population, population_average}

    return avg_data


if __name__ == '__main__':
    run({'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000})