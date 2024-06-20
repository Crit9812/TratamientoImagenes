import cv2
import numpy as np

imagen1 = cv2.imread('flowers.jpg')
imagen = cv2.resize(imagen1,(500,500))

dx = 50
dy = 30

alto, ancho = imagen.shape[:2]
imagenTras = np.zeros_like(imagen)

for y in range(alto):
    for x in range(ancho):
        nuevoX = x + dx
        nuevoY = y + dy
        if 0 <= nuevoX < ancho and 0 <= nuevoY < alto:
            imagenTras[nuevoY, nuevoX] = imagen[y, x]

cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Trasladada Manualmente', imagenTras)

cv2.waitKey(0)
cv2.destroyAllWindows()
