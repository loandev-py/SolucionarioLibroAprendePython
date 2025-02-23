# *****************
# MENOR ID SIN USAR
# *****************


def run(ids: list) -> int:
    # TU CÓDIGO AQUÍ
  if not ids:
     return 1

  ids_set = set(ids)
  id_actual = 1
  while id_actual in ids_set:
     id_actual += 1

  return id_actual


if __name__ == '__main__':
    run([3, 1, 8, 4, 9])