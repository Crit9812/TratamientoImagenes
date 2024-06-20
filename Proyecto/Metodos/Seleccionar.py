import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class seleccion:
    def evento_seleccionar(self):
        archivo = filedialog.askopenfilename()
        nombre = os.path.basename(archivo)
        return archivo