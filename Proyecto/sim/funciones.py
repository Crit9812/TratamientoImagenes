import cv2
import numpy as np
from tkinter import simpledialog
from tkinter import messagebox
import os

class f():

    def dilatacionGris(imagen, tam_kernel):
        if len(imagen.shape) > 2:
            imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        tam_kernel += 1 if tam_kernel % 2 == 0 else 0
        ancho_relleno = tam_kernel // 2
        imagen_padded = np.pad(imagen, pad_width=ancho_relleno, mode='edge')
        alto, ancho = imagen.shape
        imagen_dilatada = np.zeros_like(imagen)

        for i in range(alto):
            for j in range(ancho):
                vecindario = imagen_padded[i:i+tam_kernel, j:j+tam_kernel]
                imagen_dilatada[i, j] = np.max(vecindario)

        return imagen_dilatada

    def dilatacionRGB(imagen, tam_kernel):
        if tam_kernel % 2 == 0: 
            tam_kernel += 1
        
        ancho_relleno = tam_kernel // 2
        alto, ancho, canales = imagen.shape
        
        # Rellenar la imagen para manejar los bordes
        imagen_padded = np.pad(imagen, pad_width=((ancho_relleno, ancho_relleno), (ancho_relleno, ancho_relleno), (0, 0)), mode='edge')
        
        imagen_dilatada = np.zeros_like(imagen)
        
        for i in range(alto):
            for j in range(ancho):
                for c in range(canales):
                    # Obtener la región del vecindario
                    vecindario = imagen_padded[i:i+tam_kernel, j:j+tam_kernel, c]
                    imagen_dilatada[i, j, c] = np.max(vecindario)
        
        return imagen_dilatada
        
    def erosionGris(imagen, tam_kernel):
        if len(imagen.shape) > 2:
            imagen = imagen.mean(axis=2).astype(np.uint8)

        tam_kernel += 1 if tam_kernel % 2 == 0 else 0
        ancho_relleno = tam_kernel // 2
        imagen_padded = np.pad(imagen, pad_width=ancho_relleno, mode='edge')
        alto, ancho = imagen.shape
        imagen_erosionada = np.zeros_like(imagen)

        for i in range(alto):
            for j in range(ancho):
                vecindario = imagen_padded[i:i+tam_kernel, j:j+tam_kernel]
                imagen_erosionada[i, j] = np.min(vecindario)

        return imagen_erosionada

    def erosionRGB(imagen, tam_kernel):
        if tam_kernel % 2 == 0: 
            tam_kernel += 1
        
        ancho_relleno = tam_kernel // 2
        alto, ancho, canales = imagen.shape
        
        # Rellenar la imagen para manejar los bordes
        imagen_padded = np.pad(imagen, pad_width=((ancho_relleno, ancho_relleno), (ancho_relleno, ancho_relleno), (0, 0)), mode='edge')
        
        imagen_erosionada = np.zeros_like(imagen)
        
        for i in range(alto):
            for j in range(ancho):
                for c in range(canales):
                    # Obtener la región del vecindario
                    vecindario = imagen_padded[i:i+tam_kernel, j:j+tam_kernel, c]
                    imagen_erosionada[i, j, c] = np.min(vecindario)
        
        return imagen_erosionada

    def modificarImg(image, angle, scale):
        # Obtener dimensiones de la imagen
        (h, w) = image.shape[:2]
        # Obtener el centro de la imagen
        center = (w // 2, h // 2)
        # Calcular la matriz de rotación
        M = cv2.getRotationMatrix2D(center, angle, scale)
        # Aplicar la matriz de rotación
        rotated_image = cv2.warpAffine(image, M, (w, h))
        return rotated_image