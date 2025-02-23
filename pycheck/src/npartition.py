# ***********************
# PARTICIÓN POR EL NÚMERO
# ***********************


def run(values: list, ref_value: int) -> list:
    # TU CÓDIGO AQUÍ
  less_than_reference = []
  greater_than_or_equal_to_reference = []

  for num in values:
    if num < ref_value:
        less_than_reference.append(num)
    elif num >= ref_value:
        greater_than_or_equal_to_reference.append(num)

  return [less_than_reference, greater_than_or_equal_to_reference]

if __name__ == '__main__':
    run([4, 3, 2, 9, 8, 5], 4)