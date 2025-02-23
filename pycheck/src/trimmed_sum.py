# **************
# SUMA RECORTADA
# **************


def run(values: list) -> int:
    # TU CÓDIGO AQUÍ
  if not values:
     return 0
  
  maxi = max(values)
  mini = min(values)

  if maxi == mini:
     return 0

  values_copy = values.copy()

  cont_max = values_copy.count(maxi)
  cont_min = values_copy.count(mini)

  for _ in range(cont_max):
     values_copy.remove(maxi)

  for _ in range(cont_min):
     values_copy.remove(mini)

  if not values_copy:
     return 0
  
  return sum(values_copy)


if __name__ == '__main__':
    run([6, 2, 1, 8, 10])