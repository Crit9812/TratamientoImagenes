import cv2
import numpy as np

nombreImg="nina.jpg"
ruta="C:\\Users\\jessi\\Documents\\Universidad\\6to Semestre\\Procesamiento_imagenes\\Practicas\\Imagenes\\"+nombreImg
imagen=cv2.imread(ruta,cv2.IMREAD_GRAYSCALE)
imagen = cv2.resize(imagen, (500, 600))
#n=21
n=int(input("Ingresa el tamaño de la máscara: "))
if n%2==0: n=n+1
margen=n//2
print("El tamaño de l a matriz es ",n,"x",n)

alto,ancho=imagen.shape
pixelesImg=np.array(imagen)
nuevaImg=np.zeros((alto, ancho), dtype=np.uint8)

# ------------------------------para toda la imagen--------------------------------------------
for i in range(0,alto):
    for j in range(0,ancho):
        columna=max(0, i-margen)
        columnaFin=min(alto, i+margen+1)
        fila=max(0, j-margen)
        filaFin=min(ancho, j+margen+1)

        matriz=pixelesImg[columna:columnaFin, fila:filaFin]
        ordenado=np.sort(matriz)
        media=np.median(ordenado)
        nuevaImg[i, j]=int(media)


  
cv2.imshow("Imagen original",imagen.astype(np.uint8))
cv2.imshow("Imagen mediana",nuevaImg.astype(np.uint8))
cv2.waitKey()
cv2.destroyAllWindows()