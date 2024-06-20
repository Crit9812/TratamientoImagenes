
import cv2
import numpy as np
from funciones import f

class logGris():
    
    def andd(imagen,imagen2):
        imagen,imagen2=f.redimensionar(imagen,imagen2)
        alto, ancho = imagen.shape
        imagenAnd = np.zeros((alto, ancho), dtype=np.uint8)

        for i in range(alto):
            for u in range(ancho):
                imagenAnd[i,u] =imagen2[i,u] and imagen[i,u]
                
        imagenAnd=f.conversion(imagenAnd)  
        return imagenAnd
    
    def orr(imagen,imagen2):
        imagen,imagen2=f.redimensionar(imagen,imagen2)
        alto, ancho = imagen.shape
        imagenOr = np.zeros((alto, ancho), dtype=np.uint8)
        
        for i in range(alto):
            for u in range(ancho):
                imagenOr[i,u] =imagen2[i,u] or imagen[i,u]
        
        imagenOr=f.conversion(imagenOr)  
        return imagenOr

    def xorr(imagen,imagen2):
        imagen,imagen2=f.redimensionar(imagen,imagen2)
        alto, ancho = imagen.shape
        imagenXor = np.zeros((alto, ancho), dtype=np.uint8)
        
        for i in range(alto):
            for u in range(ancho):
                imagenXor[i,u] = imagen2[i,u] ^ imagen[i,u]

                
        imagenXor=f.conversion(imagenXor)  
        return imagenXor
    
    def nott(imagen):
        imagenNot, img ,x1, y1, x2, y2, alto, ancho=f.medidas(imagen)
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), -1)
        
        for i in range(alto):
            for u in range(ancho):
                imagenNot[i,u] = ~ imagen[i,u]
                
        imagenNot=f.conversion(imagenNot)  
        return imagenNot