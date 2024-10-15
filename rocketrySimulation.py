import numpy as np
import matplotlib.pyplot as plt

#Declarar constantes
g0 = 9.81 #m/s^2
R = 6371e3 #Radio de la tierra (m)
C_d = .75 #Coeficiente de arrastre
A = 0.01 #Área de la sección transversal del cohete (m^2)
rho = 1.225 #(kg/m^3)
m = 1000 #Masa del cohete (kg)

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

#Inicializar componentes de velocidad
vx = v0 * np.cos(theta_rad) #comp hor
vy = v0 * np.sin(theta_rad) #comp ver

#Listas para almacenar valores
tiempos = []
alturas = []
posiciones_x = []

#Bluce de simulación
#Cambiar h a y
while y >= 0: #La simulación acaba cuando el cohete toca el suelo
    #Guardar los datos en las listas
    tiempos.append(t)
    alturas.append(y)
    posiciones_x.append(x)

    #Calcular fuerzas
    g = gravedad(y) #Gravedad en la altura actual
    F_res_x = resistencia(vx) #F de resistencia del aire en x y en y
    F_res_y = resistencia(vy)

    #Ecuaciones de movimiento para actualizar las variables

    #Usando la segunda ley de Newt a = F / m
    a_x = -F_res_x / m #Aceleración en x
    a_y = -g - (F_res_y / m) #Aceleración en y
    #Actualizar componentes de velocidades en función de la aceleración
    vx += a_x * dt
    vy += a_y * dt
    x += vx * dt  #Pos horizontal 
    y += vy * dt  #Pos vertical 
    t += dt

#Graficar
plt.figure()
plt.plot(posiciones_x, alturas)
plt.title("Trayectoria del cohete")
plt.xlabel("Posición horizontal en metros")
plt.ylabel("Altura en metros")
plt.grid()
plt.show() 