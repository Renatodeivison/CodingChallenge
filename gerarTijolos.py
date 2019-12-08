from random import seed, randint
import time
from datetime import datetime
import matplotlib.pyplot as plt

# Funcao para gerar tijolos de maneira aleatória improvisada


def generateTijolos(max_int, altura):
    tijolo = []
    timestamp = int(time.mktime(datetime.now().timetuple()))
    seed(timestamp)

    for i in range(altura):
        tamTijolo = max_int
        linTijolo = []
        for j in range(max_int):
            tempTijolo = randint(1, tamTijolo)
            tamTijolo -= tempTijolo
            if tamTijolo < 1:
                linTijolo.append(tempTijolo)
                break
            else:
                linTijolo.append(tempTijolo)
        tijolo.append(linTijolo)
    return tijolo
