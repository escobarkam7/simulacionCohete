import numpy as np
import matplotlib.pyplot as plt

#Declarar constantes
g0 = 9.81 #m/s^2
R = 6371e3 #Radio de la tierra (m)
C_d = .75 #Coeficiente de arrastre
A = 0.01 #Área de la sección transversal del cohete (m^2)
rho = 1.225 #(kg/m^3)

# Parámetros iniciales
v0 = 500  #Velocidad inicial (m/s)
theta = 45  #Ángulo de lanzamiento en grados
theta_rad = np.radians(theta) #Conversión del ángulo a radianes


