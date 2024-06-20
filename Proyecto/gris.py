import cv2
import numpy as np
from PIL import Image

arch="persona3.jpg"
ruta="C:\\Users\\naomi\\OneDrive\\Documentos\\Imagenes_Digitales\\Imagenes\\"+arch
imagen=cv2.imread(ruta)
alto, ancho, _=imagen.shape


imagen0=imagen.copy()
for i in range(alto):
    for j in range(ancho):
        for c in range(3):
            if imagen0[i, j, c] > 230:
                imagen0[i, j, :] == 0

cv2.imshow("xd", imagen0)
cv2.imshow("orignal", imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()
