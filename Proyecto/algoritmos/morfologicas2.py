import numpy as np
from funciones import f
import cv2

class morf2():

    def aperturaGris(imagen, tam):
        imgErosionada = f.erosionGris(imagen, tam)
        apertura = f.dilatacionGris(imgErosionada, tam)
        
        return apertura

    def aperturaRGB(imagen, tam):
        imgErosionada = f.erosionRGB(imagen, tam)
        apertura = f.dilatacionRGB(imgErosionada, tam)
        
        return apertura

    def clausuraGris(imagen, tam):
        imgDilatada = f.dilatacionGris(imagen, tam)
        clausura = f.erosionGris(imgDilatada, tam)
        
        return clausura

    def clausuraRGB(imagen, tam):
        imgDilatada = f.dilatacionRGB(imagen, tam)
        clausura = f.erosionRGB(imgDilatada, tam)
        
        return clausura

    def gradienteGris(imagen, tam):
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        imgErosionada = f.erosionGris(imagen, tam)
        imgDilatada = f.dilatacionGris(imagen, tam)
        gradienteImg = np.abs(imgDilatada - imgErosionada )
        
        return gradienteImg.astype(np.uint8)

    def gradienteRGB(imagen, tam):
        imgErosionada = f.erosionRGB(imagen, tam)
        imgDilatada = f.dilatacionRGB(imagen, tam)
        gradienteImg = np.abs (imgDilatada - imgErosionada )
        
        return gradienteImg.astype(np.uint8)

    def perimetroGris(imagen, tam):
        imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        imgErosionada=f.erosionGris(imagen, tam)
        perimetro = imagen-imgErosionada
        
        return perimetro

    def perimetroRGB(imagen,tam):
        imgErosionada=f.erosionRGB(imagen,tam)
        perimetro=imagen-imgErosionada
        
        return perimetro