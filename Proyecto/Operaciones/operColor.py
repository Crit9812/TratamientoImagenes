import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread("mapache.jpg")
imagenAnd = cv2.imread("mapache.jpg")
imagenOr = cv2.imread("mapache.jpg")
imagenXor = cv2.imread("mapache.jpg")
imagenNot = cv2.imread("mapache.jpg")

alto, ancho, nv = imagen.shape

# Creación de imagen binaria
img = np.ones((alto, ancho, nv), dtype=np.uint8) * 0
# Definir coordenadas del rectángulo en el centro
x1 = ancho // 2 - 100
y1 = alto // 2 - 100
x2 = ancho // 2 + 100
y2 = alto // 2 + 100

# Dibujar el rectángulo en la imagen binaria
cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), -1)

for i in range(alto):
    for u in range(ancho):
        imagenAnd[i,u,0] =img[i,u,0] and imagen[i,u,0]
        imagenAnd[i,u,1] =img[i,u,1] and imagen[i,u,1]
        imagenAnd[i,u,2] =img[i,u,2] and imagen[i,u,2]

for i in range(alto):
    for u in range(ancho):
        imagenOr[i,u,0] =img[i,u,0] or imagen[i,u,0]
        imagenOr[i,u,1] =img[i,u,1] or imagen[i,u,1]
        imagenOr[i,u,2] =img[i,u,2] or imagen[i,u,2]

for i in range(alto):
    for u in range(ancho):
        imagenXor[i,u,0] = img[i,u,0] ^ imagen[i,u,0]
        imagenXor[i,u,1] = img[i,u,1] ^ imagen[i,u,1]
        imagenXor[i,u,2] = img[i,u,2] ^ imagen[i,u,2]

for i in range(alto):
    for u in range(ancho):
        imagenNot[i,u,0] = ~ imagen[i,u,0]
        imagenNot[i,u,1] = ~ imagen[i,u,1]
        imagenNot[i,u,2] = ~ imagen[i,u,2]



# Mostrar imágenes resultantes
cv2.imshow("IMAGEN", imagen)
cv2.imshow("IMAGEN BINARIA", img)
cv2.imshow("IMAGEN AND", imagenAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("IMAGEN", imagen)
cv2.imshow("IMAGEN BINARIA", img)
cv2.imshow("IMAGEN OR", imagenOr)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("IMAGEN", imagen)
cv2.imshow("IMAGEN BINARIA", img)
cv2.imshow("IMAGEN XOR", imagenXor)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("IMAGEN", imagen)
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

