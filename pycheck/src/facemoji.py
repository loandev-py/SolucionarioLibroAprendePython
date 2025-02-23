# ****************
# TODO SON CARITAS
# ****************


def run(emoji_text: str) -> str:
    # TU CÓDIGO AQUÍ
    match emoji_text:
        case 'happy':
            emoji = '😀'
        case 'SAD':
            emoji = '😔'
        case 'Angry':
            emoji = '😡'
        case 'peNsive':
            emoji = '🤔'
        case 'surpriseD':
            emoji = '😮'

    return emoji


if __name__ == '__main__':
    run('happy')