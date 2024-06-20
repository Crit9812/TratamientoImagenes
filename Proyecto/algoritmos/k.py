
import cv2
import numpy as np
from tkinter import messagebox
from funciones import f

class k():
    
    def kmeansAlg(self,imagen):
        messagebox.showinfo("Mensaje","Agrega los atractores que desees en la imagen con el click. Presiona cualquier tecla para terminar ")
        self.imagen=imagen
        self.imagenOriginal=imagen.copy()

        self.centroides = []

        cv2.imshow("Imagen Original", self.imagenOriginal)
        cv2.setMouseCallback("Imagen Original", self.guardarDatosClick)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        imagenK=self.imagen.reshape((-1, 3)) #matriz[24000x3]

        #-----------------kmeans-----------------------

        k=len(self.centroides) 
        iteraciones=10 
        epsilon=1
        clases,centroides=self.kmeans(imagenK, self.centroides, iteraciones, epsilon)
        #print(clases)
        centroides=np.uint8(centroides)

        #--------------------asignar----------------------

        arregloColoresXPixel=centroides[clases.flatten()] #arreglo
        imagenSegmentada=arregloColoresXPixel.reshape(imagen.shape)

        imagenSegmentada=f.conversion(imagenSegmentada)
        return imagenSegmentada
    
    
    
    def kmeans(self,imagen, centroides, iteraciones, epsilon):
        for i in range(iteraciones):
            #    distancia euclidiana   dim. extra(2+1)               eje -> color
            distancias=np.linalg.norm(imagen [:, None] - centroides,    axis=2)
            #                             eje -> columnas(centorides)
            clases=np.argmin(distancias, axis=1)
            k=len(centroides)
            centroidesAct=np.array([imagen[clases==j].mean(axis=0) 
                                    for j in range(k)])

            #-----------cond---------------------------
            if np.linalg.norm(centroidesAct-centroides)<epsilon: break

            centroides = centroidesAct

        return clases, centroides

    def guardarDatosClick(self, event,x,y,flags,params):
        if event==cv2.EVENT_LBUTTONDOWN:
            self.centroides.append(self.imagen[x,y].tolist())
                    # imagen      centro  radio   color    grosor
            cv2.circle(self.imagenOriginal,(x,y),  3,   (255,0,0),  -1)
            cv2.imshow("Imagen Original", self.imagenOriginal)
            
    

