# ****************************
# CONVIRTIENDO HTML A MARKDOWN
# ****************************


def run(html: str) -> str:
    # TU CÓDIGO AQUÍ
    markdown = html.replace('<h1>', '# ').replace('</h1>', '').replace('<h2>', '## ').replace('</h2>','').replace('<h3>', '### ').replace('</h3>','').replace('<h4>', '#### ').replace('</h4>','')

    return markdown


if __name__ == '__main__':
    run('<h1>Core</h1>')