import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from algoritmos.morfologicas2 import morf2
from algoritmos.transformada import Houhg
from algoritmos.esqueletos import esq
from algoritmos.hu import Momentos
from algoritmos.hatss import Hats
from algoritmos.rellenoBordes import RellenoImagen
from algoritmos.esqueletos2 import Esqueletizador
from Metodos.Seleccionar import seleccion
from algoritmos.k import k
from algoritmos.filtroMedia import media
from algoritmos.filtroMediana import mediana
from algoritmos.logicasC import logColor
from algoritmos.logicasG import logGris
from algoritmos.umbralBasico import umbrales
from algoritmos.otsu import otsuB
from algoritmos.detectarBordes import detectar
from algoritmos.transformaciones import transf
from Histograma import hist
from tkinter import messagebox
from tkinter import simpledialog
from funciones import f
import cv2

class panelMMK:
    arregloI=[]

    def sel(self):
        self.textoOriginal.config(text="Original")
        selec = seleccion()
        imagenn = selec.evento_seleccionar()
        imagen = Image.open(imagenn)
        self.imagen00 = cv2.imread(imagenn)
        self.imagen0 = self.imagen00.copy()
        self.linkImagen.insert(0, imagenn)

        if self.identificador == 1:
            imagen = cv2.cvtColor(self.imagen00, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (400, 400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil1)
            self.original.configure(image=self.imagen_tk)

        elif self.identificador == 2:
            imagen = cv2.cvtColor(self.imagen00, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (400, 400))
            _, imagen = cv2.threshold(imagen, 200, 255, cv2.THRESH_BINARY)
            imagen_pil1 = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil1)
            self.original.configure(image=self.imagen_tk)

        else:
            imagen = imagen.resize((400, 400))
            self.imagen_tk = ImageTk.PhotoImage(imagen)
            self.original.configure(image=self.imagen_tk)
            self.linkImagen.insert(0, imagenn)

    def selR(self):
        self.textoOriginal.config(text="Original")
        imagen = Image.open(self.linkImagen.get())
        self.imagen00 = cv2.imread(self.linkImagen.get())
        self.imagen0=self.imagen00.copy()

        if self.identificador == 1:
            imagen = cv2.cvtColor(self.imagen00, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (400, 400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil1)
            self.original.configure(image=self.imagen_tk)

        elif self.identificador == 2:
            imagen = cv2.cvtColor(self.imagen00, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (400, 400))
            _, imagen = cv2.threshold(imagen, 200, 255, cv2.THRESH_BINARY)
            imagen_pil1 = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil1)
            self.original.configure(image=self.imagen_tk)

        else:
            imagen = imagen.resize((400, 400))
            self.imagen_tk = ImageTk.PhotoImage(imagen)
            self.original.configure(image=self.imagen_tk)

    def transf(self):
        self.arregloI.clear()
        img1=transf.rotacion(self.imagen0)
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        img2=transf.traslacion(img1)
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        img33=transf.escalado(img2)
        img3 = cv2.resize(img33,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        
        self.arregloI.append(img33)
    
    def mediaF(self):
        self.arregloI.clear()
        img11=media.filtro(self.imagen0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)

        self.arregloI.append(img11)
    
    def medianaF(self):
        self.arregloI.clear()
        img11=mediana.filtro(self.imagen0,0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        self.arregloI.append(img11)

    def kmeansS(self):
        self.arregloI.clear()
        instancia_k = k()
        img11 = instancia_k.kmeansAlg(self.imagen0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        self.arregloI.append(img11)

    def imagenD (self):
        if self.identificador== 1: #gris
            self.arregloI.clear()
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            tam = simpledialog.askinteger("Tamaño Dilatación", "Ingrese el tamaño de la dilatación en pixeles:")
            img11=f.dilatacionGris(imagen, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)


        if self.identificador== 3: # color
            self.arregloI.clear()
            #imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            tam = simpledialog.askinteger("Tamaño Dilatación", "Ingrese el tamaño de la dilatación en pixeles:")
            img11=f.dilatacionRGB(self.imagen0, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)
        
    def imagenE (self):
        if self.identificador== 1: #gris
            self.arregloI.clear()
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            tam = simpledialog.askinteger("Tamaño Erosión", "Ingrese el tamaño de la erosión en pixeles:")
            img11=f.erosionGris(imagen, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)


        if self.identificador== 3: # color
            self.arregloI.clear()
            #imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            tam = simpledialog.askinteger("Tamaño Erosión", "Ingrese el tamaño de la erosión en pixeles:")
            img11=f.erosionRGB(self.imagen0, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)

    def imagenOTSU (self):
        self.arregloI.clear()
        nivel, img11=otsuB.inicio(self.imagen0)
        s=str(nivel)
        messagebox.showinfo("Mensaje","El nivel de umbralizacion es: "+s)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        self.arregloI.append(img11)

    def imagenHough (self):
        self.arregloI.clear()
        img2=self.imagen0
        img11=Houhg.transformar(img2)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)
        
    def imagenCanny (self):
        self.arregloI.clear()
        img11=detectar.canny(self.imagen0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        self.arregloI.append(img11)

    def imagenSobel (self):
        self.arregloI.clear()
        img11, img22=detectar.sobel(self.imagen0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.original.configure(image=self.imagen_tk1)

        img2 = cv2.resize(img22,(400,400))
        imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

        self.truncamiento.configure(image=self.imagen_tk2)

        self.textoOriginal.config(text="Gradiente en X")
        self.textoTruncamiento.config(text="Gradiente en Y")

        self.arregloI.append(img11)
        self.arregloI.append(img22)

    def imagenPrewitt (self):
        self.arregloI.clear()
        img11, img22=detectar.prewitt(self.imagen0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.original.configure(image=self.imagen_tk1)

        img2 = cv2.resize(img22,(400,400))
        imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

        self.truncamiento.configure(image=self.imagen_tk2)
        
        self.textoOriginal.config(text="Gradiente en X")
        self.textoTruncamiento.config(text="Gradiente en Y")
        self.arregloI.append(img11)
        self.arregloI.append(img22)

    def imagenGauss (self):
        self.arregloI.clear()
        img11=detectar.gauss(self.imagen0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        self.arregloI.append(img11)

    def imagenShearV (self):
        self.arregloI.clear()
        img11=transf.shearV(self.imagen0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        self.arregloI.append(img11)

    def imagenShearH (self):
        self.arregloI.clear()
        img11=transf.shearH(self.imagen0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        self.arregloI.append(img11)

    def imagenUmbralB (self):
        self.arregloI.clear()
        if self.identificador== 1:
            imagen=cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            imgH1=hist.gris(imagen)

            img1 = cv2.resize(imagen,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

            self.original.configure(image=self.imagen_tk1)

            img2 = cv2.resize(imgH1,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoTruncamiento.config(text="Histograma")

            #mostrar imagen e hist
            nivelG=simpledialog.askinteger("Nivel para el umbral","Ingresa el valor del nivel para la imagen en gris: ")
            alto,ancho=imagen.shape
            
            imagenUmbral=umbrales.umbralBasico(nivelG, imagen, alto, ancho)
            imagenUmbralInv=umbrales.umbralInvertido(nivelG, imagen, alto, ancho)

            img1 = cv2.resize(imagenUmbral,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

            self.original.configure(image=self.imagen_tk1)

            img2 = cv2.resize(imagenUmbralInv,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoOriginal.config(text="Umbral basico")
            self.textoTruncamiento.config(text="Umbral basico invertido")
            self.arregloI.append(imagenUmbral)
            self.arregloI.append(imagenUmbralInv)
        if self.identificador== 3:
            imgH=hist.color(self.imagen0)

            img2 = cv2.resize(imgH,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoTruncamiento.config(text="Histograma")
            #mostrar img  e hist
            self.nivelG=simpledialog.askinteger("Nivel para el umbral","Ingresa el valor del nivel para la imagen a color: ")
            
            self.red=self.imagen0[:,:,0]
            self.green=self.imagen0[:,:,1]
            self.blue=self.imagen0[:,:,2]
            self.alto,self.ancho,_=self.imagen0.shape
            
            imagenUmbral=umbrales.umbralBasico(self.nivelG, self.red, self.alto, self.ancho)
            imagenUmbralInv=umbrales.umbralInvertido(self.nivelG, self.red, self.alto, self.ancho)
            img1 = cv2.resize(imagenUmbral,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

            self.original.configure(image=self.imagen_tk1)

            img2 = cv2.resize(imagenUmbralInv,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoOriginal.config(text="Umbral basico rojo")
            self.textoTruncamiento.config(text="Umbral basico invertido rojo")
            self.arregloI.append(imagenUmbral)
            self.arregloI.append(imagenUmbralInv)
            
    def imagenUmbralPN (self):
        self.arregloI.clear()
        if self.identificador== 1:
            imagen=cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            imgH=hist.gris(imagen)
            img2 = cv2.resize(imgH,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoTruncamiento.config(text="Histograma")
            #m
            nivelC=simpledialog.askinteger("Nivel para el umbral","Ingresa el valor del nivel para la imagen en gris: ")
            alto,ancho=imagen.shape
            imagenUmbral=umbrales.umbralNivelG(nivelC, imagen, alto, ancho)
            imagenUmbralInv=umbrales.umbralNivelInvertidoG(nivelC, imagen, alto, ancho)
            img1 = cv2.resize(imagenUmbral,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

            self.original.configure(image=self.imagen_tk1)

            img2 = cv2.resize(imagenUmbralInv,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoOriginal.config(text="Umbral por nivel")
            self.textoTruncamiento.config(text="Umbral por nivel invertido")
            self.arregloI.append(imagenUmbral)
            self.arregloI.append(imagenUmbralInv)
        if self.identificador== 3:
            imgH=hist.color(self.imagen0)
            img2 = cv2.resize(imgH,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoTruncamiento.config(text="Histograma")
            #m
            nivelC=simpledialog.askinteger("Nivel para el umbral","Ingresa el valor del nivel para la imagen a color: ")
            alto,ancho,_=self.imagen0.shape
            imagenUmbral=umbrales.umbralNivel(nivelC, self.imagen0, alto, ancho)
            imagenUmbralInv=umbrales.umbralNivelInvertido(nivelC, self.imagen0, alto, ancho)
            img1 = cv2.resize(imagenUmbral,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

            self.original.configure(image=self.imagen_tk1)

            img2 = cv2.resize(imagenUmbralInv,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoOriginal.config(text="Umbral por nivel")
            self.textoTruncamiento.config(text="Umbral por nivel invertido")
            self.arregloI.append(imagenUmbral)
            self.arregloI.append(imagenUmbralInv)
    
    def imagenUmbral2P (self):
        self.arregloI.clear()
        if self.identificador== 1:
            imagen=cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            imgH=hist.gris(imagen)
            img2 = cv2.resize(imgH,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoTruncamiento.config(text="Histograma")
            #m
            nivelG1=simpledialog.askinteger("Nivel para el umbral","Ingresa el valor del primer nivel para la imagen en gris: ")
            nivelG2=simpledialog.askinteger("Nivel para el umbral","Ingresa el valor del segundo nivel para la imagen en gris: ")
            alto,ancho=imagen.shape
            imagenUmbral=umbrales.umbral2(nivelG1, nivelG2, imagen, alto, ancho)
            imagenUmbralInv=umbrales.umbral2Invertido(nivelG1, nivelG2, imagen, alto, ancho)
            img1 = cv2.resize(imagenUmbral,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

            self.original.configure(image=self.imagen_tk1)

            img2 = cv2.resize(imagenUmbralInv,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoOriginal.config(text="Umbral 2 puntos")
            self.textoTruncamiento.config(text="Umbral 2 puntos invertido")
            self.arregloI.append(imagenUmbral)
            self.arregloI.append(imagenUmbralInv)
        if self.identificador== 3:
            imgH=hist.color(self.imagen0)
            imgH=hist.color(self.imagen0)
            img2 = cv2.resize(imgH,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoTruncamiento.config(text="Histograma")
            #m
            nivelC1=simpledialog.askinteger("Nivel para el umbral","Ingresa el valor del primer nivel para la imagen a color: ")
            nivelC2=simpledialog.askinteger("Nivel para el umbral","Ingresa el valor del segundo nivel para la imagen a color: ")
            alto,ancho,_=self.imagen0.shape
            imagenUmbral=umbrales.umbral2C(nivelC1, nivelC2, self.imagen0, alto, ancho)
            imagenUmbralInv=umbrales.umbral2InvertidoC(nivelC1, nivelC2, self.imagen0, alto, ancho)
            img1 = cv2.resize(imagenUmbral,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

            self.original.configure(image=self.imagen_tk1)

            img2 = cv2.resize(imagenUmbralInv,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoOriginal.config(text="Umbral 2 puntos")
            self.textoTruncamiento.config(text="Umbral 2 puntos invertido")
            self.arregloI.append(imagenUmbral)
            self.arregloI.append(imagenUmbralInv)

    def imagenNOT (self):
        self.arregloI.clear()
        if self.identificador== 1:             
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            img11=logGris.nott(imagen)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 2:
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            _, imagen = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)
            img11=logGris.nott(imagen)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 3:
            img11=logColor.nott(self.imagen0)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)
        self.truncamiento.configure(image=self.imagen_tk1)

    def imagenNegativo (self):
        self.arregloI.clear()
        if self.identificador== 1:             
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            img11=logGris.nott(imagen)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 2:
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            _, imagen = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)
            img11=logGris.nott(imagen)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 3:
            img11=logColor.nott(self.imagen0)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)
        self.truncamiento.configure(image=self.imagen_tk1)

    def imagenHistogramas (self):
        self.arregloI.clear()
        if self.identificador== 1:
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            img11=hist.gris(imagen)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 3:
            img11=hist.color(self.imagen0)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)
        self.truncamiento.configure(image=self.imagen_tk1)

    def apertura(self):
        if self.identificador== 1:
            self.arregloI.clear()
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.aperturaRGB(self.imagen0, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)
        if self.identificador== 3:
            self.arregloI.clear()
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.aperturaRGB(self.imagen0, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)

    def clausura(self):
        if self.identificador== 1:
            self.arregloI.clear()
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.clausuraGris(imagen, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 3:
            self.arregloI.clear()
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.clausuraRGB(self.imagen0, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)

    def gradiente(self):
        if self.identificador== 1:
            self.arregloI.clear()
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.gradienteGris(self.imagen0, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 3:
            self.arregloI.clear()
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.gradienteRGB(self.imagen0, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)

    def perimetro(self):
        if self.identificador== 1:
            self.arregloI.clear()
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.perimetroGris(self.imagen0, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 3:
            self.arregloI.clear()
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.perimetroRGB(self.imagen0, tam)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)

    def relleno(self):
        
        self.arregloI.clear()
        inst = RellenoImagen()
        img11 = inst.rellenar(self.imagen0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

        self.truncamiento.configure(image=self.imagen_tk1)
        self.arregloI.append(img11)
    def esqueleto(self):
        self.arregloI.clear()
        tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
        img11=esq.esqueletizar(self.imagen0, tam)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)

    def esqueleto2(self):
        self.arregloI.clear()
        img11=Esqueletizador.go(self.imagen0)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)

    def topHat(self):
        self.arregloI.clear()
        tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
        img11=Hats.topHat(self.imagen0, tam)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)

    def blackHat(self):
        self.arregloI.clear()
        tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
        img11=Hats.blackHat(self.imagen0, tam)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        self.arregloI.append(img11)

        self.truncamiento.configure(image=self.imagen_tk1)

    def momentos(self):
        self.arregloI.clear()
        img11=f.modificarImg(self.imagen0, 45, 1.5)

        phi_1, phi_2, phi_3, phi_4, phi_5, phi_6, phi_7 = Momentos.huM(self.imagen0)
        texto="IMAGEN1: "
        texto += "\nMomento de Hu 1: " + str(phi_1)
        texto += "\nMomento de Hu 2: " + str(phi_2)
        texto += "\nMomento de Hu 3: " + str(phi_3)
        texto += "\nMomento de Hu 4: " + str(phi_4)
        texto += "\nMomento de Hu 5: " + str(phi_5)
        texto += "\nMomento de Hu 6: " + str(phi_6)
        texto += "\nMomento de Hu 7: " + str(phi_7)
        texto+="\n\nIMAGEN2: "

        phi_1, phi_2, phi_3, phi_4, phi_5, phi_6, phi_7 = Momentos.huM(img11)
        texto += "\nMomento de Hu 1: " + str(phi_1)
        texto += "\nMomento de Hu 2: " + str(phi_2)
        texto += "\nMomento de Hu 3: " + str(phi_3)
        texto += "\nMomento de Hu 4: " + str(phi_4)
        texto += "\nMomento de Hu 5: " + str(phi_5)
        texto += "\nMomento de Hu 6: " + str(phi_6)
        texto += "\nMomento de Hu 7: " + str(phi_7)
        img1 = cv2.resize(img11,(400,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        self.arregloI.append(img11)
        

        self.truncamiento.configure(image=self.imagen_tk1)
        messagebox.showinfo("Mensaje", texto)

    def siguientee(self):
        contador =1
        if contador == 1:
            contador = contador + 1
            imagenUmbral=umbrales.umbralBasico(self.nivelG, self.green, self.alto, self.ancho)
            imagenUmbralInv=umbrales.umbralInvertido(self.nivelG, self.green, self.alto, self.ancho)
            img1 = cv2.resize(imagenUmbral,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

            self.original.configure(image=self.imagen_tk1)

            img2 = cv2.resize(imagenUmbralInv,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoOriginal.config(text="Umbral basico verde")
            self.textoTruncamiento.config(text="Umbral basico invertido verde")
        if contador ==2:
            imagenUmbral=umbrales.umbralBasico(self.nivelG, self.blue, self.alto, self.ancho)
            imagenUmbralInv=umbrales.umbralInvertido(self.nivelG, self.blue, self.alto, self.ancho)
            img1 = cv2.resize(imagenUmbral,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

            self.original.configure(image=self.imagen_tk1)

            img2 = cv2.resize(imagenUmbralInv,(400,400))
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

            self.truncamiento.configure(image=self.imagen_tk2)

            self.textoOriginal.config(text="Umbral basico azul")
            self.textoTruncamiento.config(text="Umbral basico invertido azul")
            #m

    def siguienteMoment(self):
        print("jajaja")

    def guarda(self):
        for imagen in self.arregloI:
            f.guardarImagen(imagen)
    
    def crearPanel1(self, ventana,menu_lateral,operacion,identificador):
        self.identificador=identificador
        self.panel = tk.Frame(ventana, borderwidth=2, bg="#F9E1E0",relief="solid")
        self.panel.place(x=200, y=0,width=1000, height=699)

                
        self.original=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.original.place(x=50, y=150, width=400, height=400)

        self.truncamiento=tk.Label(self.panel, text="Imagen 2", borderwidth=2, relief="solid", highlightbackground="black")
        self.truncamiento.place(x=500, y=150,width=400, height=400)
        
        self.linkImagen=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
        self.linkImagen.place(x=50, y=600, width=450, height=30)

        self.buscarR = tk.Button(self.panel, text="->", command=self.selR, bg="#E39EDB")
        self.buscarR.place(x=505, y=600 , width=30, height=30)
        
        self.buscar = tk.Button(self.panel, text="BUSCAR", command=self.sel, bg="#E39EDB")
        self.buscar.place(x=540, y=600 , width=100, height=30)

        self.guardar = tk.Button(self.panel, text="Guardar", command=self.guarda, bg="#E39EDB")
        self.guardar.place(x=650, y=600 , width=100, height=30)

#-----------------------------Transformaciones 2.0------------------------------------
        if operacion == 10:
            self.textoTitulo=tk.Label(self.panel, text="Transformaciones 2.0", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Transformada",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.transf, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#---------------------------------Media----------------------------------------------
        if operacion == 25:
            self.textoTitulo=tk.Label(self.panel, text="Media", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Filtro",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.mediaF, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#---------------------------------Mediana--------------------------------------------
        if operacion == 26:
            self.textoTitulo=tk.Label(self.panel, text="Mediana", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Filtro",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.medianaF, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#---------------------------------Kmeans---------------------------------------------
        if operacion == 28:
            self.textoTitulo=tk.Label(self.panel, text="Kmeans", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Filtro",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.kmeansS, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#---------------------------------Dilatacion-----------------------------------------
        if operacion == 14:
            self.textoTitulo=tk.Label(self.panel, text="Dilatacion", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Imagen dilatada",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenD, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

            #self.linkImagen.destroy()
            #self.buscar.destroy()
            #self.buscarR.destroy()

#---------------------------------Erosion-------------------------------------------
        if operacion == 15:
            self.textoTitulo=tk.Label(self.panel, text="Erosion", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Resultado",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenE, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

            #self.linkImagen.destroy()
            #self.buscar.destroy()
            #self.buscarR.destroy()

#-----------------------------------OTSU-------------------------------------------
        if operacion == 19:
            self.textoTitulo=tk.Label(self.panel, text="OTSU", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Resultado",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenOTSU, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Hough-------------------------------------------
        if operacion == 20:
            self.textoTitulo=tk.Label(self.panel, text="Hough", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Resultado",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenHough, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Canny-------------------------------------------
        if operacion == 21:
            self.textoTitulo=tk.Label(self.panel, text="Canny", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Borde",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenCanny, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Sobel-------------------------------------------
        if operacion == 22:
            self.textoTitulo=tk.Label(self.panel, text="Sobel", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Borde",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenSobel, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#---------------------------------Prewitt-----------------------------------------
        if operacion == 23:
            self.textoTitulo=tk.Label(self.panel, text="Prewitt", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Borde",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenPrewitt, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#------------------------------------Gauss-----------------------------------------
        if operacion == 24:
            self.textoTitulo=tk.Label(self.panel, text="Gauss", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Borde",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenGauss, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------Shear Vertical------------------------------------
        if operacion == 12:
            self.textoTitulo=tk.Label(self.panel, text="Shear Vertical", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Shear",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenShearV, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------Shear Horizontal-----------------------------------
        if operacion == 13:
            self.textoTitulo=tk.Label(self.panel, text="Shear Horizontal", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Shear",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenShearH, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#---------------------------------Umbral basico-----------------------------------
        if operacion == 16:
            self.textoTitulo=tk.Label(self.panel, text="Umbral basico", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Umbral invertido",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenUmbralB, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

            self.sig = tk.Button(self.panel, text="Siguiente",command=self.siguientee, bg="#E39EDB")
            self.sig.place(x=780, y=555 , width=100, height=30)

#-----------------------------Umbral por nivel-----------------------------------
        if operacion == 17:
            self.textoTitulo=tk.Label(self.panel, text="Umbral por nivel", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Umbral invertido",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenUmbralPN, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------Umbral a 2 puntos-----------------------------------
        if operacion == 18:
            self.textoTitulo=tk.Label(self.panel, text="Umbral a 2 puntos", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Umbral invertido",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenUmbral2P, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#----------------------------------------Not-------------------------------------
        if operacion == 7:
            self.textoTitulo=tk.Label(self.panel, text="Not", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="NOT",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenNOT, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)



#--------------------------------------Negativo----------------------------------
        if operacion == 9:
            self.textoTitulo=tk.Label(self.panel, text="Negativo", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Negativo",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenNegativo, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Histogramas----------------------------------
        if operacion == 30:
            self.textoTitulo=tk.Label(self.panel, text="Histogramas", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Histogramas",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenHistogramas, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Apertura----------------------------------
        if operacion == 31:
            self.textoTitulo=tk.Label(self.panel, text="Apertura", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Apertura",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.apertura, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Clausura----------------------------------
        if operacion == 32:
            self.textoTitulo=tk.Label(self.panel, text="Clausura", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Clausura",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.clausura, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Gradiente----------------------------------
        if operacion == 33:
            self.textoTitulo=tk.Label(self.panel, text="Gradiente", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Gradiente",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.gradiente, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Perimetro----------------------------------
        if operacion == 34:
            self.textoTitulo=tk.Label(self.panel, text="Perimetro", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Perimetro",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.perimetro, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Relleno----------------------------------
        if operacion == 35:
            self.textoTitulo=tk.Label(self.panel, text="Relleno", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Relleno",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.relleno, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Esqueleto----------------------------------
        if operacion == 36:
            self.textoTitulo=tk.Label(self.panel, text="Esqueleto", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Esqueleto",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.esqueleto, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------Esqueleto2----------------------------------
        if operacion == 37:
            self.textoTitulo=tk.Label(self.panel, text="Esqueleto 2", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Esqueleto 2",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.esqueleto2, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------MomentosHU----------------------------------
        if operacion == 38:
            self.textoTitulo=tk.Label(self.panel, text="Momentos HU", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Momentos",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.momentos, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

            self.sig = tk.Button(self.panel, text="Siguiente",command=self.siguienteMoment, bg="#E39EDB")
            self.sig.place(x=780, y=555 , width=100, height=30)

#-----------------------------------TopHat----------------------------------
        if operacion == 39:
            self.textoTitulo=tk.Label(self.panel, text="TopHat", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="TopHat",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.topHat, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------------BlackHat----------------------------------
        if operacion == 40:
            self.textoTitulo=tk.Label(self.panel, text="BlackHat", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="BlackHat",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.blackHat, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)
        