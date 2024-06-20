import numpy as np
import cv2

class Esqueletizador:

    @staticmethod
    def verificar_vecinos(p, img):
        # Definir vecinos de un punto p
        vecinos = [(p[0] - 1, p[1]), (p[0] - 1, p[1] + 1), (p[0], p[1] + 1), (p[0] + 1, p[1] + 1),
                   (p[0] + 1, p[1]), (p[0] + 1, p[1] - 1), (p[0], p[1] - 1), (p[0] - 1, p[1] - 1)]

        # Contar píxeles blancos en los vecinos de p
        vecinos_blancos = sum([img[i, j] for i, j in vecinos])

        # Condiciones de eliminación de puntos
        if vecinos_blancos < 2 or vecinos_blancos > 6:
            return False

        transiciones = 0
        for i in range(len(vecinos)):
            if img[vecinos[i]] == 0 and img[vecinos[(i + 1) % len(vecinos)]] == 1:
                transiciones += 1

        if transiciones != 1:
            return False

        # Condiciones de conectividad
        if img[p[0] - 1, p[1]] * img[p[0], p[1] + 1] * img[p[0] + 1, p[1]] * img[p[0], p[1] - 1] == 1:  # t
            return False
        if img[p[0] - 1, p[1]] * img[p[0] - 1, p[1] + 1] * img[p[0] + 1, p[1] + 1] * img[p[0] + 1, p[1]] * img[
            p[0] + 1, p[1] - 1] * img[p[0] - 1, p[1] - 1] == 1:  # I
            return False
        if img[p[0], p[1] + 1] * img[p[0] + 1, p[1]] * img[p[0], p[1] - 1] == 1:  # v
            return False

        # Si ninguna de las condiciones anteriores se cumple, el punto puede ser eliminado y la función devuelve True
        return True

    @staticmethod
    def eliminar_pixel(p, img):
        if Esqueletizador.verificar_vecinos(p, img):
            img[p[0], p[1]] = 0

    @staticmethod
    def esqueletizar_pavlidis(img):
        nf, nc = img.shape
        d = 1  # tamaño de la plantilla de 3x3

        # Convertir imagen a 0s y 1s
        img = np.where(img > 0, 1, 0)

        # Crear una matriz para marcar los píxeles que se eliminan
        a_eliminar = np.zeros_like(img)

        # Realizar iteraciones hasta que no haya más cambios
        hay_cambios = True
        while hay_cambios:
            hay_cambios = False

            # Paso 1: Marcar los píxeles que se pueden eliminar
            for i in range(1 + d, nf - d):
                for j in range(1 + d, nc - d):
                    if img[i, j] == 1 and a_eliminar[i, j] == 0 and Esqueletizador.verificar_vecinos((i, j), img):
                        a_eliminar[i, j] = 1
                        hay_cambios = True

            # Paso 2: Eliminar los píxeles marcados
            for i in range(1 + d, nf - d):
                for j in range(1 + d, nc - d):
                    if a_eliminar[i, j] == 1:
                        Esqueletizador.eliminar_pixel((i, j), img)
                        a_eliminar[i, j] = 0

        return img.astype(np.uint8) * 255

    @staticmethod
    def go(imagen):
        img = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        esqueleto = Esqueletizador.esqueletizar_pavlidis(img)
        return esqueleto
