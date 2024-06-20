
import cv2
import numpy as np
from tkinter import simpledialog
from tkinter import messagebox
import os

class f(): 

    def dilatacionGris(imagen, tam_kernel):
        if len(imagen.shape) > 2:
            imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        tam_kernel += 1 if tam_kernel % 2 == 0 else 0
        ancho_relleno = tam_kernel // 2
        imagen_padded = np.pad(imagen, pad_width=ancho_relleno, mode='edge')
        alto, ancho = imagen.shape
        imagen_dilatada = np.zeros_like(imagen)

        for i in range(alto):
            for j in range(ancho):
                vecindario = imagen_padded[i:i+tam_kernel, j:j+tam_kernel]
                imagen_dilatada[i, j] = np.max(vecindario)

        return imagen_dilatada

    def dilatacionRGB(imagen, tam_kernel):
        if tam_kernel % 2 == 0: 
            tam_kernel += 1
        
        ancho_relleno = tam_kernel // 2
        alto, ancho, canales = imagen.shape
        
        # Rellenar la imagen para manejar los bordes
        imagen_padded = np.pad(imagen, pad_width=((ancho_relleno, ancho_relleno), (ancho_relleno, ancho_relleno), (0, 0)), mode='edge')
        
        imagen_dilatada = np.zeros_like(imagen)
        
        for i in range(alto):
            for j in range(ancho):
                for c in range(canales):
                    # Obtener la región del vecindario
                    vecindario = imagen_padded[i:i+tam_kernel, j:j+tam_kernel, c]
                    imagen_dilatada[i, j, c] = np.max(vecindario)
        
        return imagen_dilatada
        
    def erosionGris(imagen, tam_kernel):
        if len(imagen.shape) > 2:
            imagen = imagen.mean(axis=2).astype(np.uint8)

        tam_kernel += 1 if tam_kernel % 2 == 0 else 0
        ancho_relleno = tam_kernel // 2
        imagen_padded = np.pad(imagen, pad_width=ancho_relleno, mode='edge')
        alto, ancho = imagen.shape
        imagen_erosionada = np.zeros_like(imagen)

        for i in range(alto):
            for j in range(ancho):
                vecindario = imagen_padded[i:i+tam_kernel, j:j+tam_kernel]
                imagen_erosionada[i, j] = np.min(vecindario)

        return imagen_erosionada

    def erosionRGB(imagen, tam_kernel):
        if tam_kernel % 2 == 0: 
            tam_kernel += 1
        
        ancho_relleno = tam_kernel // 2
        alto, ancho, canales = imagen.shape
        
        # Rellenar la imagen para manejar los bordes
        imagen_padded = np.pad(imagen, pad_width=((ancho_relleno, ancho_relleno), (ancho_relleno, ancho_relleno), (0, 0)), mode='edge')
        
        imagen_erosionada = np.zeros_like(imagen)
        
        for i in range(alto):
            for j in range(ancho):
                for c in range(canales):
                    # Obtener la región del vecindario
                    vecindario = imagen_padded[i:i+tam_kernel, j:j+tam_kernel, c]
                    imagen_erosionada[i, j, c] = np.min(vecindario)
        
        return imagen_erosionada

    def modificarImg(image, angle, scale):
        # Obtener dimensiones de la imagen
        (h, w) = image.shape[:2]
        # Obtener el centro de la imagen
        center = (w // 2, h // 2)
        # Calcular la matriz de rotación
        M = cv2.getRotationMatrix2D(center, angle, scale)
        # Aplicar la matriz de rotación
        rotated_image = cv2.warpAffine(image, M, (w, h))
        return rotated_image
    
    def medidasColor(imagen):
        imagenOp=imagen.copy()
        alto, ancho, nv = imagen.shape
        # Creación de imagen binaria
        img = np.ones((alto, ancho, nv), dtype=np.uint8) * 0
        # Definir coordenadas del rectángulo en el centro
        x1 = ancho // 2 - 100
        y1 = alto // 2 - 100
        x2 = ancho // 2 + 100
        y2 = alto // 2 + 100
        
        return imagenOp, img, x1, y1, x2,y2,alto,ancho
    
    def guardarImagen(imagen):
        nombre=simpledialog.askstring("Guardar imágen","Si deseas guardar la imagen escribe el nombre: ")
        ruta="C:\\Users\\jessi\\Documents\\Universidad\\6to Semestre\\Procesamiento_imagenes\\Practicas\\Interfaz_Prev\\Imagenes_usuario\\"
        if nombre!="":
            nombreImg=nombre+".jpg"
            ruta+=nombreImg
            cv2.imwrite(ruta, imagen)
            messagebox.showinfo("Mensaje","La imagen ha sido guardada en la carpeta imagenes_usuario")
        
    def crearImgBinaria():
        imagen = np.zeros((600, 600), dtype=np.uint8)
        color = 255

        # largo
        imagen[85:485, 300:315] = color
        imagen[275:545, 285:300] = color
        imagen[425:440, 250:345] = color #b
        imagen[410:425, 220:360] = color
        imagen[395:410, 160:390] = color #p
        imagen[365:395, 145:405] = color
        imagen[335:365, 130:405] = color
        imagen[320:335, 160:390] = color
        imagen[305:320, 190:375] = color
        imagen[290:305, 220:360] = color
        imagen[275:290, 250:345] = color
        #pata
        imagen[470:515, 315:330] = color
        imagen[500:545, 330:345] = color
        imagen[530:545, 345:360] = color
        # pico
        imagen[115:130, 240:495] = color
        imagen[70:160, 285:300] = color
        imagen[85:145, 270:285] = color
        imagen[85:145, 255:270] = color
        

        return imagen
    
    def redimensionar(imagen, imagen2):
        if len(imagen.shape) == 3:
            alto1,ancho1,_=imagen.shape
            alto2,ancho2,_=imagen2.shape
        else:
            alto1,ancho1=imagen.shape
            alto2,ancho2=imagen2.shape
        size1=alto1*ancho1
        size2=alto2*ancho2
        if size1<size2:
            imagen2=cv2.resize(imagen2, (ancho1, alto1))
        elif size2<size1:
            imagen=cv2.resize(imagen, (ancho2, alto2))

        return imagen, imagen2
    
    def calcularDatos(imagen_n):
        #hacer array de colores - histograma-
        alto, ancho=imagen_n.shape
        frecuenciaColores=[[i,0]for i in range(256)]
            
        for i in range(0,alto):
            for j in range(0,ancho):
                valor=imagen_n[i,j]
                frecuenciaColores[valor][1]+=1
                
        return frecuenciaColores
    
    def filtro_gaussiano(imagen, tamano_kernel):
        kernel = cv2.getGaussianKernel(tamano_kernel, .5)
        imagen_filtrada = cv2.filter2D(imagen, -1, kernel * kernel.T)
        return imagen_filtrada
    
    def conversion(imagen):
        imagen=imagen.astype(np.uint8)
        return imagen

    def medidas(imagen):
        imagenOp=imagen.copy()
        alto, ancho = imagen.shape
        # Creación de imagen binaria
        img = np.ones((alto, ancho), dtype=np.uint8) * 0
        # Definir coordenadas del rectángulo en el centro
        x1 = ancho // 2 - 100
        y1 = alto // 2 - 100
        x2 = ancho // 2 + 100
        y2 = alto // 2 + 100
        
        return imagenOp, img, x1, y1, x2, y2, alto, ancho
    
    def getMean(array, i):
        arreglo1=array[:i]
        arreglo2=array[i:]
        suma=sum(arreglo1)
        suma2=sum(arreglo2)
        if suma==0:
            mediana1=0
        else:
            p1=0
            for n in range(len(arreglo1)):
                p1+=arreglo1[n]*n
            mediana1=p1/suma

        if suma2==0:
            mediana2=0
        else:
            p2=0
            for n in range(len(arreglo2)):
                p2+=arreglo2[n]*n
            mediana2=p2/suma2

        return mediana1, mediana2

    def getVarianza(array, i, m1, m2):
        arreglo1=array[:i]
        arreglo2=array[i:]
        suma=sum(arreglo1)
        suma2=sum(arreglo2)
        if suma==0:
            varianza1=0
        else:
            p1=0
            for n in range(len(arreglo1)):
                p1+=((arreglo1[n]-m1)**2)*n
            varianza1=p1/suma

        if suma2==0:
            varianza2=0
        else:
            p2=0
            for n in range(len(arreglo2)):
                p2+=((arreglo2[n]-m2)**2)*n
            varianza2=p2/suma2

        return varianza1, varianza2 

    def getPeso(array,i, sumaT):
        suma=sum(array[:i])
        suma2=sum(array[i:])
        weight=suma/sumaT
        weight2=suma2/sumaT
        return weight, weight2
    
    def deteccion_bordes_laplaciano(imagen):
        kernel_laplaciano = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
        imagen_filtrada_laplaciano = cv2.filter2D(imagen, -1, kernel_laplaciano)
        return imagen_filtrada_laplaciano
    
    def guardarImagen(imagen):
        nombre = simpledialog.askstring("Guardar imagen", "Si deseas guardar la imagen, escribe el nombre:")

        if nombre is not None and nombre.strip() != "":
            ruta = os.getcwd()
            ruta = os.path.join(ruta, "Imagenes_usuario")  
            nombreImg = nombre + ".jpg"
            ruta = os.path.join(ruta, nombreImg)
            cv2.imwrite(ruta, imagen)
            messagebox.showinfo("Mensaje", "La imagen ha sido guardada en la carpeta Imagenes_usuario")
