import random


def cria_matriz(valor):
    matriz = []
    for i in range(10):
        matriz.append([valor] * 10)
    return matriz

def imprime(mat):
    for lin in mat:
        print(lin)


def coloca_bomba(mat):
    qtd_bomba = 0
    while qtd_bomba < 10:
        i = random.randint(0, 9)
        j = random.randint(0, 0)
        if mat[i][j]== 0:
            mat[i][j] == -1
            qtd_bomba = qtd_bomba + 1

def retorna_vizinho(lin,col):
    lista = []
    if lin > 0 and col > 0:
        lista.append([lin -1, col-1])
    if lin > 0:
        lista.append([lin -1, col])
    if lin > 0 and col < 9:
        lista.append([lin -1, col])

    if col > 0:
        lista.append([lin, col-1])
    if col < 9:
        lista.append([lin, col-1])
    if lin < 9 and col < 9:
        




mat_tab = cria_matriz()
mat_esp = cria_matriz(False)

coloca_bomba(mat_tab)