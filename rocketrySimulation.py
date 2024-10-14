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
    return 0.5 * C_d * A * rho * v**2

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

#Bluce de simulación
while h >= 0:
    #Guardar los datos en las listas
    tiempos.append(t)
    alturas.append(h)
    posiciones_x.append(x)

    #Calcular fuerzas
    g = gravedad(h) #Gravedad en la altura actual
    F_res = resistencia(v) #F de resistencia del aire

    #Ecuaciones de movimiento para actualizar las variables
    v = v - (g + F_res) * dt 
    h = h + v * np.sin(theta_rad) * dt
    x = x + v * np.cos(theta_rad) * dt #Pos horizontal 
    t += dt

#Graficar
plt.figure()
plt.plot(posiciones_x, alturas)
plt.title("Trayectoria del cohete")
plt.xlabel("Posición horizontal en metros")
plt.ylabel("Altura en metros")
plt.grid()
plt.show() 