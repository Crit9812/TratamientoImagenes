import cv2
import numpy as np
from tkinter import simpledialog
from funciones import f

class multiplicar():
    
    def color(imagen):
        alto,ancho,_=imagen.shape
        valor=simpledialog.askfloat("Valor","Ingresa el valor por el cual quieres multiplicar")
    
        imagenOp1 = np.zeros((alto, ancho, 3), np.uint32)
        imagenOp2 = np.zeros((alto, ancho, 3), np.uint32)
        imagenOp3 = np.zeros((alto, ancho, 3), np.uint32)

        #---------------truncar---------------------------------------
        for p in range(0,3):
            for i in range (0,alto):
                for j in range (0,ancho):
                    v1=int(imagen[i,j,p])
                    nuevoV=v1*valor            
                    if nuevoV>255:
                        nuevoV=255
                    if nuevoV<0:
                        nuevoV=0
                    imagenOp1[i,j,p]=nuevoV

        #---------------ciclico---------------------------------------
        imagenOp2= np.mod(imagen*valor, 256)

        arregloOp = np.zeros((alto, ancho, 3), dtype=np.int32)
        for p in range(0,3):
            for i in range (0,alto):
                for j in range (0,ancho):
                    v1=int(imagen[i,j,p])
                    nuevoV=v1*valor
                    arregloOp[i, j, p] = nuevoV

        #---------------escalar---------------------------------------

        min = np.min(arregloOp)
        max = np.max(arregloOp)
        for p in range(0,3):
            for i in range (0,alto):
                for j in range (0,ancho):
                    v1=int(imagen[i,j,p])
                    nuevoV=v1*valor
                    imagenOp3[i,j,p]=int((nuevoV - min) * 255 / (max - min))

        imagenOp1=f.conversion(imagenOp1)
        imagenOp2=f.conversion(imagenOp2)
        imagenOp3=f.conversion(imagenOp3)

        return imagenOp1, imagenOp2, imagenOp3
    
    def gris(imagen):
        alto,ancho=imagen.shape
        valor=simpledialog.askfloat("Valor","Ingresa el valor por el cual quieres multiplicar")
    
        imagenOp1 = np.zeros((alto, ancho, 3), np.uint32)
        imagenOp2 = np.zeros((alto, ancho, 3), np.uint32)
        imagenOp3 = np.zeros((alto, ancho, 3), np.uint32)
        
        # ---------------truncar---------------------------------------
        for i in range(0, alto):
            for j in range(0, ancho):
                v1= int(imagen[i, j])
                nuevoV= int(v1*valor)
                if nuevoV> 255:
                    nuevoV= 255
                if nuevoV< 0:
                    nuevoV= 0
                imagenOp1[i, j]= nuevoV

        # ---------------ciclico---------------------------------------
        imagenOp2= np.mod(imagen*valor, 256).astype(np.uint8)

        # ---------------escalar---------------------------------------
        arregloOp= np.zeros((alto, ancho), dtype=np.int32)
        for i in range(0, alto):
            for j in range(0, ancho):
                v1= int(imagen[i, j])
                nuevoV= int(v1*valor)
                arregloOp[i, j]= nuevoV

        minimo= np.min(arregloOp)
        maximo= np.max(arregloOp)
        for i in range(0, alto):
            for j in range(0, ancho):
                v1= int(imagen[i, j])
                nuevoV= int((v1*valor-minimo)*255 / (maximo-minimo))
                imagenOp3[i, j]= nuevoV
        imagenOp1=f.conversion(imagenOp1)
        imagenOp2=f.conversion(imagenOp2)
        imagenOp3=f.conversion(imagenOp3)
        return imagenOp1, imagenOp2, imagenOp3
    
    