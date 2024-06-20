import cv2
import numpy as np

# Función para aplicar el filtro Gaussiano
def filtro_gaussiano(imagen, tamano_kernel):
    # Crear el kernel Gaussiano utilizando una función de OpenCV
    # .5 para que se vea mas el contorno, entre mas pequeño mas visible menos suave la imagen
    kernel = cv2.getGaussianKernel(tamano_kernel, .5)
    # Aplicar el filtro Gaussiano
    #multiplicacion del kernel con si mismo transpuesto
    imagen_filtrada = cv2.filter2D(imagen, -1, kernel * kernel.T)
    return imagen_filtrada

# Función para la detección de bordes usando el operador Laplaciano


nombreImg="flores.jpg"
ruta="C:\\Users\\jessi\\Documents\\Universidad\\6to Semestre\\Procesamiento_imagenes\\Practicas\\Imagenes\\"+nombreImg
imagen=cv2.imread(ruta)


# Mostrar la imagen original y la imagen con bordes detectados
cv2.imshow('Original', imagen)
cv2.imshow('Imagen suavisada', imagen_suavizada)
cv2.imshow('Bordes Detectados', bordes_detectados)

# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
