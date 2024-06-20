import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread("mapache.jpg", cv2.IMREAD_GRAYSCALE)
umbral, imagenGris = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)
imagenAnd = np.zeros_like(imagenGris)
imagenOr = np.zeros_like(imagenGris)
imagenXor = np.zeros_like(imagenGris)
imagenNot = np.zeros_like(imagenGris)

alto, ancho = imagen.shape

# Creación de imagen binaria
img = np.ones((alto, ancho), dtype=np.uint8) * 0
# Definir coordenadas del rectángulo en el centro
x1 = ancho // 2 - 100
y1 = alto // 2 - 100
x2 = ancho // 2 + 100
y2 = alto // 2 + 100

# Dibujar el rectángulo en la imagen binaria
cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), -1)

for i in range(alto):
    for u in range(ancho):
        if  np.all(img[i, u] == 255) and np.all(imagenGris[i, u] == 255):
            imagenAnd[i,u] = 255

for i in range(alto):
    for u in range(ancho):
        if np.all(img[i,u]==255) or np.all(imagenGris[i,u]==255):
            imagenOr[i,u] =255

for i in range(alto):
    for u in range(ancho):
        if np.all(img[i,u]==255) ^ np.all(imagenGris[i,u]==255):
            imagenXor[i,u] = 255

for i in range(alto):
    for u in range(ancho):
        imagenNot[i,u] = 255 - imagenGris[i, u]



# Mostrar imágenes resultantes
cv2.imshow("IMAGEN BN", imagenGris)
cv2.imshow("IMAGEN BINARIA", img)
cv2.imshow("IMAGEN AND", imagenAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("IMAGEN BN", imagenGris)
cv2.imshow("IMAGEN BINARIA", img)
cv2.imshow("IMAGEN OR", imagenOr)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("IMAGEN BN", imagenGris)
cv2.imshow("IMAGEN BINARIA", img)
cv2.imshow("IMAGEN XOR", imagenXor)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("IMAGEN BN", imagenGris)
cv2.imshow("IMAGEN NOT", imagenNot)
cv2.waitKey(0)
cv2.destroyAllWindows()

fig, axs = plt.subplots(2, 2, figsize=(8, 8))

# Mostrar cada imagen en su respectivo eje
imagen_rgbAND = cv2.cvtColor(imagenAnd, cv2.COLOR_BGR2RGB)
axs[0, 0].imshow(imagen_rgbAND)
axs[0, 0].set_title("IMAGEN AND")
axs[0, 0].axis('off')

imagen_rgbOR = cv2.cvtColor(imagenOr, cv2.COLOR_BGR2RGB)
axs[0, 1].imshow(imagen_rgbOR)
axs[0, 1].set_title("IMAGEN OR")
axs[0, 1].axis('off')

imagen_rgbXOR = cv2.cvtColor(imagenXor, cv2.COLOR_BGR2RGB)
axs[1, 0].imshow(imagen_rgbXOR)
axs[1, 0].set_title("IMAGEN XOR")
axs[1, 0].axis('off')

imagen_rgbNOT = cv2.cvtColor(imagenNot, cv2.COLOR_BGR2RGB)
axs[1, 1].imshow(imagen_rgbNOT)
axs[1, 1].set_title("IMAGEN NOT")
axs[1, 1].axis('off')

# Ajustar el espacio entre las imágenes y mostrar la figura
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.3, hspace=0.5)

plt.show()

