
import numpy as np
from funciones import f

class gris():
    
    def grisColor(imagen):

        imagenR= imagen[:, :, 0] 
        imagenG= imagen[:, :, 1]
        imagenB= imagen[:, :, 2] 

        r=imagenR.astype(float)
        g=imagenG.astype(float)
        b=imagenB.astype(float)

        #------------------promedio-------------------------------------

        v=[1/3,1/3,1/3]
        im0=v[0]*r+v[1]*g+v[2]*b
        img2=im0.astype(np.uint8)

        #---------------formula--------------------------------------------

        v=[0.2125,0.7154,0.0721]
        im=v[0]*r+v[1]*g+v[2]*b
        img1=im.astype(np.uint8)
        
        img1=f.conversion(img1)
        img2=f.conversion(img2)
        return img1, img2
