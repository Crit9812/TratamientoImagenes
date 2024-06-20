import cv2
import numpy as np
from scipy.ndimage import maximum_filter
from tkinter import messagebox

class RellenoImagen():
    

    def dilatacion2(self, pixelesImg, margen):
        max_filt = maximum_filter(pixelesImg, size=2*margen+1, mode='constant')
        return max_filt

    def rellenar(self, imagen):
        messagebox.showinfo("Mensaje","Agrega el punto semilla a partir del cual se va a rellenar la imagen. Presiona cualquier tecla para terminar ")
        self.imagen = imagen
        self.imagenOriginal = imagen.copy()
        self.semilla = []
        self.clic = False

        cv2.imshow("Imagen Original", self.imagenOriginal)
        cv2.setMouseCallback("Imagen Original", self.guardarDatosClick)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if not self.clic:
            print("No se seleccionó ninguna semilla.")
            return None

        E = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        alto, ancho = E.shape
        E_not = cv2.bitwise_not(E)
        X = np.zeros((alto, ancho), dtype=np.uint8)
        X[self.semilla[1], self.semilla[0]] = 255
        X_ant = np.zeros((alto, ancho), dtype=np.uint8)
        kernel = 1  # Kernel size set to 1 for simplicity

        while True:
            X = cv2.bitwise_and(self.dilatacion2(X, kernel), E_not)
            if np.array_equal(X_ant, X):
                break
            X_ant = X.copy()
        
        return X

    def guardarDatosClick(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN and not self.clic:
            cv2.circle(self.imagenOriginal, (x, y), 3, (255, 255, 255), -1)
            self.semilla = [x, y]
            self.clic = True
            cv2.setMouseCallback("Imagen Original", lambda *args: None)
            cv2.imshow("Imagen Original", self.imagenOriginal)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# Ejemplo de cómo usar la clase RellenoImagen:
# instancia_k = RellenoImagen()
# img11 = instancia_k.rellenar(self.imagen0)
# if img11 is not None:
#     cv2.imshow("Resultado Final", img11)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()



