import cv2
from tkinter import simpledialog
from algoritmos.rellenoBordes import RellenoImagen
from algoritmos.esqueletos2 import Esqueletizador
from algoritmos.conversionesColor import Col
from algoritmos.morfologicas2 import morf2
from algoritmos.transformada import Houhg
from algoritmos.esqueletos import esq
from algoritmos.hu import Momentos
from algoritmos.hatss import Hats
from funciones import f
from tkinter import messagebox


def menu():
    print("Operaciones Morfológicas")
    print("1. COLOR")
    print("   1.1. Apertura")
    print("   1.2. Clausura")
    print("   1.3. Dilatación")
    print("   1.4. Erosión")
    print("   1.5. Gradiente")
    print("   1.6. Perímetro")
    print("2. GRIS")
    print("   2.1. Apertura")
    print("   2.2. Clausura")
    print("   2.3. Dilatación")
    print("   2.4. Erosión")
    print("   2.5. Gradiente")
    print("   2.6. Perímetro")
    print("   2.7. Relleno")
    print("   2.8. Esqueleto 1")
    print("   2.9. Esqueleto 2")
    print("3. Momentos de Hu")
    print("4. Transformada de Hough")
    print("5. Top Hat")
    print("6. Black Hat")
    print("7. Espacios de color")
    print("   7.1. HSV")
    print("   7.2. RGB")
    print("   7.3. CMYK")
    print("0. Salir")

def main():

    arch="patoBin.jpeg"
    ruta="C:\\Users\\naomi\\OneDrive\\Documentos\\Imagenes_Digitales\\Imagenes\\"+arch
    img=cv2.imread(ruta)

    menu()
    choice = input("Selecciona una opción: ")
    
    if choice == "0":
        print("Saliendo...")

    elif choice == "1":
        sub_choice = input("Selecciona una operación de COLOR: ")
        if sub_choice == "1":
            print("Seleccionaste COLOR -> Apertura")
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.aperturaRGB(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "2":

            print("Seleccionaste COLOR -> Clausura")
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.clausuraRGB(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "3":

            print("Seleccionaste COLOR -> Dilatación")
            tam = simpledialog.askinteger("Tamaño Dilatación", "Ingrese el tamaño de la dilatación en pixeles:")
            img11=f.dilatacionRGB(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "4":

            print("Seleccionaste COLOR -> Erosión")
            tam = simpledialog.askinteger("Tamaño Erosión", "Ingrese el tamaño de la erosión en pixeles:")
            img11=f.erosionRGB(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "5":
            print("Seleccionaste COLOR -> Gradiente")
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.gradienteRGB(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "6":
            print("Seleccionaste COLOR -> Perímetro")
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.perimetroRGB(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    elif choice == "2":
        sub_choice = input("Selecciona una operación de GRIS: ")

        if sub_choice == "1":

            print("Seleccionaste GRIS -> Apertura")
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.aperturaGris(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "2":

            print("Seleccionaste GRIS -> Clausura")
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.clausuraGris(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "3":

            print("Seleccionaste GRIS -> Dilatación")
            tam = simpledialog.askinteger("Tamaño Dilatación", "Ingrese el tamaño de la dilatación en pixeles:")
            img11=f.dilatacionGris(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        elif sub_choice == "4":
            
            print("Seleccionaste GRIS -> Erosión")
            tam = simpledialog.askinteger("Tamaño Erosión", "Ingrese el tamaño de la erosión en pixeles:")
            img11=f.erosionGris(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "5":
            print("Seleccionaste GRIS -> Gradiente")
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.gradienteGris(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "6":

            print("Seleccionaste GRIS -> Perímetro")
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=morf2.perimetroGris(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "7":

            print("Seleccionaste GRIS -> Relleno")
            imagenOriginal = cv2.imread(ruta)
            clic = False
            semilla = []
            params = {
                'imagenOriginal': imagenOriginal,
                'imagen': img,
                'clic': clic,
                'semilla': semilla
            }
            cv2.imshow("Imagen Original", imagenOriginal)
            cv2.setMouseCallback("Imagen Original", RellenoImagen.guardarDatosClick, params)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "8":

            print("Seleccionaste GRIS -> Esqueleto Morfológico")
            tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
            img11=esq.esqueletizar(img, tam)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "9":
            print("Seleccionaste GRIS -> Esqueleto No Morfológico")
            img11=Esqueletizador.go(img)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
    elif choice == "3":

        print("Seleccionaste Momentos de Hu")

        img11=f.modificarImg(img, 45, 1.5)

        phi_1, phi_2, phi_3, phi_4, phi_5, phi_6, phi_7 = Momentos.huM(img)
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

        cv2.imshow("imagen transformada", img11)
        cv2.imshow("imagen original", img)
        messagebox.showinfo("Mensaje", texto)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    elif choice == "4":
        print("Seleccionaste Transformada de Hough")
        img2=cv2.imread(ruta)
        img11=Houhg.transformar(img)
        cv2.imshow("imagen resultante", img11)
        cv2.imshow("imagen original", img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == "5":
        print("Seleccionaste Top Hat")
        tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
        img11=Hats.topHat(img, tam)
        cv2.imshow("imagen original", img)
        cv2.imshow("imagen resultante", img11)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == "6":
        print("Seleccionaste Black Hat")
        tam = simpledialog.askinteger("Kernel", "Ingrese el kernel en pixeles:")
        img11=Hats.blackHat(img, tam)
        cv2.imshow("imagen original", img)
        cv2.imshow("imagen resultante", img11)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == "7":
        sub_choice = input("Selecciona un Espacio de color: ")
        if sub_choice == "1":

            print("Seleccionaste HSV")
            img11, p1, p2, p3=Col.BGRaHSV(img)
            res2=Col.HSVaBGR(img11)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.imshow("imagen devuelta", res2)
            cv2.imshow("plano 1", p1)
            cv2.imshow("plano 2", p2)
            cv2.imshow("plano 3", p3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "2":

            print("Seleccionaste RGB")
            img11, p1, p2, p3=Col.BGRaRGB(img)
            res2=Col.RGBaBGR(img11)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.imshow("imagen devuelta", res2)
            cv2.imshow("plano 1", p1)
            cv2.imshow("plano 2", p2)
            cv2.imshow("plano 3", p3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif sub_choice == "3":
            print("Seleccionaste CMYK")
            img11, k, p1, p2, p3=Col.BGRaCMYK(img)
            res2=Col.CMYKaBGR(img11, k)
            cv2.imshow("imagen original", img)
            cv2.imshow("imagen resultante", img11)
            cv2.imshow("imagen devuelta", res2)
            cv2.imshow("plano 1", p1)
            cv2.imshow("plano 2", p2)
            cv2.imshow("plano 3", p3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    else:
        print("Opción no válida, intenta de nuevo.")

    


main()
