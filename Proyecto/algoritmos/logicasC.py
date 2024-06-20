
import cv2
import numpy as np
from funciones import f

class logColor():
    
    def andd(imagen, imagen2):
        #imagenAnd, img ,x1, y1, x2, y2, alto, ancho=f.medidasColor(imagen)
        #cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), -1)
        imagen,imagen2=f.redimensionar(imagen,imagen2)
        alto, ancho,n = imagen.shape
        imagenAnd = np.zeros((alto, ancho,n), dtype=np.uint8)

        for i in range(alto):
            for u in range(ancho):
                imagenAnd[i,u,0] =imagen2[i,u,0] and imagen[i,u,0]
                imagenAnd[i,u,1] =imagen2[i,u,1] and imagen[i,u,1]
                imagenAnd[i,u,2] =imagen2[i,u,2] and imagen[i,u,2]
        
        imagenAnd=f.conversion(imagenAnd)        
        return imagenAnd
    
    def orr(imagen,imagen2):
        imagen,imagen2=f.redimensionar(imagen,imagen2)
        alto, ancho ,n= imagen.shape
        imagenOr = np.zeros((alto, ancho,n), dtype=np.uint8)

        for i in range(alto):
            for u in range(ancho):
                imagenOr[i,u,0] =imagen2[i,u,0] or imagen[i,u,0]
                imagenOr[i,u,1] =imagen2[i,u,1] or imagen[i,u,1]
                imagenOr[i,u,2] =imagen2[i,u,2] or imagen[i,u,2]
        
        imagenOr=f.conversion(imagenOr)  
        return imagenOr

    def xorr(imagen,imagen2):
        imagen,imagen2=f.redimensionar(imagen,imagen2)
        alto, ancho ,n= imagen.shape
        imagenXor = np.zeros((alto, ancho,n), dtype=np.uint8)

        for i in range(alto):
            for u in range(ancho):
                imagenXor[i,u,0] =imagen2[i,u,0] ^ imagen[i,u,0]
                imagenXor[i,u,1] =imagen2[i,u,1] ^ imagen[i,u,1]
                imagenXor[i,u,2] =imagen2[i,u,2] ^ imagen[i,u,2]
                
        imagenXor=f.conversion(imagenXor)  
        return imagenXor
    
    def nott(imagen):
        imagenNot, img ,x1, y1, x2, y2, alto, ancho=f.medidasColor(imagen)
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), -1)
        
        for i in range(alto):
            for u in range(ancho):
                imagenNot[i,u,0] = ~ imagen[i,u,0]
                imagenNot[i,u,1] = ~ imagen[i,u,1]
                imagenNot[i,u,2] = ~ imagen[i,u,2]
                
        imagenNot=f.conversion(imagenNot)  
        return imagenNot