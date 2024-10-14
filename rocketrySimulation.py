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

#Funcion para obtener la gravedad con respecto a la altura
def gravedad(h):
    return g0 * (R / (R + h))**2

#Función para calcular la fuerza de resistencia del aire en función de la velocidad del coehete
#La resistencia aumenta con el cuadrado de la velocidad
def resistencia(v):
    return 0.5 * c_d * A * rho * v**2

#-----------------------Simulación
t = 0 #t0
dt = 0.1 #Paso de tiempo
h = 0 #h0
v = v0 #v0
x = 0 #pos horizontal
y = 0 #pos vertical

#Listas para almacenar valores
tiempos = []
alturas = []
posiciones_x = []