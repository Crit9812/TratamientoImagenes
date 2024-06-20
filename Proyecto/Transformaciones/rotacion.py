import cv2
import numpy as np
import math

imagen = cv2.imread('flowers.jpg')
imagen = cv2.resize(imagen, (500, 500))

angulo = 45

alto, ancho = imagen.shape[:2]

centroX = ancho // 2
centroY = alto // 2

anguloRad = math.radians(angulo)

imagenRotada = np.zeros_like(imagen)

for y in range(alto):
    for x in range(ancho):
        # Calcular la posicion del pixel original despues de la rotacion
        nuevoX = int((x - centroX) * math.cos(anguloRad) - (y - centroY) * math.sin(anguloRad) + centroX)
        nuevoY = int((x - centroX) * math.sin(anguloRad) + (y - centroY) * math.cos(anguloRad) + centroY)

        # Verificar si las coordenadas rotadas estan dentro de los limites de la imagen
        if 0 <= nuevoX < ancho and 0 <= nuevoY < alto:
            # Asignar el valor del pixel original al pixel correspondiente en la imagen rotada
            imagenRotada[nuevoY, nuevoX] = imagen[y, x]

cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Rotada Manualmente', imagenRotada)

cv2.waitKey(0)
cv2.destroyAllWindows()
