# ***************
# APLANA LA LISTA
# ***************


def run(elements: list) -> list:
    # TU CÓDIGO AQUÍ
    flat_list = []  #lista vacia para almacenar los elementos desanidados
    for element in elements:
        if isinstance(element, list):   # verificamis si el elemento es una lista
            flat_list.extend(run(element))  # recursivamente aplanaoms la sublista
        else:
            flat_list.append(element)   # agregamos el elemento simple a la lista final

    return flat_list        

if __name__ == '__main__':
    run([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])