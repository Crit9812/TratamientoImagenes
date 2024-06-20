import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from Metodos.Seleccionar import seleccion
from algoritmos.mult import multiplicar
from algoritmos.division import dividir
from tkinter import simpledialog
import cv2
from funciones import f

class panelMD:
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
            self.original.configure(image=self.imagen_tk)

        elif self.identificador == 2:
            imagen = cv2.cvtColor(self.imagen00, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (450, 250))
            _, imagen = cv2.threshold(imagen, 200, 255, cv2.THRESH_BINARY)
            imagen_pil1 = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil1)
            self.original.configure(image=self.imagen_tk)

        else:
            imagen = imagen.resize((450, 250))
            self.imagen_tk = ImageTk.PhotoImage(imagen)
            self.original.configure(image=self.imagen_tk)
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
            self.original.configure(image=self.imagen_tk)

        elif self.identificador == 2:
            imagen = cv2.cvtColor(self.imagen00, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (450, 250))
            _, imagen = cv2.threshold(imagen, 200, 255, cv2.THRESH_BINARY)
            imagen_pil1 = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil1)
            self.original.configure(image=self.imagen_tk)

        else:
            imagen = imagen.resize((450, 250))
            self.imagen_tk = ImageTk.PhotoImage(imagen)
            self.original.configure(image=self.imagen_tk)

    def multiplicacionI(self):
        self.arregloI.clear()
        if self.identificador== 1:
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            img11, img22, img33=multiplicar.gris(imagen)
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
            self.escalar.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)

        if self.identificador== 2:
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            _, imagen = cv2.threshold(imagen, 200, 255, cv2.THRESH_BINARY)
            img11, img22, img33=multiplicar.gris(imagen)
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
            self.escalar.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)

        if self.identificador== 3:
            img11, img22, img33=multiplicar.color(self.imagen0)
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
            self.escalar.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)

            

    def divisionI(self):
        self.arregloI.clear()
        if self.identificador== 1:
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            img11, img22, img33=dividir.gris(imagen)
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
            self.escalar.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)


        if self.identificador== 2:
            imagen= cv2.cvtColor(self.imagen0, cv2.COLOR_BGR2GRAY)
            _, imagen = cv2.threshold(imagen, 200, 255, cv2.THRESH_BINARY)
            img11, img22, img33=dividir.gris(imagen)
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
            self.escalar.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)


        if self.identificador== 3:
            img11, img22, img33=dividir.color(self.imagen0)
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
            self.escalar.configure(image=self.imagen_tk3)
            self.arregloI.append(img11)
            self.arregloI.append(img22)
            self.arregloI.append(img33)

    def guarda(self):
        for imagen in self.arregloI:
            f.guardarImagen(imagen)

    def crearPanel1(self, ventana,menu_lateral,operacion,identificador):
        self.identificador=identificador
        self.panel = tk.Frame(ventana, borderwidth=2, bg="#F9E1E0",relief="solid")
        self.panel.place(x=200, y=0,width=1000, height=699)

#-----------------------------Multiplicacion---------------------------------------
        if operacion == 3:
            self.textoTitulo=tk.Label(self.panel, text="Multiplicación", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=30)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.multiplicacionI, bg="#E39EDB")
            self.continuar.place(x=800, y=650 , width=100, height=30)

#--------------------------------Division-------------------------------------------
        else:
            self.textoTitulo=tk.Label(self.panel, text="Division", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=30)
        
            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.divisionI, bg="#E39EDB")
            self.continuar.place(x=800, y=650 , width=100, height=30)

        self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
        self.textoOriginal.place(x=50, y=60, width=400, height=20)
        self.original=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.original.place(x=50, y=80, width=400, height=250)

        self.textoTruncamiento=tk.Label(self.panel, text="Truncamiento",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
        self.textoTruncamiento.place(x=500, y=60,width=400, height=20)
        self.truncamiento=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.truncamiento.place(x=500, y=80,width=400, height=250)

        self.textoCiclico=tk.Label(self.panel, text="Ciclico", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
        self.textoCiclico.place(x=50, y=360, width=400, height=20)
        self.ciclico=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.ciclico.place(x=50, y=380, width=400, height=250)

        self.textoEscalar=tk.Label(self.panel, text="Escalar", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
        self.textoEscalar.place(x=500, y=360,width=400, height=20)
        self.escalar=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.escalar.place(x=500, y=380,width=400, height=250)
        
        self.linkImagen=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
        self.linkImagen.place(x=50, y=650, width=450, height=30)

        self.buscarR = tk.Button(self.panel, text="->", command=self.selR, bg="#E39EDB")
        self.buscarR.place(x=505, y=650 , width=30, height=30)
        
        self.buscar = tk.Button(self.panel, text="BUSCAR", command=self.sel, bg="#E39EDB")
        self.buscar.place(x=540, y=650 , width=100, height=30)

        self.guardar = tk.Button(self.panel, text="Guardar",command=self.guarda, bg="#E39EDB")
        self.guardar.place(x=650, y=650 , width=100, height=30)
        