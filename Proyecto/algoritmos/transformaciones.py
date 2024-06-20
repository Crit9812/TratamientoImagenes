
import numpy as np
from tkinter import simpledialog
import math
from funciones import f
from scipy.ndimage import affine_transform

class transf():
    
    def rotacion(imagen):
        angulo = simpledialog.askfloat("Rotacion", "Ingresa el valor del angulo al cual quieres rotar la imagen: ")
        alto, ancho = imagen.shape[:2]
        centroX = ancho // 2
        centroY = alto // 2
        anguloRad = math.radians(angulo)
        imagenRotada = np.zeros_like(imagen)

        for y in range(alto):
            for x in range(ancho):
                # Aplicar rotación inversa para encontrar los puntos originales en la imagen
                x_original = (x - centroX) * math.cos(-anguloRad) - (y - centroY) * math.sin(-anguloRad) + centroX
                y_original = (x - centroX) * math.sin(-anguloRad) + (y - centroY) * math.cos(-anguloRad) + centroY
                
                # Interpolación bilineal
                x0 = int(x_original)
                x1 = x0 + 1
                y0 = int(y_original)
                y1 = y0 + 1

                if 0 <= x0 < ancho-1 and 0 <= x1 < ancho and 0 <= y0 < alto-1 and 0 <= y1 < alto:
                    dx = x_original - x0
                    dy = y_original - y0
                    
                    # Valores de los pixeles vecinos
                    A = imagen[y0, x0]
                    B = imagen[y0, x1]
                    C = imagen[y1, x0]
                    D = imagen[y1, x1]

                    # Interpolación bilineal
                    pixel_interpolado = (A * (1 - dx) * (1 - dy)) + (B * dx * (1 - dy)) + (C * (1 - dx) * dy) + (D * dx * dy)

                    # Asignar el valor interpolado al píxel rotado
                    imagenRotada[y, x] = pixel_interpolado

        return imagenRotada
    
    def traslacion(imagen):
        
        dx=simpledialog.askinteger("Traslacion","Ingresa la coordenada en x para trasladar la imagen: ")
        dy=simpledialog.askinteger("Traslacion","Ingresa la coordenada en y para trasladar la imagen: ")
        alto, ancho = imagen.shape[:2]
        imagenTras = np.zeros_like(imagen)

        for y in range(alto):
            for x in range(ancho):
                nuevoX = x + dx
                nuevoY = y + dy
                if 0 <= nuevoX < ancho and 0 <= nuevoY < alto:
                    imagenTras[nuevoY, nuevoX] = imagen[y, x]
        
        imagenTras=f.conversion(imagenTras)
        return imagenTras
    
    
    def escalado(imagen):
        alto, ancho, n = imagen.shape

        nuevo_tam = simpledialog.askinteger("Escalado", "Ingresa el nuevo tamaño para redimensionar la imagen: ")

        if nuevo_tam is None:  # Verificar si el usuario canceló el diálogo
            return None

        # Calcular el factor de escala
        factor_escala = nuevo_tam / max(alto, ancho)

        # Calcular el nuevo tamaño para la imagen
        nuevo_alto = int(alto * factor_escala)
        nuevo_ancho = int(ancho * factor_escala)

        # Redimensionar la imagen utilizando interpolación
        imagen_redimensionada = np.zeros((nuevo_alto, nuevo_ancho, n), dtype=np.uint8)
        for y in range(nuevo_alto):
            for x in range(nuevo_ancho):
                pixelXOriginal = int(x / factor_escala)
                pixelYOriginal = int(y / factor_escala)
                pixelColor = imagen[pixelYOriginal, pixelXOriginal]
                imagen_redimensionada[y, x] = pixelColor

        return imagen_redimensionada
    
    def espejo(imagen):
        alto, ancho, _ =imagen.shape

        nuevaImg=np.zeros((alto,ancho,3), np.uint8)
        nuevaImg2=np.zeros((alto,ancho,3), np.uint8)

        for i in range (0,alto):
            for j in range (0,ancho):
                pix=imagen[i,j,:]
                nuevaImg[i,ancho-j-1,:]=pix
                
        for i in range (0,alto):
            for j in range (0,ancho):
                pix=imagen[i,j,:]
                nuevaImg2[alto-i-1,j,:]=pix
                
        nuevaImg=f.conversion(nuevaImg)  
        nuevaImg2=f.conversion(nuevaImg2)      
        return nuevaImg, nuevaImg2
    
    def shearH(imagen):
        alto, ancho, _ =imagen.shape
        nuevaImg=np.zeros_like(imagen)

        p=simpledialog.askstring("Nivel de desplazamiento","Ingresa el porcentaje que quieres aplicar de desplazamiento: ")
        p=float(p)
        p=p*0.01

        matrizH=np.float32([[1,p,0],
                            [0,1,0],
                            [0,0,1]])

        for i in range(0,alto):
            for j in range(0,ancho):
                                    #1                #p                #0
                #nuevoJ = int(matrizH[0, 0]*j + matrizH[0, 1]*i + matrizH[0, 2])
                nuevoJ = int(j+(p*i))
                                    #0               #1                 #0
                #nuevoI = int(matrizH[1, 0]*j + matrizH[1, 1]*i + matrizH[1, 2])
                nuevoI = int(i)

                if (0<=nuevoJ<ancho) and (0<=nuevoI<alto):
                    nuevaImg[nuevoI, nuevoJ] = imagen[i, j]
        
        nuevaImg=f.conversion(nuevaImg)            
        return nuevaImg
    
    def shearV(imagen):
        alto, ancho, _ =imagen.shape
        nuevaImg2=np.zeros_like(imagen)

        p=simpledialog.askstring("Nivel de desplazamiento","Ingresa el porcentaje que quieres aplicar de desplazamiento: ")
        p=float(p)
        p=p*0.01

        matrizV=np.float32([[1,0,0],
                            [p,1,0],
                            [0,0,1]])

        for i in range(0,alto):
            for j in range(0,ancho):
                
                nuevoJ2 = int(matrizV[0, 0]*j + matrizV[0, 1]*i + matrizV[0, 2])
                #nuevoJ2 = int(j)
                                    #p                 #1                 #0
                nuevoI2 = int(matrizV[1, 0]*j + matrizV[1, 1]*i + matrizV[1, 2])
                #nuevoI2 = int(i+(p*j))
                    
                if (0<=nuevoJ2<ancho) and (0<=nuevoI2<alto):
                    nuevaImg2[nuevoI2, nuevoJ2] = imagen[i, j]
         
        nuevaImg2=f.conversion(nuevaImg2)           
        return nuevaImg2