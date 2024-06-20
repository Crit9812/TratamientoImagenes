import cv2
import numpy as np
from scipy.ndimage import maximum_filter
from tkinter import simpledialog
import tkinter as tk

class RellenoImagen:
    
    @staticmethod
    def dilatacion2(pixelesImg, margen):
        max_filt = maximum_filter(pixelesImg, size=2*margen+1, mode='constant')
        return max_filt

    @staticmethod
    def rellenar(imagen, semilla):
        E = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        alto, ancho = E.shape
        E_not = cv2.bitwise_not(E)
        X = np.zeros((alto, ancho), dtype=np.uint8)
        X[semilla[1], semilla[0]] = 255
        X_ant = np.zeros((alto, ancho), dtype=np.uint8)
        kernel = 1  # Kernel size set to 1 for simplicity

        while True:
            X = cv2.bitwise_and(RellenoImagen.dilatacion2(X, kernel), E_not)
            if np.array_equal(X_ant, X):
                break
            X_ant = X.copy()

        
        return X

    @staticmethod
    def guardarDatosClick(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN and not params['clic']:
            cv2.circle(params['imagenOriginal'], (x, y), 3, (255, 255, 255), -1)
            params['semilla'].extend([x, y])
            params['clic'] = True
            cv2.setMouseCallback("Imagen Original", lambda *args: None)
            cv2.imshow("Imagen Original", params['imagenOriginal'])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            resultado = RellenoImagen.rellenar(params['imagen'], params['semilla'])
            cv2.imshow("Resultado Final", resultado)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# Código principal
if __name__ == "__main__":
    # Ruta de la imagen
    nombreImg = "relleno.jpg"
    ruta = "C:\\Users\\jessi\\Documents\\Universidad\\6to Semestre\\Procesamiento_imagenes\\Practicas\\Imagenes\\" + nombreImg
    
    # Cargar la imagen
    imagenOriginal = cv2.imread(ruta)
    imagen = cv2.imread(ruta)
    clic = False
    semilla = []

    params = {
        'imagenOriginal': imagenOriginal,
        'imagen': imagen,
        'clic': clic,
        'semilla': semilla
    }

    cv2.imshow("Imagen Original", imagenOriginal)
    cv2.setMouseCallback("Imagen Original", RellenoImagen.guardarDatosClick, params)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

