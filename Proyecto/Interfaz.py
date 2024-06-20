import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

from Paneles.panelMD import panelMD
from Paneles.panelRSC import panelRSC
from Paneles.panelMMK import panelMMK
from Paneles.panelSE import panelSE
class interfaz:
    operac = None
    identificador=0
    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.place_forget()
        else:
            self.menu_lateral.place(x=0, y=40, width=199)

    def operacionesAl(self):
        if self.botonSuma.winfo_ismapped():
            self.botonSuma.pack_forget()
            self.botonResta.pack_forget()
            self.botonMultiplicacion.pack_forget()
            self.botonDivision.pack_forget()
        else:
            self.botonSuma.pack(fill="x", after=self.boton_menuAlg)
            self.botonResta.pack(fill="x", after=self.botonSuma)
            self.botonMultiplicacion.pack(fill="x", after=self.botonResta)
            self.botonDivision.pack(fill="x", after=self.botonMultiplicacion)

            if self.botonOr.winfo_ismapped():
                self.operacionesLog()
                if self.botonGris.winfo_ismapped():
                    self.capas(0)

            if self.botonTransformaciones2.winfo_ismapped():
                self.transform()

            if self.botonDilatacion.winfo_ismapped():
                self.operacionesMor()

            if self.botonUmbralBasico.winfo_ismapped():
                self.umbral()
                if self.botonColor2.winfo_ismapped():
                    self.capas2(0)

            if self.botonCanny.winfo_ismapped():
                self.deteccionB()

            if self.botonMedia.winfo_ismapped():
                self.filtro()

            if self.botonHSV.winfo_ismapped():
                self.metEspaciosColor()

    def operacionesLog(self):
        if self.botonAnd.winfo_ismapped():
            self.botonAnd.pack_forget()
            self.botonOr.pack_forget()
            self.botonNot.pack_forget()
            self.botonXor.pack_forget()
        else:
            self.botonAnd.pack(fill="x", after=self.boton_menuLog)
            self.botonOr.pack(fill="x", after=self.botonAnd)
            self.botonNot.pack(fill="x", after=self.botonOr)
            self.botonXor.pack(fill="x", after=self.botonNot)

            if self.botonSuma.winfo_ismapped():
                self.operacionesAl()
                if self.botonBN.winfo_ismapped():
                    self.capas(0)

            if self.botonTransformaciones2.winfo_ismapped():
                self.transform()

            if self.botonDilatacion.winfo_ismapped():
                self.operacionesMor()

            if self.botonUmbralBasico.winfo_ismapped():
                self.umbral()
                if self.botonColor2.winfo_ismapped():
                    self.capas2(0)

            if self.botonCanny.winfo_ismapped():
                self.deteccionB()

            if self.botonMedia.winfo_ismapped():
                self.filtro()

            if self.botonHSV.winfo_ismapped():
                self.metEspaciosColor()

    def capas(self,oper):
        if self.botonGris.winfo_ismapped():
            self.botonGris.pack_forget()
            self.botonBN.pack_forget()
            self.botonColor.pack_forget()
            if oper!=0:
                self.capas(oper)
        else:
            if oper == 1:
                self.operac = oper
                opera = self.botonSuma
            if oper == 2:
                self.operac = oper
                opera = self.botonResta
            if oper == 3:
                self.operac = oper
                opera = self.botonMultiplicacion
            if oper == 4:
                self.operac = oper
                opera = self.botonDivision
            if oper == 5:
                self.operac = oper
                opera = self.botonAnd
            if oper == 6:
                self.operac = oper
                opera = self.botonOr
            if oper == 7:
                self.operac = oper
                opera = self.botonNot
            if oper == 8:
                self.operac = oper
                opera = self.botonXor
            if oper == 9:
                self.operac = oper
                opera = self.boton_menuNeg
            self.botonGris.pack(fill="x", after=opera)
            self.botonBN.pack(fill="x", after=self.botonGris)
            self.botonColor.pack(fill="x", after=self.botonBN)
    
    def capas2(self,opumbr):
        if self.botonGris2.winfo_ismapped():
            self.botonGris2.pack_forget()
            self.botonColor2.pack_forget()
            if opumbr!=0:
                self.capas2(opumbr)
        else:
            if opumbr == 14:
                self.operac = opumbr
                opera = self.botonDilatacion
            if opumbr == 15:
                self.operac = opumbr
                opera = self.botonErosion
            if opumbr == 16:
                self.operac = opumbr
                opera = self.botonUmbralBasico
            if opumbr == 17:
                self.operac = opumbr
                opera = self.botonUmbralPorN
            if opumbr == 18:
                self.operac = opumbr
                opera = self.botonUmbral2P
            if opumbr == 30:
                self.operac = opumbr
                opera = self.boton_menuHistograma
            if opumbr == 31:
                self.operac = opumbr
                opera = self.botonApertura
            if opumbr == 32:
                self.operac = opumbr
                opera = self.botonClausura
            if opumbr == 33:
                self.operac = opumbr
                opera = self.botonGradiente
            if opumbr == 34:
                self.operac = opumbr
                opera = self.botonPerimetro
            self.botonGris2.pack(fill="x", after=opera)
            self.botonColor2.pack(fill="x", after=self.botonGris2)

    def transform(self):
        if self.botonTransformaciones2.winfo_ismapped():
            self.botonTransformaciones2.pack_forget()
            self.botonEspejo.pack_forget()
            self.botonShearV.pack_forget()
            self.botonShearH.pack_forget()
        else:
            self.botonTransformaciones2.pack(fill="x", after=self.boton_menuTrans)
            self.botonEspejo.pack(fill="x", after=self.botonTransformaciones2)
            self.botonShearV.pack(fill="x", after=self.botonEspejo)
            self.botonShearH.pack(fill="x", after=self.botonShearV)

            if self.botonSuma.winfo_ismapped():
                self.operacionesAl()
                if self.botonBN.winfo_ismapped():
                    self.capas(0)

            if self.botonOr.winfo_ismapped():
                self.operacionesLog()
                if self.botonGris.winfo_ismapped():
                    self.capas(0)

            if self.botonDilatacion.winfo_ismapped():
                self.operacionesMor()

            if self.botonUmbralBasico.winfo_ismapped():
                self.umbral()
                if self.botonColor2.winfo_ismapped():
                    self.capas2(0)

            if self.botonCanny.winfo_ismapped():
                self.deteccionB()

            if self.botonMedia.winfo_ismapped():
                self.filtro()

            if self.botonHSV.winfo_ismapped():
                self.metEspaciosColor()

    def operacionesMor(self):
        if self.botonDilatacion.winfo_ismapped():
            self.botonDilatacion.pack_forget()
            self.botonErosion.pack_forget()
            self.botonApertura.pack_forget()
            self.botonClausura.pack_forget()
            self.botonGradiente.pack_forget()
            self.botonPerimetro.pack_forget()
            self.botonRelleno.pack_forget()
            self.botonEsqueleto.pack_forget()
        else:
            self.botonDilatacion.pack(fill="x", after=self.boton_menuMorf)
            self.botonErosion.pack(fill="x", after=self.botonDilatacion)
            self.botonApertura.pack(fill="x", after=self.botonErosion)
            self.botonClausura.pack(fill="x", after=self.botonApertura)
            self.botonGradiente.pack(fill="x", after=self.botonClausura)
            self.botonPerimetro.pack(fill="x", after=self.botonGradiente)
            self.botonRelleno.pack(fill="x", after=self.botonPerimetro)
            self.botonEsqueleto.pack(fill="x", after=self.botonRelleno)

            if self.botonSuma.winfo_ismapped():
                self.operacionesAl()
                if self.botonBN.winfo_ismapped():
                    self.capas(0)

            if self.botonOr.winfo_ismapped():
                self.operacionesLog()
                if self.botonGris.winfo_ismapped():
                    self.capas(0)

            if self.botonTransformaciones2.winfo_ismapped():
                self.transform()

            if self.botonUmbralBasico.winfo_ismapped():
                self.umbral()
                if self.botonColor2.winfo_ismapped():
                    self.capas2(0)

            if self.botonCanny.winfo_ismapped():
                self.deteccionB()

            if self.botonMedia.winfo_ismapped():
                self.filtro()

            if self.botonHSV.winfo_ismapped():
                self.metEspaciosColor()

    def umbral(self):
        if self.botonUmbralBasico.winfo_ismapped():
            self.botonUmbralBasico.pack_forget()
            self.botonUmbralPorN.pack_forget()
            self.botonUmbral2P.pack_forget()
            self.botonUmbralOTSU.pack_forget()
        else:
            self.botonUmbralBasico.pack(fill="x", after=self.boton_menuUmbral)
            self.botonUmbralPorN.pack(fill="x", after=self.botonUmbralBasico)
            self.botonUmbral2P.pack(fill="x", after=self.botonUmbralPorN)
            self.botonUmbralOTSU.pack(fill="x", after=self.botonUmbral2P)

            if self.botonSuma.winfo_ismapped():
                self.operacionesAl()
                if self.botonBN.winfo_ismapped():
                    self.capas(0)

            if self.botonOr.winfo_ismapped():
                self.operacionesLog()
                if self.botonGris.winfo_ismapped():
                    self.capas(0)

            if self.botonTransformaciones2.winfo_ismapped():
                self.transform()

            if self.botonDilatacion.winfo_ismapped():
                self.operacionesMor()

            if self.botonCanny.winfo_ismapped():
                self.deteccionB()

            if self.botonMedia.winfo_ismapped():
                self.filtro()

            if self.botonHSV.winfo_ismapped():
                self.metEspaciosColor()

    

    def deteccionB(self):
        if self.botonCanny.winfo_ismapped():
            self.botonCanny.pack_forget()
            self.botonSobel.pack_forget()
            self.botonPrewitt.pack_forget()
            self.botonGauss.pack_forget()
        else:
            self.botonCanny.pack(fill="x", after=self.boton_menuBordes)
            self.botonSobel.pack(fill="x", after=self.botonCanny)
            self.botonPrewitt.pack(fill="x", after=self.botonSobel)
            self.botonGauss.pack(fill="x", after=self.botonPrewitt)

            if self.botonSuma.winfo_ismapped():
                self.operacionesAl()
                if self.botonBN.winfo_ismapped():
                    self.capas(0)

            if self.botonOr.winfo_ismapped():
                self.operacionesLog()
                if self.botonGris.winfo_ismapped():
                    self.capas(0)

            if self.botonTransformaciones2.winfo_ismapped():
                self.transform()

            if self.botonDilatacion.winfo_ismapped():
                self.operacionesMor()

            if self.botonUmbralBasico.winfo_ismapped():
                self.umbral()
                if self.botonColor2.winfo_ismapped():
                    self.capas2(0)

            if self.botonMedia.winfo_ismapped():
                self.filtro()

            if self.botonHSV.winfo_ismapped():
                self.metEspaciosColor()

    def transH(self):
        self.operac = 20
        self.paneles(0)
    
    def metMedia(self):
        self.operac = 25
        self.paneles(0)
        
    def metMediana(self):
        self.operac = 26
        self.paneles(0)

    def kmean(self):
        self.operac = 28
        self.paneles(0)

    def metOTSU(self):
        self.operac = 19
        self.paneles(0)
    
    def negativoImg(self):
        self.operac = 9
        self.paneles(0)

    def trans2(self):
        self.operac = 10
        self.paneles(0)
    
    def metShearV(self):
        self.operac = 12
        self.paneles(0)
    
    def metShearH(self):
        self.operac = 13
        self.paneles(0)
    
    def metXor(self):
        self.operac = 8
        self.paneles(0)
    
    def convertirGris(self):
        self.operac = 29
        self.paneles(0)
    
    def metEspejo(self):
        self.operac = 11
        self.paneles(0)

    def segB(self):
        self.operac = 27
        self.paneles(0)

    def metCanny(self):
        self.operac = 21
        self.paneles(0)
    
    def metSobel(self):
        self.operac = 22
        self.paneles(0)

    def metPrewitt(self):
        self.operac = 23
        self.paneles(0)

    def metGauss(self):
        self.operac = 24
        self.paneles(0)

    def metHistograma(self):
        self.operac = 30
        self.paneles(0)
    
    def metRelleno(self):
        self.operac = 35
        self.paneles(0)

    def metEsqueleto(self):
        self.operac = 36
        self.paneles(0)

    def metEsqueleto2(self):
        self.operac = 37
        self.paneles(0)

    def metMomentosHU(self):
        self.operac = 38
        self.paneles(0)

    def metTopHat(self):
        self.operac = 39
        self.paneles(0)

    def metBlackHat(self):
        self.operac = 40
        self.paneles(0)
    
    def metHSV(self):
        self.operac = 41
        self.paneles(0)
    
    def metRGB(self):
        self.operac = 42
        self.paneles(0)
    
    def metMVK(self):
        self.operac = 43
        self.paneles(0)
    
    


    def paneles (self, ident):
        if ident == 1:
            self.identificador=1
        elif ident == 2:
            self.identificador=2
        elif ident == 3:
            self.identificador=3
        else:
            self.identificador=0
        if self.operac == 5 or self.operac == 6 or self.operac == 7 or self.operac == 8 or  self.operac == 1 or self.operac == 2 or self.operac == 29:
            plRSC = panelRSC()
            plRSC.crearPanel1(self.ventana, self.menu_lateral,self.operac,self.identificador)
        if self.operac == 3 or self.operac == 4:
            plMD = panelMD()
            plMD.crearPanel1(self.ventana, self.menu_lateral,self.operac,self.identificador)
        if self.operac == 38  or self.operac == 31  or self.operac == 32 or self.operac == 33 or self.operac == 34 or self.operac == 35 or self.operac == 36 or self.operac == 37 or self.operac == 39 or self.operac == 40 or self.operac == 9 or self.operac == 10 or self.operac == 20 or self.operac == 21 or self.operac == 22 or self.operac == 23 or self.operac == 24 or self.operac == 25 or self.operac == 26 or self.operac == 28  or self.operac == 14 or self.operac == 15 or self.operac == 19 or self.operac == 12  or self.operac == 13 or self.operac == 16 or self.operac == 17  or self.operac == 18 or self.operac == 30:
            plMMK = panelMMK()
            plMMK.crearPanel1(self.ventana, self.menu_lateral,self.operac,self.identificador)
        if self.operac == 11 or self.operac == 27 or self.operac == 41 or self.operac == 42 or self.operac == 43:
            plSE = panelSE()
            plSE.crearPanel1(self.ventana, self.menu_lateral,self.operac)
        
        
        
    def filtro(self):
        if self.botonMedia.winfo_ismapped():
            self.botonMedia.pack_forget()
            self.botonMediana.pack_forget()
        else:
            self.botonMedia.pack(fill="x", after=self.boton_menuFiltros)
            self.botonMediana.pack(fill="x", after=self.botonMedia)

            if self.botonSuma.winfo_ismapped():
                self.operacionesAl()
                if self.botonBN.winfo_ismapped():
                    self.capas(0)

            if self.botonOr.winfo_ismapped():
                self.operacionesLog()
                if self.botonGris.winfo_ismapped():
                    self.capas(0)

            if self.botonTransformaciones2.winfo_ismapped():
                self.transform()

            if self.botonDilatacion.winfo_ismapped():
                self.operacionesMor()

            if self.botonUmbralBasico.winfo_ismapped():
                self.umbral()
                if self.botonColor2.winfo_ismapped():
                    self.capas2(0)

            if self.botonCanny.winfo_ismapped():
                self.deteccionB()

            if self.botonHSV.winfo_ismapped():
                self.metEspaciosColor()

    def metEspaciosColor(self):
        if self.botonHSV.winfo_ismapped():
            self.botonHSV.pack_forget()
            self.botonRGB.pack_forget()
            self.botonMVK.pack_forget()
        else:
            self.botonHSV.pack(fill="x", after=self.boton_menuEspaciosColor)
            self.botonRGB.pack(fill="x", after=self.botonHSV)
            self.botonMVK.pack(fill="x", after=self.botonRGB)

            if self.botonSuma.winfo_ismapped():
                self.operacionesAl()
                if self.botonBN.winfo_ismapped():
                    self.capas(0)

            if self.botonOr.winfo_ismapped():
                self.operacionesLog()
                if self.botonGris.winfo_ismapped():
                    self.capas(0)

            if self.botonTransformaciones2.winfo_ismapped():
                self.transform()

            if self.botonDilatacion.winfo_ismapped():
                self.operacionesMor()

            if self.botonUmbralBasico.winfo_ismapped():
                self.umbral()
                if self.botonColor2.winfo_ismapped():
                    self.capas2(0)

            if self.botonCanny.winfo_ismapped():
                self.deteccionB()

            if self.botonMedia.winfo_ismapped():
                self.filtro()
    

    def __init__(self):
        # Crear una instancia de la ventana
        self.ventana = tk.Tk()
        colorFondo = (100, 100, 100)

        # Conversion hexadecimal
        colorF = "#{:02x}{:02x}{:02x}".format(*colorFondo)
        # Configuracion de fondo
        self.ventana.configure(bg="#F9E1E0")

        # Configurar el título de la ventana
        self.ventana.title("Mi Aplicación")

        # Configurar el tamaño de la ventana
        self.ventana.geometry("1200x700")

        boton = tk.Button(self.ventana, text="MENU", command=self.toggle_panel,width=27, height=2, bg="#BC85A3")
        boton.pack()
        boton.place(x=0, y=0)

        # Menú lateral
        self.menu_lateral = tk.Frame(self.ventana)

        # No lo desplegamos inicialmente
        self.menu_lateral.place_forget()

        #--------------------------------------------------------------
        #------------------------Botones de capas----------------------        
        self.botonGris = tk.Button(self.menu_lateral, text="GRISES",command=lambda:self.paneles(1), bg="#FEC2B9")
        self.botonBN = tk.Button(self.menu_lateral, text="BLANCO Y NEGRO",command=lambda:self.paneles(2), bg="#FEC2B9")
        self.botonColor = tk.Button(self.menu_lateral, text="COLOR!",command=lambda:self.paneles(3), bg="#FEC2B9")

        self.botonGris2 = tk.Button(self.menu_lateral, text="GRISES",command=lambda:self.paneles(1), bg="#FEC2B9")
        self.botonColor2 = tk.Button(self.menu_lateral, text="COLOR!",command=lambda:self.paneles(3), bg="#FEC2B9")
     
        #--------------------------------------------------------------
        #------------------Operaciones algebraicas---------------------
        self.boton_menuAlg = tk.Button(self.menu_lateral, text="Operaciones Algebraicas",command=self.operacionesAl, bg="#FEADB9")
        self.boton_menuAlg.pack(fill="x")
        self.botonSuma = tk.Button(self.menu_lateral, text="Suma",command=lambda: self.capas(1), bg="#FEADB9")
        self.botonResta = tk.Button(self.menu_lateral, text="Resta",command=lambda: self.capas(2), bg="#FEADB9")
        self.botonMultiplicacion = tk.Button(self.menu_lateral, text="Multiplicacion",command=lambda: self.capas(3), bg="#FEADB9")
        self.botonDivision = tk.Button(self.menu_lateral, text="Division",command=lambda: self.capas(4), bg="#FEADB9")

        #--------------------------------------------------------------
        #--------------------Operaciones Logicas-----------------------
        self.boton_menuLog = tk.Button(self.menu_lateral, text="Operaciones Logicas",command=self.operacionesLog, bg="#9799BA")
        self.boton_menuLog.pack(fill="x")
        self.botonAnd = tk.Button(self.menu_lateral, text="AND",command=lambda: self.capas(5), bg="#97ADBA")
        self.botonOr = tk.Button(self.menu_lateral, text="OR",command=lambda: self.capas(6), bg="#97ADBA")
        self.botonNot = tk.Button(self.menu_lateral, text="NOT",command=lambda: self.capas(7), bg="#97ADBA")
        self.botonXor = tk.Button(self.menu_lateral, text="XOR",command= lambda: self.capas(8), bg="#97ADBA")

        #--------------------------------------------------------------
        #--------------------Negativo de imagen------------------------
        self.boton_menuNeg = tk.Button(self.menu_lateral, text="Negativo de imagen",command=lambda: self.capas(9), bg="#9799BA")
        self.boton_menuNeg.pack(fill="x")
        
        #--------------------------------------------------------------
        #----------------------Transformaciones------------------------
        self.boton_menuTrans = tk.Button(self.menu_lateral, text="Transformaciones",command=self.transform, bg="#9799BA")
        self.boton_menuTrans.pack(fill="x")
        self.botonTransformaciones2 = tk.Button(self.menu_lateral, text="Transformaciones 2.0",command=self.trans2, bg="#97ADBA")
        self.botonEspejo = tk.Button(self.menu_lateral, text="Espejo",command=self.metEspejo, bg="#97ADBA")
        self.botonShearV = tk.Button(self.menu_lateral, text="Shear vertical",command=self.metShearV, bg="#97ADBA")
        self.botonShearH = tk.Button(self.menu_lateral, text="Shear horizontal",command=self.metShearH, bg="#97ADBA")


        #--------------------------------------------------------------
        #------------------Operaciones morfologicas--------------------
        self.boton_menuMorf = tk.Button(self.menu_lateral, text="Operaciones Morfologicas",command=self.operacionesMor, bg="#FEADB9")
        self.boton_menuMorf.pack(fill="x")
        self.botonDilatacion = tk.Button(self.menu_lateral, text="Dilatacion",command=lambda: self.capas2(14), bg="#FEADB9")
        self.botonErosion = tk.Button(self.menu_lateral, text="Erosion",command=lambda: self.capas2(15), bg="#FEADB9")
        self.botonApertura = tk.Button(self.menu_lateral, text="Apertura",command=lambda: self.capas2(31), bg="#FEADB9")
        self.botonClausura = tk.Button(self.menu_lateral, text="Clausura",command=lambda: self.capas2(32), bg="#FEADB9")
        self.botonGradiente = tk.Button(self.menu_lateral, text="Gradiente",command=lambda: self.capas2(33), bg="#FEADB9")
        self.botonPerimetro = tk.Button(self.menu_lateral, text="Perimetro",command=lambda: self.capas2(34), bg="#FEADB9")
        self.botonRelleno = tk.Button(self.menu_lateral, text="Relleno",command=self.metRelleno, bg="#FEADB9")
        self.botonEsqueleto = tk.Button(self.menu_lateral, text="Esqueleto",command=self.metEsqueleto, bg="#FEADB9")

        #-----------------------------------------------------------------
        #---------------------------Esqueleto 2---------------------------
        self.boton_menuEsqueleto2 = tk.Button(self.menu_lateral, text="Esqueleto 2",command=self.metEsqueleto2, bg="#9799BA")
        self.boton_menuEsqueleto2.pack(fill="x")


        #--------------------------------------------------------------
        #----------------------------Umbrales---------------------------
        self.boton_menuUmbral = tk.Button(self.menu_lateral, text="Umbrales",command=self.umbral, bg="#9799BA")
        self.boton_menuUmbral.pack(fill="x")
        self.botonUmbralBasico = tk.Button(self.menu_lateral, text="Umbral basico",command=lambda: self.capas2(16), bg="#97ADBA")
        self.botonUmbralPorN = tk.Button(self.menu_lateral, text="Umbral por nivel",command=lambda: self.capas2(17), bg="#97ADBA")
        self.botonUmbral2P = tk.Button(self.menu_lateral, text="Umbral a 2 puntos",command=lambda: self.capas2(18), bg="#97ADBA")
        self.botonUmbralOTSU = tk.Button(self.menu_lateral, text="OTSU", command=self.metOTSU, bg="#97ADBA")
        
        #--------------------------------------------------------------
        #--------------------Transformada de Hough------------------------
        self.boton_menuTransH = tk.Button(self.menu_lateral, text="Transformada de Hough",command=self.transH, bg="#9799BA")
        self.boton_menuTransH.pack(fill="x")

        #--------------------------------------------------------------
        #-----------------------Deteccion de bordes--------------------
        self.boton_menuBordes = tk.Button(self.menu_lateral, text="Deteccion de bordes",command=self.deteccionB, bg="#9799BA")
        self.boton_menuBordes.pack(fill="x")
        self.botonCanny = tk.Button(self.menu_lateral, text="Canny",command=self.metCanny, bg="#97ADBA")
        self.botonSobel = tk.Button(self.menu_lateral, text="Sobel",command=self.metSobel, bg="#97ADBA")
        self.botonPrewitt = tk.Button(self.menu_lateral, text="Prewitt",command=self.metPrewitt, bg="#97ADBA")
        self.botonGauss = tk.Button(self.menu_lateral, text="Gaus",command=self.metGauss, bg="#97ADBA")

        #--------------------------------------------------------------
        #-------------------------Filtros------------------------------
        self.boton_menuFiltros = tk.Button(self.menu_lateral, text="Filtros",command=self.filtro, bg="#9799BA")
        self.boton_menuFiltros.pack(fill="x")
        self.botonMedia = tk.Button(self.menu_lateral, text= "Media", command= self.metMedia, bg="#C7A2E4")
        self.botonMediana = tk.Button(self.menu_lateral, text= "Mediana", command= self.metMediana, bg="#EFB79C")
        
        #--------------------------------------------------------------
        #------------------Segmentacion de bordes----------------------
        self.boton_menuSegmentacionB = tk.Button(self.menu_lateral, text="Segmentacion de bordes",command=self.segB, bg="#9799BA")
        self.boton_menuSegmentacionB.pack(fill="x")
    
        #--------------------------------------------------------------
        #--------------------------Kmeans------------------------------
        self.boton_menuKmeans = tk.Button(self.menu_lateral, text="Kmeans",command=self.kmean, bg="#9799BA")
        self.boton_menuKmeans.pack(fill="x")
        
        #--------------------------------------------------------------
        #----------------------Convertir a gris------------------------
        self.boton_menuConvertirG = tk.Button(self.menu_lateral, text="Convertir a gris",command=self.convertirGris, bg="#9799BA")
        self.boton_menuConvertirG.pack(fill="x")

        #--------------------------------------------------------------
        #----------------------/////Histogramas------------------------
        self.boton_menuHistograma = tk.Button(self.menu_lateral, text="Histogramas", command=lambda: self.capas2(30), bg="#9799BA")
        self.boton_menuHistograma.pack(fill="x")

        #--------------------------------------------------------------
        #----------------------/////Momentos HU------------------------
        self.boton_menuMomentosHU = tk.Button(self.menu_lateral, text="Momentos HU", command=self.metMomentosHU, bg="#9799BA")
        self.boton_menuMomentosHU.pack(fill="x")

        #--------------------------------------------------------------
        #----------------------/////TopHat------------------------
        self.boton_menuTopHat = tk.Button(self.menu_lateral, text="TopHat", command=self.metTopHat, bg="#9799BA")
        self.boton_menuTopHat.pack(fill="x")

        #--------------------------------------------------------------
        #----------------------/////BlackHat------------------------
        self.boton_menuBlackHat = tk.Button(self.menu_lateral, text="BlackHat", command=self.metBlackHat, bg="#9799BA")
        self.boton_menuBlackHat.pack(fill="x")

        #--------------------------------------------------------------
        #----------------------/////EspaciosColor------------------------
        self.boton_menuEspaciosColor = tk.Button(self.menu_lateral, text="Espacios de color", command=self.metEspaciosColor, bg="#9799BA")
        self.boton_menuEspaciosColor.pack(fill="x")
        self.botonHSV = tk.Button(self.menu_lateral, text="HSV",command=self.metHSV, bg="#97ADBA")
        self.botonRGB = tk.Button(self.menu_lateral, text="RGB",command=self.metRGB, bg="#97ADBA")
        self.botonMVK = tk.Button(self.menu_lateral, text="MVK",command=self.metMVK, bg="#97ADBA")
    

        # Ejecutar el bucle principal de la aplicación para que la ventana sea visible
        self.ventana.mainloop()

# Aquí inicia la ejecución del programa
if __name__ == "__main__":
    interfaz()
