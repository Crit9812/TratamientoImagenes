import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from Metodos.Seleccionar import seleccion
from algoritmos.suma import sumar
from algoritmos.resta import restar
from algoritmos.gris import gris
from funciones import f
from algoritmos.logicasC import logColor
from algoritmos.logicasG import logGris
import cv2

class panelRSC:
    arregloI=[]
    def sel(self):
        selec = seleccion()
        imagenn = selec.evento_seleccionar()
        imagen = Image.open(imagenn)
        self.imagen00 = cv2.imread(imagenn)
        self.imagen0 = self.imagen00.copy()
        self.linkImagen.insert(0, imagenn)

        if self.identificador == 1:
            imagen = cv2.cvtColor(self.imagen00, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (450, 250))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil1)
            self.ciclico.configure(image=self.imagen_tk)

        elif self.identificador == 2:
            imagen = cv2.cvtColor(self.imagen00, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (450, 250))
            _, imagen = cv2.threshold(imagen, 200, 255, cv2.THRESH_BINARY)
            imagen_pil1 = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil1)
            self.ciclico.configure(image=self.imagen_tk)

        else:
            imagen = imagen.resize((450, 250))
            self.imagen_tk = ImageTk.PhotoImage(imagen)
            self.ciclico.configure(image=self.imagen_tk)
            self.linkImagen.insert(0, imagenn)

    def selR(self):
        imagen = Image.open(self.linkImagen.get())
        self.imagen00 = cv2.imread(self.linkImagen.get())
        self.imagen0=self.imagen00.copy()

        if self.identificador == 1:
            imagen = cv2.cvtColor(self.imagen00, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (450, 250))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil1)
            self.ciclico.configure(image=self.imagen_tk)

        elif self.identificador == 2:
            imagen = cv2.cvtColor(self.imagen00, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (450, 250))
            _, imagen = cv2.threshold(imagen, 200, 255, cv2.THRESH_BINARY)
            imagen_pil1 = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil1)
            self.ciclico.configure(image=self.imagen_tk)

        else:
            imagen = imagen.resize((450, 250))
            self.imagen_tk = ImageTk.PhotoImage(imagen)
            self.ciclico.configure(image=self.imagen_tk)

    def sel2 (self):
        selec2 = seleccion()
        imagenn2 = selec2.evento_seleccionar()
        imagen2 = Image.open(imagenn2)
        self.imagen002 = cv2.imread(imagenn2)
        self.imagen02 = self.imagen002.copy()
        self.linkImagen2.insert(0, imagenn2)

        if self.identificador == 1:
            imagen2 = cv2.cvtColor(self.imagen002, cv2.COLOR_BGR2GRAY)
            imagen2 = cv2.resize(imagen2, (450, 250))
            imagen_pil12 = Image.fromarray(cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil12)
            self.truncamiento.configure(image=self.imagen_tk2)

        elif self.identificador == 2:
            imagen2 = cv2.cvtColor(self.imagen002, cv2.COLOR_BGR2GRAY)
            imagen2 = cv2.resize(imagen2, (450, 250))
            _, imagen2 = cv2.threshold(imagen2, 200, 255, cv2.THRESH_BINARY)
            imagen_pil12 = Image.fromarray(cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil12)
            self.truncamiento.configure(image=self.imagen_tk2)

        else:
            imagen2 = imagen2.resize((450, 250))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen2)
            self.truncamiento.configure(image=self.imagen_tk2)
            self.linkImagen2.insert(0, imagenn2)

    def selR2(self):
        imagen2 = Image.open(self.linkImagen.get())
        self.imagen002 = cv2.imread(self.linkImagen.get())
        self.imagen02=self.imagen002.copy()

        if self.identificador == 1:
            imagen2 = cv2.cvtColor(self.imagen002, cv2.COLOR_BGR2GRAY)
            imagen2 = cv2.resize(imagen2, (450, 250))
            imagen_pil12 = Image.fromarray(cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil12)
            self.truncamiento.configure(image=self.imagen_tk2)

        elif self.identificador == 2:
            imagen2 = cv2.cvtColor(self.imagen002, cv2.COLOR_BGR2GRAY)
            imagen2 = cv2.resize(imagen2, (450, 250))
            _, imagen2 = cv2.threshold(imagen2, 200, 255, cv2.THRESH_BINARY)
            imagen_pil12 = Image.fromarray(cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil12)
            self.truncamiento.configure(image=self.imagen_tk2)

        else:
            imagen2 = imagen2.resize((450, 250))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen2)
            self.truncamiento.configure(image=self.imagen_tk2)
    
    def sumaI (self):
        self.arregloI.clear()
        self.nombre1 ="Ciclica"
        self.nombre2 ="Truncado"
        self.textoCiclico=tk.Label(self.panel, text=self.nombre1, bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
        self.textoCiclico.place(x=50, y=60, width=400, height=20)
        self.textoTruncamiento=tk.Label(self.panel, text=self.nombre2,bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
        self.textoTruncamiento.place(x=500, y=60,width=400, height=20)

        imagen, imagen2=f.redimensionar(self.imagen0, self.imagen02)
        if self.identificador== 1:
            imagen= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            imagen2= cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)
            img11, img22, img33=sumar.gris(imagen,imagen2)
            img1 = cv2.resize(img11,(450,250))
            img2 = cv2.resize(img22,(450,250))
            img3 = cv2.resize(img33,(450,250))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
            imagen_pil3 = Image.fromarray(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
            self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)

            self.truncamiento.configure(image=self.imagen_tk1)
            self.ciclico.configure(image=self.imagen_tk2)
            self.original.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)

        if self.identificador== 2:
            imagen= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            imagen2= cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)
            _, imagen = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)
            _, imagen2 = cv2.threshold(imagen2, 128, 255, cv2.THRESH_BINARY)
            img11, img22, img33=sumar.gris(imagen, imagen2)
            img1 = cv2.resize(img11,(450,250))
            img2 = cv2.resize(img22,(450,250))
            img3 = cv2.resize(img33,(450,250))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
            imagen_pil3 = Image.fromarray(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
            self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)

            self.truncamiento.configure(image=self.imagen_tk1)
            self.ciclico.configure(image=self.imagen_tk2)
            self.original.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)


        if self.identificador== 3:
            img11, img22, img33=sumar.color(imagen,imagen2)
            img1 = cv2.resize(img11,(450,250))
            img2 = cv2.resize(img22,(450,250))
            img3 = cv2.resize(img33,(450,250))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
            imagen_pil3 = Image.fromarray(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
            self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)

            self.truncamiento.configure(image=self.imagen_tk1)
            self.ciclico.configure(image=self.imagen_tk2)
            self.original.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)


    def restaI (self):
        self.arregloI.clear()
        self.nombre1 ="Ciclica"
        self.nombre2 ="Truncado"
        self.textoCiclico=tk.Label(self.panel, text=self.nombre1, bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
        self.textoCiclico.place(x=50, y=60, width=400, height=20)
        self.textoTruncamiento=tk.Label(self.panel, text=self.nombre2,bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
        self.textoTruncamiento.place(x=500, y=60,width=400, height=20)

        imagen, imagen2=f.redimensionar(self.imagen0, self.imagen02)
        if self.identificador== 1:
            imagen= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            imagen2= cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)
            img11, img22, img33=restar.gris(imagen,imagen2)
            img1 = cv2.resize(img11,(450,250))
            img2 = cv2.resize(img22,(450,250))
            img3 = cv2.resize(img33,(450,250))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
            imagen_pil3 = Image.fromarray(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
            self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)

            self.truncamiento.configure(image=self.imagen_tk1)
            self.ciclico.configure(image=self.imagen_tk2)
            self.original.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)

        if self.identificador== 2:
            imagen= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            imagen2= cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)
            _, imagen = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)
            _, imagen2 = cv2.threshold(imagen2, 128, 255, cv2.THRESH_BINARY)
            img11, img22, img33=restar.gris(imagen, imagen2)
            img1 = cv2.resize(img11,(450,250))
            img2 = cv2.resize(img22,(450,250))
            img3 = cv2.resize(img33,(450,250))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
            imagen_pil3 = Image.fromarray(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
            self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)

            self.truncamiento.configure(image=self.imagen_tk1)
            self.ciclico.configure(image=self.imagen_tk2)
            self.original.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)


        if self.identificador== 3:
            img11, img22, img33=restar.color(imagen,imagen2)
            img1 = cv2.resize(img11,(450,250))
            img2 = cv2.resize(img22,(450,250))
            img3 = cv2.resize(img33,(450,250))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
            imagen_pil3 = Image.fromarray(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
            self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)

            self.truncamiento.configure(image=self.imagen_tk1)
            self.ciclico.configure(image=self.imagen_tk2)
            self.original.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)

    
    def imagenAND (self):
        self.arregloI.clear()
        if self.identificador== 1:
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            imagen2= cv2.cvtColor(self.imagen02, cv2.COLOR_BGR2GRAY)
            img11=logGris.andd(imagen,imagen2)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)
            

        if self.identificador== 2:
            imagen2= cv2.cvtColor(self.imagen02, cv2.COLOR_BGR2GRAY)
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            _, imagen = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)
            _, imagen2 = cv2.threshold(imagen2, 128, 255, cv2.THRESH_BINARY)
            img11=logGris.andd(imagen,imagen2)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 3:
            img11=logColor.andd(self.imagen0,self.imagen02)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)
        self.original.configure(image=self.imagen_tk1)

    def imagenOR (self):
        self.arregloI.clear()
        if self.identificador== 1:           
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            imagen2= cv2.cvtColor(self.imagen02, cv2.COLOR_BGR2GRAY)
            img11=logGris.orr(imagen,imagen2)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)
        if self.identificador== 2:
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            imagen2= cv2.cvtColor(self.imagen02, cv2.COLOR_BGR2GRAY)
            _, imagen = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)
            _, imagen2 = cv2.threshold(imagen2, 128, 255, cv2.THRESH_BINARY)
            img11=logGris.orr(imagen,imagen2)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)
        if self.identificador== 3:
            img11=logColor.orr(self.imagen0, self.imagen02)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)    
        self.original.configure(image=self.imagen_tk1)

    def imagenXOR (self):
        self.arregloI.clear()
        if self.identificador== 1:             
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            imagen2= cv2.cvtColor(self.imagen02, cv2.COLOR_BGR2GRAY)
            img11=logGris.xorr(imagen, imagen2)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 2:
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            imagen2= cv2.cvtColor(self.imagen02, cv2.COLOR_BGR2GRAY)
            _, imagen = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)
            _, imagen2 = cv2.threshold(imagen2, 128, 255, cv2.THRESH_BINARY)
            img11=logGris.xorr(imagen,imagen2)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)

        if self.identificador== 3:
            img11=logColor.xorr(self.imagen0,self.imagen02)
            img1 = cv2.resize(img11,(400,400))
            imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
            self.arregloI.append(img11)
        self.original.configure(image=self.imagen_tk1)

    def imagenGris(self):
        self.arregloI.clear()
        img11, img22=gris.grisColor(self.imagen0)
        img1 = cv2.resize(img11,(450,250))
        img2 = cv2.resize(img22,(450,250))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

        self.original.configure(image=self.imagen_tk1)
        self.truncamiento.configure(image=self.imagen_tk2)
        self.arregloI.append(img11)
        self.arregloI.append(img22)


    def guarda(self):
        for imagen in self.arregloI:
            f.guardarImagen(imagen)

    def crearPanel1(self, ventana,menu_lateral,operacion,identificador):
        self.identificador=identificador
        self.panel = tk.Frame(ventana, borderwidth=2, bg="#F9E1E0",relief="solid")
        self.panel.place(x=200, y=0,width=1000, height=699)
        self.nombre1 ="Imagen 1"
        self.nombre2 ="Imagen 2"
        
#-----------------------------SUMA-------------------------------------------------
        if operacion == 1:
            self.textoTitulo=tk.Label(self.panel, text="Suma", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoCiclico=tk.Label(self.panel, text=self.nombre1, bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoCiclico.place(x=50, y=60, width=400, height=20)

            self.textoOriginal=tk.Label(self.panel, text="Escalar", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=360, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text=self.nombre2,bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=60,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR", command=self.sumaI, bg="#E39EDB")
            self.continuar.place(x=750, y=580 , width=100, height=30)

            self.linkImagen=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen.place(x=500, y=430, width=350, height=30)

            self.buscarR = tk.Button(self.panel, text="->", command=self.selR, bg="#E39EDB")
            self.buscarR.place(x=855, y=430 , width=30, height=30)
            
            self.buscar = tk.Button(self.panel, text="Imagen 1", command=self.sel, bg="#E39EDB")
            self.buscar.place(x=550, y=390 , width=200, height=30)

            self.linkImagen2=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen2.place(x=500, y=520, width=350, height=30)

            self.buscarR2 = tk.Button(self.panel, text="->", command=self.selR2, bg="#E39EDB")
            self.buscarR2.place(x=855, y=520 , width=30, height=30)
            
            self.buscar2 = tk.Button(self.panel, text="Imagen 2", command=self.sel2, bg="#E39EDB")
            self.buscar2.place(x=550, y=480 , width=200, height=30)

#--------------------------------Resta------------------------------------------------
        if operacion == 2:
            self.textoTitulo=tk.Label(self.panel, text="Resta", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoCiclico=tk.Label(self.panel, text=self.nombre1, bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoCiclico.place(x=50, y=60, width=400, height=20)

            self.textoOriginal=tk.Label(self.panel, text="Escalar", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=360, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text=self.nombre2,bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=60,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.restaI, bg="#E39EDB")
            self.continuar.place(x=750, y=580 , width=100, height=30)

            self.linkImagen=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen.place(x=500, y=430, width=350, height=30)

            self.buscarR = tk.Button(self.panel, text="->", command=self.selR, bg="#E39EDB")
            self.buscarR.place(x=855, y=430 , width=30, height=30)
            
            self.buscar = tk.Button(self.panel, text="Imagen 1", command=self.sel, bg="#E39EDB")
            self.buscar.place(x=550, y=390 , width=200, height=30)

            self.linkImagen2=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen2.place(x=500, y=520, width=350, height=30)

            self.buscarR2 = tk.Button(self.panel, text="->", command=self.selR2, bg="#E39EDB")
            self.buscarR2.place(x=855, y=520 , width=30, height=30)
            
            self.buscar2 = tk.Button(self.panel, text="Imagen 2", command=self.sel2, bg="#E39EDB")
            self.buscar2.place(x=550, y=480 , width=200, height=30)

#--------------------------------Conversion a gris------------------------------------
        if operacion == 29:
            self.textoTitulo=tk.Label(self.panel, text="Convertir a gris", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoCiclico=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoCiclico.place(x=50, y=60, width=400, height=20)

            self.textoOriginal=tk.Label(self.panel, text="Formula", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=360, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Division de canales",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=60,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenGris, bg="#E39EDB")
            self.continuar.place(x=750, y=580 , width=100, height=30)

            self.linkImagen=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen.place(x=500, y=430, width=350, height=30)

            self.buscarR = tk.Button(self.panel, text="->", command=self.selR, bg="#E39EDB")
            self.buscarR.place(x=855, y=430 , width=30, height=30)
            
            self.buscar = tk.Button(self.panel, text="Imagen 1", command=self.sel, bg="#E39EDB")
            self.buscar.place(x=550, y=390 , width=200, height=30)
        
        
#--------------------------------------And----------------------------------------
        if operacion == 5:
            self.textoTitulo=tk.Label(self.panel, text="And", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="AND",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenAND, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

            self.linkImagen=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen.place(x=500, y=430, width=350, height=30)

            self.buscarR = tk.Button(self.panel, text="->", command=self.selR, bg="#E39EDB")
            self.buscarR.place(x=855, y=430 , width=30, height=30)
            
            self.buscar = tk.Button(self.panel, text="Imagen 1", command=self.sel, bg="#E39EDB")
            self.buscar.place(x=550, y=390 , width=200, height=30)

            self.linkImagen2=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen2.place(x=500, y=520, width=350, height=30)

            self.buscarR2 = tk.Button(self.panel, text="->", command=self.selR2, bg="#E39EDB")
            self.buscarR2.place(x=855, y=520 , width=30, height=30)
            
            self.buscar2 = tk.Button(self.panel, text="Imagen 2", command=self.sel2, bg="#E39EDB")
            self.buscar2.place(x=550, y=480 , width=200, height=30)

#---------------------------------------Or----------------------------------------
        if operacion == 6:
            self.textoTitulo=tk.Label(self.panel, text="Or", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="OR",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenOR, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

            self.linkImagen=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen.place(x=500, y=430, width=350, height=30)

            self.buscarR = tk.Button(self.panel, text="->", command=self.selR, bg="#E39EDB")
            self.buscarR.place(x=855, y=430 , width=30, height=30)
            
            self.buscar = tk.Button(self.panel, text="Imagen 1", command=self.sel, bg="#E39EDB")
            self.buscar.place(x=550, y=390 , width=200, height=30)

            self.linkImagen2=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen2.place(x=500, y=520, width=350, height=30)

            self.buscarR2 = tk.Button(self.panel, text="->", command=self.selR2, bg="#E39EDB")
            self.buscarR2.place(x=855, y=520 , width=30, height=30)
            
            self.buscar2 = tk.Button(self.panel, text="Imagen 2", command=self.sel2, bg="#E39EDB")
            self.buscar2.place(x=550, y=480 , width=200, height=30)

#-----------------------------------------Xor-----------------------------------
        if operacion == 8:
            self.textoTitulo=tk.Label(self.panel, text="Xor", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=35)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=50, y=110, width=400, height=20)

            self.textoTruncamiento=tk.Label(self.panel, text="Xor",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoTruncamiento.place(x=500, y=110,width=400, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.imagenXOR, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

            self.linkImagen=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen.place(x=500, y=430, width=350, height=30)

            self.buscarR = tk.Button(self.panel, text="->", command=self.selR, bg="#E39EDB")
            self.buscarR.place(x=855, y=430 , width=30, height=30)
            
            self.buscar = tk.Button(self.panel, text="Imagen 1", command=self.sel, bg="#E39EDB")
            self.buscar.place(x=550, y=390 , width=200, height=30)

            self.linkImagen2=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
            self.linkImagen2.place(x=500, y=520, width=350, height=30)

            self.buscarR2 = tk.Button(self.panel, text="->", command=self.selR2, bg="#E39EDB")
            self.buscarR2.place(x=855, y=520 , width=30, height=30)
            
            self.buscar2 = tk.Button(self.panel, text="Imagen 2", command=self.sel2, bg="#E39EDB")
            self.buscar2.place(x=550, y=480 , width=200, height=30)        
        
        self.ciclico=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.ciclico.place(x=50, y=80, width=400, height=250)

        
        self.original=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.original.place(x=50, y=380, width=400, height=250)

        
        self.truncamiento=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.truncamiento.place(x=500, y=80,width=400, height=250)


        self.guardar = tk.Button(self.panel, text="Guardar",command=self.guarda, bg="#E39EDB")
        self.guardar.place(x=550, y=580 , width=100, height=30)


        