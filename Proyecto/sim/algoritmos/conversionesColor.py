import cv2
import numpy as np

class Col():

    def BGRaRGB(imagenBGR):
        B=imagenBGR[:, :, 0]
        G=imagenBGR[:, :, 1]
        R=imagenBGR[:, :, 2]
        imagenRGB= np.dstack((R, G, B))
        return imagenRGB, R, G, B

    def BGRaHSV(imagenBGR): # cv2.COLOR_BGR2HSV
            B=imagenBGR[:, :, 0]
            G=imagenBGR[:, :, 1]
            R=imagenBGR[:, :, 2]
            imagenRGB= np.dstack((R, G, B))
            R_norm = R / 255.0
            G_norm = G / 255.0
            B_norm = B / 255.0
            
            Cmax = np.maximum(R_norm, np.maximum(G_norm, B_norm))
            Cmin = np.minimum(R_norm, np.minimum(G_norm, B_norm))
            delta = Cmax - Cmin

            V = Cmax

            # Añadir una pequeña cantidad epsilon para evitar la división por cero
            epsilon = 1e-10
            S = np.where(Cmax != 0, delta / (Cmax + epsilon), 0)

            H = np.zeros_like(S)

            mask_R = (Cmax == R_norm) & (delta != 0)
            mask_G = (Cmax == G_norm) & (delta != 0)
            mask_B = (Cmax == B_norm) & (delta != 0)

            H[mask_R] = 60 * ((G_norm[mask_R] - B_norm[mask_R]) / (delta[mask_R] + epsilon) % 6)
            H[mask_G] = 60 * ((B_norm[mask_G] - R_norm[mask_G]) / (delta[mask_G] + epsilon) + 2)
            H[mask_B] = 60 * ((R_norm[mask_B] - G_norm[mask_B]) / (delta[mask_B] + epsilon) + 4)

            # Normalizar H a un rango de 0 a 179 para el espacio de color HSV de OpenCV
            H_scaled = (H % 360) / 2 
            
            imagenHSV = np.dstack((H_scaled, S * 255, V * 255)).astype(np.uint8)
            
            return imagenHSV, H, S, V

    def BGRaCMYK(imagenBGR):
        B=imagenBGR[:, :, 0]
        G=imagenBGR[:, :, 1]
        R=imagenBGR[:, :, 2]
        imagenRGB= np.dstack((R, G, B))
        alto,ancho,_=imagenRGB.shape
        imagenCMYK=np.zeros((alto, ancho, 3), dtype=np.uint8)
        K_arr=[]
        for i in range (alto):
            for j in range (ancho):            
                R1=(imagenRGB[i, j, 0])/255.0
                G1=(imagenRGB[i, j, 1])/255.0
                B1=(imagenRGB[i, j, 2])/255.0
                K=(min(1-R1, 1-G1, 1-B1))
                K_arr.append(K)
                C=(1-R1-K)/(1-K)
                M=(1-G1-K)/(1-K)
                Y=(1-B1-K)/(1-K)
                imagenCMYK[i, j] = [C*255, M*255, Y*255]
        
        return imagenCMYK, K_arr, imagenCMYK[:,:,0], imagenCMYK[:,:,1], imagenCMYK[:,:,2]

    def RGBaBGR(imagenRGB):
        R=imagenRGB[:, :, 0]
        G=imagenRGB[:, :, 1]
        B=imagenRGB[:, :, 2]
        imagenBGR= np.dstack((B, G, R))
        return imagenBGR
            
    def HSVaBGR(imagenHSV):
        alto,ancho,_=imagenHSV.shape
        imagenRGB=np.zeros((alto, ancho, 3), dtype=np.uint8)
        for i in range (alto):
            for j in range (ancho):
                H=(imagenHSV[i, j, 0])
                S=(imagenHSV[i, j, 1])/255.0
                V=(imagenHSV[i, j, 2])/255.0
                C=V*S
                X=C*(1-abs(((H/60)%2)-1))
                m=V-C
                if 0<=H<60:
                    R1, G1, B1 = C, X, 0
                elif 60<=H<120:
                    R1, G1, B1 = X, C, 0
                elif 120<=H<180:
                    R1, G1, B1 = 0, C, X
                elif 180<=H<240:
                    R1, G1, B1 = 0, X, C
                elif 240<=H<300:
                    R1, G1, B1 = X, 0, C
                else:
                    R1, G1, B1 = C, 0, X
                R=(R1+m)*255
                G=(G1+m)*255
                B=(B1+m)*255
                imagenRGB[i, j] = [R, G, B]
                
        R=imagenRGB[:, :, 0]
        G=imagenRGB[:, :, 1]
        B=imagenRGB[:, :, 2]
        imagenBGR= np.dstack((B, G, R))
        return imagenBGR
        
    def CMYKaBGR(imagenCMYK, K_arr):
        alto,ancho,_=imagenCMYK.shape
        imagenRGB=np.zeros((alto, ancho, 3), dtype=np.uint8)
        ind=0
        for i in range (alto):
            for j in range (ancho):
                C=(imagenCMYK[i, j, 0])/255.0
                M=(imagenCMYK[i, j, 1])/255.0
                Y=(imagenCMYK[i, j, 2])/255.0
                K=K_arr[ind]
                K=(min(C, M, Y))
                R=255*(1-C)*(1-K)
                G=255*(1-M)*(1-K)
                B=255*(1-Y)*(1-K)
                R = max(0, min(R, 255))
                G = max(0, min(G, 255))
                B = max(0, min(B, 255))
                imagenRGB[i, j] = [R, G, B]
        
        R=imagenRGB[:, :, 0]
        G=imagenRGB[:, :, 1]
        B=imagenRGB[:, :, 2]
        imagenBGR= np.dstack((B, G, R))
        return imagenBGR


