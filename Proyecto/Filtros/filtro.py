import cv2
import numpy as np
import statistics

imagen = cv2.imread("anny.png")
imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imagenRedi = cv2.resize(imagenGris, (500, 600))
imagenRediFil = cv2.resize(imagenGris, (500, 600))
alto, largo = imagenRediFil.shape

largoP=2
altoP=2
i=0
u=0
valores = []
contadorX=0
contadorY=0


while (i <= altoP and altoP < alto):
    while (u < largoP and largoP < largo):
        valores.append(imagenRediFil[i,u])
        u+=1
    if i==altoP:
        cambioY=i-1
        cambioX=u-1
        i-=2
        u-=1
        largoP+=1
        #mediana = statistics.median(valores)
        mediana = np.median(valores)
        #print(len(valores))
        valores.clear()
        #print(str(contadorY)+","+str(contadorX)+" "+str(mediana))
        contadorX+=1
        imagenRediFil[cambioY,cambioX]=mediana
        if largoP==largo:
            contadorY+=1
            u=0
            i=contadorY
            largoP=2
            altoP+=1
    elif u==largoP and i<altoP:
        print(i)
        u-=2
        i+=1
        

cv2.imshow("imagen", imagenRedi)
cv2.imshow("filtro",imagenRediFil)
cv2.waitKey(0)
cv2.destroyAllWindows()    

    


