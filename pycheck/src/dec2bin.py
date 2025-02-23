# *****************
# DECIMAL A BINARIO
# *****************


def run(num: int) -> str:
    # TU CÓDIGO AQUÍ
    bin_results = []

    def helper(n):
        if n > 0:
            helper(n//2)
        bin_results.append(str(n % 2))

    helper(num)
    
    if not bin_results:
        bin_results.append('0')

    return ''.join(bin_results[1::])


if __name__ == '__main__':
    run(1)