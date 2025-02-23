# ************************
# MULTIPLICACIÓN EN CADENA
# ************************


def run(numbers: list) -> int:
  product = 1
  for number in numbers:
     product *= number

  return product

if __name__ == '__main__':
    run([1, 2, 3, 4])