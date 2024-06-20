import cv2
import numpy as np

# Leer la imagen
arch="amarilla.png"
ruta="C:\\Users\\naomi\\OneDrive\\Documentos\\Imagenes_Digitales\\Imagenes\\"+arch
imagen=cv2.imread(ruta)

#gris
imagenR= imagen[:, :, 0] 
imagenG= imagen[:, :, 1]
imagenB= imagen[:, :, 2] 
r=imagenR.astype(float)
g=imagenG.astype(float)
b=imagenB.astype(float)
v=[1/3,1/3,1/3]
im0=v[0]*r+v[1]*g+v[2]*b
imagen_gris=im0.astype(np.uint8)

#hsv

imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

#deteccion_azul
rango_bajo_azul = np.array([100, 150, 50])
rango_alto_azul = np.array([140, 255, 255])
mascara_azul = cv2.inRange(imagen_hsv, rango_bajo_azul, rango_alto_azul)
mascara_no_azul = cv2.bitwise_not(mascara_azul)

#unir la gris y lo azul
imagen_gris_bgr = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)
resultado_no_azul = cv2.bitwise_and(imagen_gris_bgr, imagen_gris_bgr, mask=mascara_no_azul)
resultado_azul = cv2.bitwise_and(imagen, imagen, mask=mascara_azul)
resultado_final = cv2.add(resultado_no_azul, resultado_azul)


cv2.imshow('Imagen Original', imagen)
cv2.imshow('Resultado', resultado_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
