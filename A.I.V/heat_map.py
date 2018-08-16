# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 18:34:19 2018

@author: ggoncalves
"""
import sys

from matplotlib import pyplot as PLT
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as NP


class HeatMaping:
    __WIDTH = 30
    __HIGHT = 15
    __VALOR_INCREMENTAL = 4
    __VALOR_INCREMENTAL_PERIFERIA = __VALOR_INCREMENTAL/2
    __HEATTYPE = 'jet'
    __RAIO = 2

    @property
    def resolucao(self):
        return self.__RESOLUCAO;

    @resolucao.setter
    def resolucao(self, value):
        self.__RESOLUCAO = int(value);

    @property
    def heatArray(self):
        return self.__heatValue

    @heatArray.setter
    def heatArray(self, value):
        if (value.size == self.__RESOLUCAO):
            self.__heatValue = value;

    def __init__(self):
        try:
            # create the figure
            self.fig = PLT.figure()
            PLT.set_cmap(self.__HEATTYPE)

            ax = self.fig.add_subplot(111)
            self.__heatValue = NP.zeros((self.__HIGHT, self.__WIDTH))#random.random((self.__HIGHT, self.__WIDTH))
            self.im = ax.imshow(self.__heatValue,interpolation='nearest')
            self.clb = self.fig.colorbar(self.im, ticks=[]);

            self.config_heat_fig();
            PLT.show(block=False)
            PLT.pause(0.01)
        except:
            pass

    def incrementa(self, x, y):

        self.heatArray[x][y] = self.__VALOR_INCREMENTAL
        self.__VALOR_INCREMENTAL += 5

        __heat = [8];

        if (0 > x > self.__WIDTH or 0 > y > self.__HIGHT):
            #Adicionar mensagem de erro!!
            return;

        # local = (x * self.__RESOLUCAO + y * self.__RESOLUCAO)


        for i in range(0, self.__RAIO):

            self.__heatValue[x + i][0] = self.__VALOR_INCREMENTAL;                  # direita
            self.__heatValue[x - i][0] = self.__VALOR_INCREMENTAL;                  # esquerda
            self.__heatValue[0][y + i] = self.__VALOR_INCREMENTAL;                  # cima
            self.__heatValue[0][y - i] = self.__VALOR_INCREMENTAL;
            self.__heatValue[x + i][y + i] = self.__VALOR_INCREMENTAL_PERIFERIA;    # direita em cima
            self.__heatValue[x - i][y + i] = self.__VALOR_INCREMENTAL_PERIFERIA;    # esquerda em cima
            self.__heatValue[x - i][y + i] = self.__VALOR_INCREMENTAL_PERIFERIA;    # direita em baixo
            self.__heatValue[x - i][y - i] = self.__VALOR_INCREMENTAL_PERIFERIA;    # esquerda em baixo

        for posicao in __heat:

            if (posicao > self.__RESOLUCAO or posicao < 0):
                continue;

            self.__heatValue[posicao] = self.__VALOR_INCREMENTAL;

        return;

    def show_map(self):
        try:
            #Transfor para numpy array
            # self.__heatValue = NP.random.random((self.__HIGHT, self.__WIDTH))
            self.im.set_array(self.__heatValue)
            self.fig.canvas.draw()

            vmax = self.__heatValue.max()
            vmin = self.__heatValue.min()

            self.clb.set_clim(vmin=vmin,vmax=vmax);

            PLT.pause(0.01)
        except:
            error = sys.exc_info()[0]
            print("Unexpected error:", error)
            pass
        return


    def teste_heat(self):
        self.__heatValue = NP.random.random((self.__HIGHT, self.__WIDTH))
        return

    def config_heat_fig(self):

        PLT.axis('off');
        PLT.suptitle("A.I.V.");
        PLT.colorbar()

    # def incr(self):
        # self.heatArray[]

if (__name__ == '__main__' ):

    hm = HeatMaping()

    # heat = []
    for i in range(14, -1, -1):
        # heat.append([0])
        for k in range(30):
            # heat[i].append(0)
            hm.incrementa(i, k)
            hm.show_map()

    hm.show_map()