import cv2
import numpy as np
from funciones import f

class detectar():
    
    def prewitt(imagen):
        imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        # Aplicar el filtro Gaussiano para reducir el ruido
        imagen_suavizada = f.filtro_gaussiano(imagen, 5)
        
        # Calcular los gradientes de la imagen usando el operador de Prewitt
        kernel_prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        kernel_prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        gradiente_x = cv2.filter2D(imagen_suavizada, -1, kernel_prewitt_x)
        gradiente_y = cv2.filter2D(imagen_suavizada, -1, kernel_prewitt_y)

        # Normalizar los gradientes para que estén en el rango [0, 255]
        gradiente_x = np.clip(gradiente_x, 0, 255).astype(np.uint8)
        gradiente_y = np.clip(gradiente_y, 0, 255).astype(np.uint8)
        
        gradiente_x=f.conversion(gradiente_x)
        gradiente_y=f.conversion(gradiente_y)
        return gradiente_x, gradiente_y
    
    def sobel(imagen):
        imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        # Aplicar el filtro Gaussiano para reducir el ruido
        imagen_suavizada = f.filtro_gaussiano(imagen, 5)

        # Crear los kernels de Sobel para calcular los gradientes
        kernel_sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        kernel_sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

        # Calcular los gradientes de la imagen utilizando los kernels de Sobel
        gradiente_x = cv2.filter2D(imagen_suavizada, -1, kernel_sobel_x)
        gradiente_y = cv2.filter2D(imagen_suavizada, -1, kernel_sobel_y)

        # Calcular la magnitud y la orientación del gradiente
        #magnitud_gradiente = np.sqrt(gradiente_x**2 + gradiente_y**2)
        #orientacion_gradiente = np.arctan2(gradiente_y, gradiente_x) * (180 / np.pi)

        gradiente_x=f.conversion(gradiente_x)
        gradiente_y=f.conversion(gradiente_y)
        return gradiente_x, gradiente_y
        
    def canny(imagen):
        imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        # Aplicar el filtro Gaussiano para reducir el ruido
        imagen_suavizada = f.filtro_gaussiano(imagen,5)

        # Calcular los gradientes de la imagen usando Sobel
        gradiente_x = cv2.Sobel(imagen_suavizada, cv2.CV_64F, 1, 0, ksize=3)
        gradiente_y = cv2.Sobel(imagen_suavizada, cv2.CV_64F, 0, 1, ksize=3)

        # Calcular la magnitud y la orientación del gradiente
        magnitud_gradiente = np.sqrt(gradiente_x**2 + gradiente_y**2)
        orientacion_gradiente = np.arctan2(gradiente_y, gradiente_x) * (180 / np.pi)

        # Supresión de no máximos
        bordes_suprimidos = np.zeros_like(magnitud_gradiente)
        filas, columnas = imagen.shape
        for i in range(1, filas - 1):
            for j in range(1, columnas - 1):
                angulo = orientacion_gradiente[i, j]
                vecinos = [0, 0]
                if (0 <= angulo < 22.5) or (157.5 <= angulo <= 180):
                    vecinos = [magnitud_gradiente[i, j-1], magnitud_gradiente[i, j+1]]
                elif (22.5 <= angulo < 67.5):
                    vecinos = [magnitud_gradiente[i-1, j-1], magnitud_gradiente[i+1, j+1]]
                elif (67.5 <= angulo < 112.5):
                    vecinos = [magnitud_gradiente[i-1, j], magnitud_gradiente[i+1, j]]
                elif (112.5 <= angulo < 157.5):
                    vecinos = [magnitud_gradiente[i-1, j+1], magnitud_gradiente[i+1, j-1]]
                
                if magnitud_gradiente[i, j] >= max(vecinos):
                    bordes_suprimidos[i, j] = magnitud_gradiente[i, j]
                    
        # Umbralización por histéresis
        umbral_bajo = 50
        umbral_alto = 90
        bordes = np.zeros_like(bordes_suprimidos, dtype=np.uint8)
        bordes[bordes_suprimidos >= umbral_alto] = 255
        for i in range(1, filas - 1):
            for j in range(1, columnas - 1):
                if umbral_bajo <= bordes_suprimidos[i, j] < umbral_alto:
                    vecinos = bordes_suprimidos[i-1:i+2, j-1:j+2]
                    if np.max(vecinos) >= umbral_alto:
                        bordes[i, j] = 255
        
        bordes=f.conversion(bordes)                
        return bordes
    
    def gauss( imagen):
        imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        # Aplicar filtro Gaussiano para suavizar la imagen
        imagen_suavizada = f.filtro_gaussiano(imagen, tamano_kernel=5)

        # Detección de bordes usando el operador Laplaciano
        bordes_detectados =f.deteccion_bordes_laplaciano(imagen_suavizada)

        # Convertir los valores negativos a positivos
        bordes_detectados = np.uint8(np.absolute(bordes_detectados))

        imagen = cv2.resize(imagen,(500,500))
        bordes_detectados = cv2.resize(bordes_detectados,(500,500))
        imagen_suavizada = cv2.resize(imagen_suavizada,(500,500))
        
        bordes_detectados=f.conversion(bordes_detectados)
        return bordes_detectados
    



