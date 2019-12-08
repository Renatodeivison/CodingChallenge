from random import seed, randint
import time


def checkCut(pos, lin, tempPos):  # verifica se a linha a ser traçada cortou o tijolo
    tempTijolos = tijolos[lin]
    soma = sum(tempTijolos[:tempPos[lin]])
    if (soma <= pos):
        return 0
    else:
        return 1


def findLine(tijolos):
    qtnTijolo = sum(tijolos[:][0])
    altura = len(tijolos)
    tempPos = [1]*altura
    menosCortes = altura

    for pos in range(qtnTijolo-1):
        linha = 0
        for lin in range(altura):
            linha += checkCut(pos+1, lin, tempPos)
            if (checkCut(pos+1, lin, tempPos) == 0):
                tempPos[lin] += 1
            if ((linha > menosCortes) and (pos >= 1)):
                break
        if (linha <= menosCortes):
            menosCortes = linha
        if (linha == 0):
            return menosCortes

    return menosCortes


# insira seu input aqui
tijolos = [[1, 2, 2, 1],
           [3, 1, 2],
           [1, 3, 2],
           [2, 4],
           [3, 1, 2],
           [1, 3, 1, 1]]

menosCortes = findLine(tijolos)

print("Menor número de cortes:", menosCortes)
