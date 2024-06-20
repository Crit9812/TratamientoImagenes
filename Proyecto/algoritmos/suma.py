import numpy as np
from funciones import f

class sumar():
    
    def color(imagen, imagen2):
        alto, ancho,_=imagen.shape
        imagenOp1 = np.zeros((alto, ancho, 3), np.uint16)
        imagenOp2 = np.zeros((alto, ancho, 3), np.uint16)
        imagenOp3 = np.zeros((alto, ancho, 3), np.uint16)

        v1= imagen[:, :, :3].astype(int)
        v2= imagen2[:, :, :3].astype(int)

        #---------------truncar---------------------------------------
        nuevoV= np.minimum(v1+ v2, 255)
        imagenOp1[:, :, :3]= nuevoV

        #---------------ciclico---------------------------------------
        imagenOp2= np.mod(imagen+ imagen2, 256)

        #---------------escalar---------------------------------------
        arregloEsc=(v1+v2)
        minimo=np.min(arregloEsc)
        maximo=np.max(arregloEsc)
        nuevoV2 = np.interp(arregloEsc, (minimo, maximo), (0, 255)).astype(int)                
        imagenOp3[:, :, :3]= nuevoV2
        
        imagenOp1=f.conversion(imagenOp1)
        imagenOp2=f.conversion(imagenOp2)
        imagenOp3=f.conversion(imagenOp3)
        return imagenOp1, imagenOp2, imagenOp3
    
    def gris(imagen, imagen2):
        alto,ancho=imagen.shape
        
        imagenOp1 = np.zeros((alto, ancho), np.uint16)
        imagenOp2 = np.zeros((alto, ancho), np.uint16)
        imagenOp3 = np.zeros((alto, ancho), np.uint16)

        v1= imagen[:, :].astype(int)
        v2= imagen2[:, :].astype(int)

        #---------------truncar---------------------------------------
        nuevoV= np.minimum(v1+ v2, 255)
        imagenOp1[:, :]= nuevoV

        # ---------------ciclico---------------------------------------
        imagenOp2 = np.mod(imagen + imagen2, 256).astype(np.uint16)

        # ---------------escalar---------------------------------------
        arregloEsc=(v1+v2)
        minimo=np.min(arregloEsc)
        maximo=np.max(arregloEsc)
        nuevoV2 = np.interp(arregloEsc, (minimo, maximo), (0, 255)).astype(int)                
        imagenOp3[:, :]= nuevoV2
        
        imagenOp1=f.conversion(imagenOp1)
        imagenOp2=f.conversion(imagenOp2)
        imagenOp3=f.conversion(imagenOp3)
        return imagenOp1, imagenOp2, imagenOp3
    
    