import cv2
import numpy as np
import math
from tkinter import simpledialog

class tranformaciones2():
    
    def rotacion(imagen):
        
        angulo=simpledialog.askfloat("Rotacion","Ingresa el valor del angulo al cual quieres rotar la imagen: ")
        alto, ancho = imagen.shape[:2]
        centroX = ancho // 2
        centroY = alto // 2
        anguloRad = math.radians(angulo)
        imagenRotada = np.zeros_like(imagen)

        for y in range(alto):
            for x in range(ancho):
                nuevoX = int((x - centroX) * math.cos(anguloRad) - (y - centroY) * math.sin(anguloRad) + centroX)
                nuevoY = int((x - centroX) * math.sin(anguloRad) + (y - centroY) * math.cos(anguloRad) + centroY)
                if 0 <= nuevoX < ancho and 0 <= nuevoY < alto:
                    imagenRotada[nuevoY, nuevoX] = imagen[y, x]

        return imagenRotada
    
    def traslacion(imagen):
        
        dx=simpledialog.askfloat("Traslacion","Ingresa la coordenada en x para trasladar la imagen: ")
        dy=simpledialog.askfloat("Traslacion","Ingresa la coordenada en y para trasladar la imagen: ")
        alto, ancho = imagen.shape[:2]
        imagenTras = np.zeros_like(imagen)

        for y in range(alto):
            for x in range(ancho):
                nuevoX = x + dx
                nuevoY = y + dy
                if 0 <= nuevoX < ancho and 0 <= nuevoY < alto:
                    imagenTras[nuevoY, nuevoX] = imagen[y, x]
        
        return imagenTras
    
    def escalado(imagen):
        alto, ancho, n = imagen.shape

        tamXnuevo=simpledialog.askfloat("Escalado","Ingresa el nuevo tamaño de x para trasladar la imagen: ")
        tamYnuevo=simpledialog.askfloat("Escalado","Ingresa el nuevo tamaño de  y para trasladar la imagen: ")

        imagenRedimensionada = np.zeros((tamYnuevo, tamXnuevo, n), dtype=np.uint8)

        for y in range(tamYnuevo):
            for x in range(tamXnuevo):
                pixelXOriginal = int(x * (ancho / tamXnuevo))
                pixelYOriginal = int(y * (alto / tamYnuevo))
                pixelColor = imagen[pixelYOriginal, pixelXOriginal]
                imagenRedimensionada[y, x] = pixelColor
                
        return imagenRedimensionada


