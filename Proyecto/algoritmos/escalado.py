import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

imagen = cv2.imread('nina.jpg')

alto, ancho, n = imagen.shape

tamXnuevo = 200
tamYnuevo = 150

imagenRedimensionada = np.zeros((tamYnuevo, tamXnuevo, n), dtype=np.uint8)

for y in range(tamYnuevo):
    for x in range(tamXnuevo):
        pixelXOriginal = int(x * (ancho / tamXnuevo))
        pixelYOriginal = int(y * (alto / tamYnuevo))
        pixelColor = imagen[pixelYOriginal, pixelXOriginal]
        imagenRedimensionada[y, x] = pixelColor

cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Escalada mia', imagenRedimensionada)

cv2.waitKey(0)
cv2.destroyAllWindows()
