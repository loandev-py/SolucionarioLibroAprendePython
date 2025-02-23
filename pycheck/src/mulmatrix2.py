# *****************************
# MULTIPLICANDO MATRICES DE 2X2
# *****************************


def run(A: list, B: list) -> list:
    # TU CÓDIGO AQUÍ
    P = [[0,0],[0,0]]
    for i in range(len(A)):
      for j in range(len(B[0])):
         for k in range(len(B)):
            P[i][j] += A[i][k] * B[k][j]  
            
    return P


if __name__ == '__main__':
    run([[6, 4], [8, 9]], [[3, 2], [1, 7]])