import numpy as np
import cv2


class Houhg():

    def transformar(imagen):
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        filas, columnas, _ = imagen.shape
        imgCanny = cv2.Canny(gray, 50, 150,apertureSize=3)
        coordenadasBlancas = np.where(imgCanny == 255)
        coordenadas_blancas_arreglo = np.column_stack((coordenadasBlancas[0], coordenadasBlancas[1]))

        maxValRho = abs(int(filas * np.cos(180) + columnas* np.sin(180)))+1
        Histograma2D = np.zeros(((maxValRho*2), 180))
        valoresRhoPorCadaPixel = np.zeros((filas, columnas), dtype=int)
        valoresThetaPorCadaPixel = np.zeros((filas, columnas), dtype=int)
        resolucionTheta = np.pi /180

        # asociar cada pixel con rho y theta
        for coordenada in coordenadas_blancas_arreglo:
            y, x = coordenada
            for o in range(180):
                Theta = o * resolucionTheta
                rho = int(x * np.cos(Theta) + y* np.sin(Theta))+ maxValRho
                Histograma2D[rho, o] += 1
                valoresRhoPorCadaPixel[y, x] = rho
                valoresThetaPorCadaPixel[y, x] = o

        valoresMayores0 = valoresRhoPorCadaPixel > 0
        valores_filtrados = valoresRhoPorCadaPixel[valoresMayores0]

        valoresMayores0_2 = valoresThetaPorCadaPixel > 0
        valores_filtrados_2 = valoresThetaPorCadaPixel[valoresMayores0_2]
        umbralDeteccionLineas = 200  

        lines = []
        for indiceRho in range(Histograma2D.shape[0]):
            for indiceTheta in range(Histograma2D.shape[1]):
                if Histograma2D[indiceRho, indiceTheta] > umbralDeteccionLineas:
                    rho = indiceRho - maxValRho 
                    theta = indiceTheta * resolucionTheta
                    lines.append((rho, theta))

        for rho, theta in lines:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(imagen, (x1, y1), (x2, y2), (0, 0, 255), 2)

        return imagen
