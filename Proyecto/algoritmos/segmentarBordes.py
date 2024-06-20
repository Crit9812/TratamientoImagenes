
import numpy as np
from tkinter import simpledialog
from algoritmos.filtroMediana import mediana
from funciones import f
import cv2 
import matplotlib.pyplot as plt

class bordes(): 
  
  def obtenerRGB(imagen):
    
    I = imagen[:,:,:] 
    R = I[:,:,2]
    G = I[:,:,1]
    B = I[:,:,0]
    
    R=f.conversion(R)
    G=f.conversion(G)
    B=f.conversion(B)
    cv2.imshow("r",R.astype(np.uint8))
    cv2.imshow("G",G.astype(np.uint8))
    cv2.imshow("B",B.astype(np.uint8))
    cv2.waitKey()
    cv2.destroyAllWindows()
    I = imagen[:,:,[2,1,0]] 
    return R,G,B, I
  
  def segmentarRGB(R,G,B, I):

    Sr = (R>190) & (R<=255)
    Sg = (G>100) & (G<=255)
    Sb = (B<20) & (B>=0)
    #cv2.imshow("r",Sr.astype(np.uint8)*255)
    #cv2.imshow("G",(Sg.astype(np.uint8))*255,)
    cv2.imshow("B", (Sb.astype(np.uint8))*255)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    (N,M) = B.shape
    Q = B
    #buscar mínimos y máximos 
    imin = 1000
    imax = 0
    jmin = 1000
    jmax = 0
    for i in range(N):
      for j in range(M):
        if Q[i,j]>0:
          if i<imin:
            imin = i
          if i>imax:
            imax = i
          if j<jmin:
            jmin = j
          if j>jmax:
            jmax = j

    #Dibujar caja      
    y = [imin,imin,imax,imax,imin]
    x = [jmin,jmax,jmax,jmin,jmin]
    plt.imshow(cv2.cvtColor(I, cv2.COLOR_RGB2BGR))
    plt.plot(x,y)
    plt.show()
        

    Q=mediana.filtro(Q,1)
    #Q=filtroMedia(Q)

    #Detección de bordes
    E = np.zeros((N,M),np.uint8)
    for i in range(N):
      for j in range(1,M):
        if Q[i,j]!=Q[i,j-1]:
          E[i,j]   = 1
          E[i,j-1] = 1
    for i in range(1,N):
      for j in range(M):
        if Q[i-1,j]!=Q[i,j]:
          E[i,j]   = 1
          E[i,j-1] = 1

    for i in range(N):
      for j in range(M):
        if E[i,j]==1:
          imagen[i,j,:] = [255,0,0]
    
    img1=f.conversion(Q*255)
    img2=f.conversion(E*255)
    imagen=f.conversion(imagen)
    cv2.imshow("r",img1)
    cv2.imshow("G",(img2))
    cv2.imshow("B", (imagen))
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    
    return (Sr.astype(np.uint8))*255, (Sg.astype(np.uint8))*255, (Sb.astype(np.uint8))*255




  def segmentar(Sr,Sg,Sb, imagen):
    
    Srg = np.logical_and(Sr,Sg)
    S   = np.logical_and(Srg,Sb)
    (N,M) = S.shape
    Q = S

    Q=mediana.filtro(Q,1)
    #Q=filtroMedia(Q)

    #Detección de bordes
    E = np.zeros((N,M),np.uint8)
    for i in range(N):
      for j in range(1,M):
        if Q[i,j]!=Q[i,j-1]:
          E[i,j]   = 1
          E[i,j-1] = 1
    for i in range(1,N):
      for j in range(M):
        if Q[i-1,j]!=Q[i,j]:
          E[i,j]   = 1
          E[i,j-1] = 1

    for i in range(N):
      for j in range(M):
        if E[i,j]==1:
          imagen[i,j,:] = [255,0,0]
    
    img1=f.conversion(Q*255)
    img2=f.conversion(E*255)
    imagen=f.conversion(imagen)
    cv2.imshow("r",img1)
    cv2.imshow("G",(img2))
    cv2.imshow("B", (imagen))
    cv2.waitKey()
    cv2.destroyAllWindows()
    return img1, img2, imagen