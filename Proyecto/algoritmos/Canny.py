import cv2
import numpy as np
import matplotlib.pyplot as plt

def filtro_gaussiano(imagen, tamano_kernel):
    # Crear el kernel Gaussiano utilizando una función de OpenCV
    # .5 para que se vea mas el contorno, entre mas pequeño mas visible menos suave la imagen
    kernel = cv2.getGaussianKernel(tamano_kernel, .5)
    # Aplicar el filtro Gaussiano
    #multiplicacion del kernel con si mismo transpuesto
    imagen_filtrada = cv2.filter2D(imagen, -1, kernel * kernel.T)
    return imagen_filtrada

# Cargar la imagen en escala de grises
nombreImg="flores.jpg"
ruta="C:\\Users\\jessi\\Documents\\Universidad\\6to Semestre\\Procesamiento_imagenes\\Practicas\\Imagenes\\"+nombreImg
imagen=cv2.imread(ruta)


# Mostrar la imagen original y los bordes detectados
plt.subplot(121), plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(bordes, cmap='gray')
plt.title('Bordes Canny'), plt.xticks([]), plt.yticks([])
plt.show()
