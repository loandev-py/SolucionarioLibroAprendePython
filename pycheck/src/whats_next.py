# *********************
# ¿QUÉ ES LO SIGUIENTE?
# *********************


def run(items: list, ref_item: object) -> object:
    # TU CÓDIGO AQUÍ
   try:
       indice = items.index(ref_item)

       return items[indice + 1] if indice + 1 < len(items) else None
   
   except ValueError:
       return None


if __name__ == '__main__':
    run([1, 2, 3, 4, 5, 6, 7], 3)