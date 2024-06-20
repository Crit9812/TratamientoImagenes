import cv2
import numpy as np
import matplotlib.pyplot as plt
from funciones import f

class hist():
    
    def color(imagen):
        alto, ancho, _ = imagen.shape
        azules = []
        verdes = []
        rojos = []
        # Iterar sobre cada píxel y almacenar los valores de los niveles de color
        for y in range(ancho):
            for x in range(alto):
                pixel = imagen[x, y]
                azules.append(pixel[0])
                verdes.append(pixel[1])
                rojos.append(pixel[2])
        hist_azul, bins_azul = np.histogram(azules, bins=256, range=(0,256))
        hist_verde, bins_verde = np.histogram(verdes, bins=256, range=(0,256))
        hist_rojo, bins_rojo = np.histogram(rojos, bins=256, range=(0,256))
    
        plt.figure(figsize=(10, 5))
        plt.plot(bins_azul[:-1], hist_azul, color='blue', alpha=0.5, label='Azul')
        plt.plot(bins_azul[:-1], hist_verde, color='green', alpha=0.5, label='Verde')
        plt.plot(bins_azul[:-1], hist_rojo, color='red', alpha=0.5, label='Rojo')
        plt.xlabel('Valor del píxel')
        plt.ylabel('Frecuencia')
        plt.title('Histograma de Colores')
        plt.legend()
        plt.savefig('histograma.png')
        plt.close()
        imgH=cv2.imread('histograma.png')
        
        imgH=f.conversion(imgH)
        return imgH    
    
    def gris(imagen):
        alto, ancho = imagen.shape

        grises = []
        for y in range(ancho):
            for x in range(alto):
                intensidad = imagen[x, y]
                grises.append(intensidad)

        hist_gris, bins_gris = np.histogram(grises, bins=256, range=(0,256))
        
        
        
        plt.figure(figsize=(10, 5))
        plt.plot(bins_gris[:-1], hist_gris, color='gray', alpha=0.5, label='Gris')
        plt.xlabel('Valor del píxel')
        plt.ylabel('Frecuencia')
        plt.title('Histograma de Grises')
        plt.legend()
        plt.savefig('histograma.png')
        plt.close()
        imgH=cv2.imread('histograma.png')
        
        imgH=f.conversion(imgH)
        return imgH
