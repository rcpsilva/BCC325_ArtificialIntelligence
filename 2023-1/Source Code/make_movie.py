import matplotlib.pyplot as plt
import numpy as np
from Labirinto import Labirinto

def make_movie(L):

    plt.ion()

    for caminho in L.caminhos:
        plt.axes().invert_yaxis()
        plt.pcolormesh(L.map)
        for i in range(len(caminho)-1):
            plt.plot([caminho[i][1]+0.5,caminho[i+1][1]+0.5],[caminho[i][0]+0.5,caminho[i+1][0]+0.5],'-rs')
        plt.draw()
        plt.pause(0.1)
        plt.clf()
