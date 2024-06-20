import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from Metodos.Seleccionar import seleccion
from tkinter import simpledialog
from tkinter import messagebox
from algoritmos.segmentarBordes import bordes
from algoritmos.transformaciones import transf
from algoritmos.conversionesColor import Col
import cv2
from funciones import f

class panelSE:
    arregloI=[]
    def sel(self):
        self.textoOriginal.config(text="Original")
        selec = seleccion()
        imagenn = selec.evento_seleccionar()
        imagen = Image.open(imagenn)
        self.imagen00 = cv2.imread(imagenn)
        self.imagen0 = self.imagen00.copy()
        self.linkImagen.insert(0, imagenn)

        
        imagen = imagen.resize((300, 400))
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.original.configure(image=self.imagen_tk)
        self.linkImagen.insert(0, imagenn)

    def selR(self):
        self.textoOriginal.config(text="Original")
        imagen = Image.open(self.linkImagen.get())
        self.imagen00 = cv2.imread(self.linkImagen.get())
        self.imagen0=self.imagen00.copy()

        
        imagen = imagen.resize((300, 400))
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.original.configure(image=self.imagen_tk)

    def espe(self):
        self.arregloI.clear()
        img11, img22=transf.espejo(self.imagen0)
        img1 = cv2.resize(img11,(300,400))
        img2 = cv2.resize(img22,(300,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

        self.Horizontal.configure(image=self.imagen_tk1)
        self.Vertical.configure(image=self.imagen_tk2)
        self.arregloI.append(img11)
        self.arregloI.append(img22)
    

    def segmen(self):   
        self.arregloI.clear()
        r1,g2,b3, I=bordes.obtenerRGB(self.imagen0)
        img1 = cv2.resize(r1,(300,400))
        img2 = cv2.resize(g2,(300,400))
        img3 = cv2.resize(b3,(300,400))
        imagen_pil1 = Image.fromarray(img1)
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        imagen_pil2 = Image.fromarray(img2)
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
        imagen_pil3 = Image.fromarray(img3)
        self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)
        self.original.configure(image=self.imagen_tk3)
        self.Horizontal.configure(image=self.imagen_tk1)
        self.Vertical.configure(image=self.imagen_tk2)
        self.arregloI.append(r1)
        self.arregloI.append(g2)
        self.arregloI.append(b3)
       
        #mostrar r g b
        rb1,gb2,bb3=bordes.segmentarRGB(r1,g2,b3, I)
        img1 = cv2.resize(rb1,(300,400))
        img2 = cv2.resize(gb2,(300,400))
        img3 = cv2.resize(bb3,(300,400))
        imagen_pil1 = Image.fromarray(img1)
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        imagen_pil2 = Image.fromarray(img2)
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
        imagen_pil3 = Image.fromarray(img3)
        self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)
        self.original.configure(image=self.imagen_tk3)
        self.Horizontal.configure(image=self.imagen_tk1)
        self.Vertical.configure(image=self.imagen_tk2)
        messagebox.showinfo("Mensaje","Continuar")
        self.arregloI.append(rb1)
        self.arregloI.append(gb2)
        self.arregloI.append(bb3)
        #mostrar rb, gb, bb
        img11, img22, img33=bordes.segmentar(rb1,gb2,bb3,self.imagen0)
        img1 = cv2.resize(img11,(300,400))
        img2 = cv2.resize(img22,(300,400))
        img3 = cv2.resize(img33,(300,400))
        imagen_pil1 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        imagen_pil2 = Image.fromarray(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
        imagen_pil3 = Image.fromarray(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
        self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)
        self.original.configure(image=self.imagen_tk3)
        self.Horizontal.configure(image=self.imagen_tk1)
        self.Vertical.configure(image=self.imagen_tk2)
        self.arregloI.append(img11)
        self.arregloI.append(img22)
        self.arregloI.append(img33)

    def espacioHSV(self):
        global p1, p2, p3
        self.arregloI.clear()
        img11, p1, p2, p3=Col.BGRaHSV(self.imagen0)
        res2=Col.HSVaBGR(img11)
        img1 = cv2.resize(self.imagen0,(300,400))
        img2 = cv2.resize(img11,(300,400))
        img3 = cv2.resize(res2,(300,400))
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
        imagen_pil1 = Image.fromarray(img3)
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        imagen_pil2 = Image.fromarray(img2)
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
        imagen_pil3 = Image.fromarray(img1)
        self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)
        self.original.configure(image=self.imagen_tk3)
        self.Horizontal.configure(image=self.imagen_tk1)
        self.Vertical.configure(image=self.imagen_tk2)
        img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
        img3 = cv2.cvtColor(img3, cv2.COLOR_RGB2BGR)
        self.arregloI.append(img2)
        self.arregloI.append(img3)
    
    def espacioRGB(self):
        global p1, p2, p3
        self.arregloI.clear()
        img11, p1, p2, p3=Col.BGRaRGB(self.imagen0)
        res2=Col.RGBaBGR(img11)
        img1 = cv2.resize(self.imagen0,(300,400))
        img2 = cv2.resize(img11,(300,400))
        img3 = cv2.resize(res2,(300,400))
        img1G = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img2G = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img3G = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
        imagen_pil1 = Image.fromarray(img3G)
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        imagen_pil2 = Image.fromarray(img2G)
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
        imagen_pil3 = Image.fromarray(img1G)
        self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)
        self.original.configure(image=self.imagen_tk3)
        self.Horizontal.configure(image=self.imagen_tk1)
        self.Vertical.configure(image=self.imagen_tk2)
        self.arregloI.append(img11)
        self.arregloI.append(res2)
    
    def espacioMVK(self):
        global p1, p2, p3
        self.arregloI.clear()
        img11,k, p1, p2, p3=Col.BGRaCMYK(self.imagen0)
        res2=Col.CMYKaBGR(img11,k)
        img1 = cv2.resize(self.imagen0,(300,400))
        img2 = cv2.resize(img11,(300,400))
        img3 = cv2.resize(res2,(300,400))
        img1G = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img2G = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img3G = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
        imagen_pil1 = Image.fromarray(img3G)
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        imagen_pil2 = Image.fromarray(img2G)
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
        imagen_pil3 = Image.fromarray(img1G)
        self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)
        self.original.configure(image=self.imagen_tk3)
        self.Horizontal.configure(image=self.imagen_tk1)
        self.Vertical.configure(image=self.imagen_tk2)
        self.arregloI.append(img11)
        self.arregloI.append(res2)

    def siguientee(self):
        img1 = cv2.resize(p1,(300,400))
        #cv2.imshow("p1", p1)
        img2 = cv2.resize(p2,(300,400))
        #cv2.imshow("p2", p2)
        img3 = cv2.resize(p3,(300,400))
        #cv2.imshow("p3", p3)
        imagen_pil1 = Image.fromarray(img3)
        self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)
        imagen_pil2 = Image.fromarray(img2)
        self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)
        imagen_pil3 = Image.fromarray(img1)
        self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)
        self.original.configure(image=self.imagen_tk3)
        self.Horizontal.configure(image=self.imagen_tk1)
        self.Vertical.configure(image=self.imagen_tk2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.arregloI.append(img1)
        self.arregloI.append(img2)
        self.arregloI.append(img3)



    def guarda(self):
        for imagen in self.arregloI:
            f.guardarImagen(imagen)

    def crearPanel1(self, ventana,menu_lateral,operacion):
        self.panel = tk.Frame(ventana, borderwidth=2, bg="#F9E1E0",relief="solid")
        self.panel.place(x=200, y=0,width=1000, height=699)

#-----------------------------Espejo--------------------------------------------
        if operacion == 11:
            self.textoTitulo=tk.Label(self.panel, text="Espejo", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=30)

            self.textoOriginal=tk.Label(self.panel, text="Original", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=30, y=110, width=300, height=20)

            self.textoVertical=tk.Label(self.panel, text="Vertical",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoVertical.place(x=350, y=110,width=300, height=20)

            self.textoHorizontal=tk.Label(self.panel, text="Horizontal",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoHorizontal.place(x=670, y=110,width=300, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.espe, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------Segmentacion de bordes------------------------------
        if operacion == 27:
            self.textoTitulo=tk.Label(self.panel, text="Segmentacion de bordes", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=30)

            self.textoOriginal=tk.Label(self.panel, text="R", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=30, y=110, width=300, height=20)

            self.textoVertical=tk.Label(self.panel, text="G",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoVertical.place(x=350, y=110,width=300, height=20)

            self.textoHorizontal=tk.Label(self.panel, text="B",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoHorizontal.place(x=670, y=110,width=300, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.segmen, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

#-----------------------------Espacio HSV------------------------------
        if operacion == 41:
            self.textoTitulo=tk.Label(self.panel, text="Espacio HSV", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=30)

            self.textoOriginal=tk.Label(self.panel, text="R", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=30, y=110, width=300, height=20)

            self.textoVertical=tk.Label(self.panel, text="G",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoVertical.place(x=350, y=110,width=300, height=20)

            self.textoHorizontal=tk.Label(self.panel, text="B",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoHorizontal.place(x=670, y=110,width=300, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.espacioHSV, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

            self.sig = tk.Button(self.panel, text="Siguiente",command=self.siguientee, bg="#E39EDB")
            self.sig.place(x=790, y=560 , width=100, height=30)

#-----------------------------Espacio RGB------------------------------
        if operacion == 42:
            self.textoTitulo=tk.Label(self.panel, text="Espacio RGB", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=30)

            self.textoOriginal=tk.Label(self.panel, text="R", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=30, y=110, width=300, height=20)

            self.textoVertical=tk.Label(self.panel, text="G",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoVertical.place(x=350, y=110,width=300, height=20)

            self.textoHorizontal=tk.Label(self.panel, text="B",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoHorizontal.place(x=670, y=110,width=300, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.espacioRGB, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

            self.sig = tk.Button(self.panel, text="Siguiente",command=self.siguientee, bg="#E39EDB")
            self.sig.place(x=790, y=560 , width=100, height=30)

#-----------------------------Espacio MVK------------------------------
        if operacion == 43:
            self.textoTitulo=tk.Label(self.panel, text="Espacio MVK", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 24))
            self.textoTitulo.place(x=300, y=20, width=400, height=30)

            self.textoOriginal=tk.Label(self.panel, text="R", bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoOriginal.place(x=30, y=110, width=300, height=20)

            self.textoVertical=tk.Label(self.panel, text="G",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoVertical.place(x=350, y=110,width=300, height=20)

            self.textoHorizontal=tk.Label(self.panel, text="B",bg=self.panel.cget("bg"), borderwidth=0, font=("Arial", 12))
            self.textoHorizontal.place(x=670, y=110,width=300, height=20)

            self.continuar = tk.Button(self.panel, text="REALIZAR",command=self.espacioMVK, bg="#E39EDB")
            self.continuar.place(x=800, y=600 , width=100, height=30)

            self.sig = tk.Button(self.panel, text="Siguiente",command=self.siguientee, bg="#E39EDB")
            self.sig.place(x=790, y=560 , width=100, height=30)
        
        
        self.original=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.original.place(x=30, y=150, width=300, height=400)

        
        self.Vertical=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.Vertical.place(x=350, y=150,width=300, height=400)

        
        self.Horizontal=tk.Label(self.panel, text="Imagen 1", borderwidth=2, relief="solid", highlightbackground="black")
        self.Horizontal.place(x=670, y=150,width=300, height=400)
        
        self.linkImagen=tk.Entry(self.panel, borderwidth=2, relief="solid", highlightbackground="black")
        self.linkImagen.place(x=50, y=600, width=450, height=30)

        self.buscarR = tk.Button(self.panel, text="->", command=self.selR, bg="#E39EDB")
        self.buscarR.place(x=505, y=600 , width=30, height=30)
        
        self.buscar = tk.Button(self.panel, text="BUSCAR", command=self.sel, bg="#E39EDB")
        self.buscar.place(x=540, y=600 , width=100, height=30)

        self.guardar = tk.Button(self.panel, text="Guardar",command=self.guarda, bg="#E39EDB")
        self.guardar.place(x=650, y=600 , width=100, height=30)

        
        