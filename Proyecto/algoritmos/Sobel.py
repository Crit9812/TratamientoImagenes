import cv2
import numpy as np
import matplotlib.pyplot as plt

nombreImg="flores.jpg"
ruta="C:\\Users\\jessi\\Documents\\Universidad\\6to Semestre\\Procesamiento_imagenes\\Practicas\\Imagenes\\"+nombreImg
imagen=cv2.imread(ruta)
imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Función para aplicar el filtro Gaussiano
def filtro_gaussiano(imagen, tamano_kernel):
    # Crear el kernel Gaussiano utilizando una función de OpenCV
    # .5 para que se vea mas el contorno, entre mas pequeño mas visible menos suave la imagen
    kernel = cv2.getGaussianKernel(tamano_kernel, .5)
    # Aplicar el filtro Gaussiano
    #multiplicacion del kernel con si mismo transpuesto
    imagen_filtrada = cv2.filter2D(imagen, -1, kernel * kernel.T)
    return imagen_filtrada

# Aplicar el filtro Gaussiano para reducir el ruido
imagen_suavizada = filtro_gaussiano(imagen, 5)

# Crear los kernels de Sobel para calcular los gradientes
kernel_sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel_sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Calcular los gradientes de la imagen utilizando los kernels de Sobel
gradiente_x = cv2.filter2D(imagen_suavizada, -1, kernel_sobel_x)
gradiente_y = cv2.filter2D(imagen_suavizada, -1, kernel_sobel_y)

# Calcular la magnitud y la orientación del gradiente
magnitud_gradiente = np.sqrt(gradiente_x**2 + gradiente_y**2)
orientacion_gradiente = np.arctan2(gradiente_y, gradiente_x) * (180 / np.pi)

# Mostrar los resultados
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')

plt.subplot(1, 3, 2)
plt.imshow(gradiente_x, cmap='gray')
plt.title('Gradiente en X')

plt.subplot(1, 3, 3)
plt.imshow(gradiente_y, cmap='gray')
plt.title('Gradiente en Y')

plt.show()
