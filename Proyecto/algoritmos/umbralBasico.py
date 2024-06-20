
from funciones import f
from tkinter import messagebox

class umbrales():
    
    def umbralBasico(nivel,imagen, alto, ancho):
        imagen0=imagen.copy()
        cont=0
        for i in range(0,alto):
            for j in range (0,ancho):
                if imagen0[i,j] >= nivel:
                    imagen0[i,j]=255
                else:
                    imagen0[i,j]=0
                    cont=cont+1
        msj="area: ",cont," px"
        messagebox.showinfo("Mensaje",msj)
        return imagen0

    def umbralInvertido(nivel,imagen, alto, ancho):
        for i in range(0,alto):
            for j in range (0,ancho):
                if imagen[i,j] >= nivel:
                    imagen[i,j]=0
                else:
                    imagen[i,j]=255
        return imagen

    def umbralNivel(nivel, imagen, alto, ancho):
        imagen0=imagen.copy()
        for i in range(alto):
            for j in range(ancho):
                for c in range(3):
                    if imagen0[i, j, c] < nivel:
                        imagen0[i, j, :] = 0

        return imagen0

    def umbralNivelInvertido(nivel,imagen,alto, ancho):
        for p in range (0, 3):
            for i in range(0,alto):
                for j in range (0,ancho):
                    if imagen[i,j,p] < nivel:
                        imagen[i,j,:]=255
        return imagen

    def umbralNivelG(nivel, imagen, alto, ancho):
        imagen0=imagen.copy()
        for i in range(alto):
            for j in range(ancho):
                if imagen0[i, j] < nivel:
                    imagen0[i, j] = 0

        return imagen0

    def umbralNivelInvertidoG(nivel,imagen,alto, ancho):
        for i in range(0,alto):
            for j in range (0,ancho):
                if imagen[i,j] < nivel:
                    imagen[i,j]=255
        return imagen

    def umbral2(nivel, nivel2, imagen, alto, ancho):
        imagen0=imagen.copy()
        for i in range(0,alto):
            for j in range (0,ancho):
                if imagen0[i,j] < nivel or imagen0[i,j] > nivel2 :
                    imagen0[i,j]=0
                else: imagen0[i,j]=255
        return imagen0

    def umbral2Invertido(nivel, nivel2, imagen, alto, ancho):
        for i in range(0,alto):
            for j in range (0,ancho):
                if imagen[i,j] < nivel or imagen[i,j] > nivel2 :
                    imagen[i,j]=255
                else: imagen[i,j]=0
        return imagen

    def umbral2C(nivel, nivel2, imagen, alto, ancho):
        imagen0=imagen.copy()
        for i in range(alto):
            for j in range(ancho):
                pixel=imagen0[i, j]
                promedio=(int(pixel[0]) + int(pixel[1]) + int(pixel[2]))/3
                if promedio < nivel or promedio > nivel2:
                    imagen0[i, j]=[0,0,0] 
                else: imagen0[i,j]=[255,255,255]

        return imagen0

    def umbral2InvertidoC(nivel, nivel2, imagen, alto, ancho):
        #for p in range (0, 3):
        for i in range(0,alto):
                for j in range (0,ancho):
                    pixel = imagen[i, j]
                    promedio = (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3
                    if promedio < nivel or promedio > nivel2:
                        imagen[i, j] = [255,255,255]
                    else: imagen[i,j]=[0,0,0] 
        return imagen



