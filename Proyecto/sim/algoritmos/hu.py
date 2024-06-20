import numpy as np
from funciones import f
import cv2

class Momentos():

    def huM(image):
        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Calcular momentos de la imagen
        moments = cv2.moments(gray)
        
        # Calcular momentos centrales
        x_bar = moments['m10'] / moments['m00']
        y_bar = moments['m01'] / moments['m00']
        
        # Momentos centrales
        mu_20 = moments['mu20'] / moments['m00'] - x_bar**2
        mu_02 = moments['mu02'] / moments['m00'] - y_bar**2
        mu_11 = moments['mu11'] / moments['m00'] - x_bar * y_bar
        mu_30 = moments['mu30'] / moments['m00'] - 3 * x_bar * mu_20 + 2 * x_bar**3
        mu_03 = moments['mu03'] / moments['m00'] - 3 * y_bar * mu_02 + 2 * y_bar**3
        mu_21 = moments['mu21'] / moments['m00'] - 2 * x_bar * mu_11 - y_bar * mu_20 + 2 * x_bar**2 * y_bar
        mu_12 = moments['mu12'] / moments['m00'] - 2 * y_bar * mu_11 - x_bar * mu_02 + 2 * y_bar**2 * x_bar
        
        # Momentos invariantes a escala, rotación y reflexión
        phi_1 = mu_20 + mu_02
        phi_2 = (mu_20 - mu_02)**2 + 4 * mu_11**2
        phi_3 = (mu_30 - 3 * mu_12)**2 + (3 * mu_21 - mu_03)**2
        phi_4 = (mu_30 + mu_12)**2 + (mu_21 + mu_03)**2
        phi_5 = (mu_30 - 3 * mu_12) * (mu_30 + mu_12) * ((mu_30 + mu_12)**2 - 3 * (mu_21 + mu_03)**2) + \
                (3 * mu_21 - mu_03) * (mu_21 + mu_03) * (3 * (mu_30 + mu_12)**2 - (mu_21 + mu_03)**2)
        phi_6 = (mu_20 - mu_02) * ((mu_30 + mu_12)**2 - (mu_21 + mu_03)**2) + \
                4 * mu_11 * (mu_30 + mu_12) * (mu_21 + mu_03)
        phi_7 = (3 * mu_21 - mu_03) * (mu_30 + mu_12) * ((mu_30 + mu_12)**2 - 3 * (mu_21 + mu_03)**2) - \
                (mu_30 - 3 * mu_12) * (mu_21 + mu_03) * (3 * (mu_30 + mu_12)**2 - (mu_21 + mu_03)**2)
        
        # Hacer los momentos de Hu invariante a escala, rotación y reflexión
        phi_1_inv = -1 * np.sign(phi_1) * np.log10(abs(phi_1))
        phi_2_inv = -1 * np.sign(phi_2) * np.log10(abs(phi_2))
        phi_3_inv = -1 * np.sign(phi_3) * np.log10(abs(phi_3))
        phi_4_inv = -1 * np.sign(phi_4) * np.log10(abs(phi_4))
        phi_5_inv = -1 * np.sign(phi_5) * np.log10(abs(phi_5))
        phi_6_inv = -1 * np.sign(phi_6) * np.log10(abs(phi_6))
        phi_7_inv = -1 * np.sign(phi_7) * np.log10(abs(phi_7))
        
        return phi_1_inv, phi_2_inv, phi_3_inv, phi_4_inv, phi_5_inv, phi_6_inv, phi_7_inv