import cv2
import numpy as np
from tkinter import simpledialog
from funciones import f

class mediana():
    
    def filtro(imagenC, val):
        if val==0:
            n=simpledialog.askinteger("Matriz","Ingresa el tamaño de la matriz: ")
            if n%2==0: n=n+1
            imagen=cv2.cvtColor(imagenC, cv2.COLOR_BGR2GRAY)
            
        else:
            n=11
            imagen=imagenC

        margen=n//2

        alto,ancho=imagen.shape
        pixelesImg=np.array(imagen)
        nuevaImg=np.zeros((alto, ancho), dtype=np.uint8)

        # ------------------------------para toda la imagen--------------------------------------------
        for i in range(0,alto):
            for j in range(0,ancho):
                columna=max(0, i-margen)
                columnaFin=min(alto, i+margen+1)
                fila=max(0, j-margen)
                filaFin=min(ancho, j+margen+1)

                matriz=pixelesImg[columna:columnaFin, fila:filaFin]
                ordenado=np.sort(matriz)
                media=np.median(ordenado)
                nuevaImg[i, j]=int(media)

        nuevaImg=f.conversion(nuevaImg)
        return nuevaImg
