
import cv2
from algoritmos.umbralBasico import umbrales
from funciones import f

class otsuB():
    
    def inicio(imagen):
        alto,ancho,_=imagen.shape
        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        arrayX=f.calcularDatos(imagen_gris)
        array=[par[1] for par in arrayX]
        suma=sum(array)
        datosVarianza=[]

        for i in range(256):
            weightB, weightF=f.getPeso(array,i,suma)
            meanB, meanF=f.getMean(array,i)
            varianceB, varianceF=f.getVarianza(array,i, meanB, meanF)
            
            varianzaClase=(weightB*varianceB)+(weightF*varianceF)
            datosVarianza.append(varianzaClase)
            
        minimo=min(datosVarianza)
        nivel=datosVarianza.index(minimo)

        imagenUmbral=umbrales.umbralBasico(nivel, imagen_gris, alto, ancho)
        
        imagenUmbral=f.conversion(imagenUmbral)
        return nivel, imagenUmbral



    


