# *****************
# COMBINANDO TECLAS
# *****************


def run(key1: str, key2: str, key3: str) -> str:
    # TU CÓDIGO AQUÍ
    if key1 == 'CTRL' and key2 == 'ALT':
            match key3:
                case 'T':
                    return 'Open terminal'
                case 'L':
                    return 'Lock screen'
                case 'D':
                    return 'Show desktop'
                case 'DEL':
                    return 'Log out'
    elif key1 == 'CTRL' and  key2 == 'Q':
            if key3 == '': return 'Close window'
    elif key1 == 'ALT' and key2 == 'F2':
        if key3 =='': return 'Run console'
    


if __name__ == '__main__':
    run('CTRL', 'ALT', 'T')