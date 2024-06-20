import numpy as np
from funciones import f
import cv2


class esq():


    def esqueletizar(imagen, tam):
        alto_original, ancho_original = imagen.shape[:2]
        print((ancho_original // 2, alto_original // 2))
        imagen_redimensionada = cv2.resize(imagen, (ancho_original // 2, alto_original // 2))

        gray = cv2.cvtColor(imagen_redimensionada, cv2.COLOR_BGR2GRAY)
        _, binarizada = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        cont =0
        # Inicializar la imagen de salida (esqueleto)
        esqueleto = np.zeros_like(binarizada)

        while True:
            eroded = f.erosionGris(binarizada, tam)
            # Aplicar dilatación a la imagen erosionada
            temp = f.dilatacionGris(eroded, tam)
            temp = binarizada-temp
            esqueleto = np.bitwise_or(esqueleto, temp)
            binarizada = eroded.copy()
            cont=cont+1
            # Parar si no hay más cambios
            if np.count_nonzero(binarizada) == 0:
                break

        # Convertir el esqueleto a BGR para mostrarlo en color
        esqueleto_bgr = cv2.cvtColor(esqueleto, cv2.COLOR_GRAY2BGR)
        esqueleto_final = cv2.resize(esqueleto_bgr, (ancho_original, alto_original))

        return esqueleto_final


