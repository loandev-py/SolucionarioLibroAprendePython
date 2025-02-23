# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    # TU CÓDIGO AQUÍ
    winner = points[0]

    for char in points:
        if char != winner:
            winner = char
    
    return winner

if __name__ == '__main__':
    run('ABAABA')