import numpy as np
from funciones import f
import cv2

class Hats():

    def blackHat (imagen, kernel):
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        dilatada = f.dilatacionGris(imagen, kernel)
        cerrada = f.erosionGris(dilatada, kernel)
        blackhat =cerrada-imagen
        return blackhat 

    def topHat (imagen, kernel):
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        erosionada = f.erosionGris(imagen, kernel)
        abierta = f.dilatacionGris(erosionada, kernel)
        tophat = imagen - abierta
        return tophat