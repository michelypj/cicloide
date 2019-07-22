from numpy import array, linspace
from math import*
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint

from vpython import sphere, scene, vector, color, arrow, text, sleep

arrow_size = 1.

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.5

def func (conds, t, g, x): # funcion definida para los valores de theta y omega
    dthe = conds[1]
    dr = conds[3]
    dome = (g/conds[2])*cos(conds[0])-(2*conds[3]/conds[2])*conds[1]
    ddr = conds[2]*conds[1]**2+g*sin(conds[0])
    return array([dthe, dome, dr, ddr], float)


g = 9.81
x=1.
y=(x)**2
thes = atan(y/x) # valores iniciales para theta y omega
omes = 0.
dh =0.
r1= sqrt(x**2+y**2)

initcond = array([thes, omes, r1, dh], float)#arreglos de las condiciones iniciales

n_steps = 1000 #numero de pasos
t_start = 0. #tiempo inicial
t_final = 15.#tiempo final
t_delta = (t_final - t_start) / n_steps #diferencial de tiempo
t = linspace(t_start, t_final, n_steps)#arreglo de diferencial de tiempo

solu, outodeint = odeint( func, initcond, t, args = (g, x), full_output=True) #solucion de la ecuacion diferencial (parametros acordes a los definidos en la funcion)

theta, omega, v, r = solu.T # solucion para cada paso de theta y omega
#print(r)
# =====================

scene.range = 10. # tamaño de la ventana de fondo

xp = r1*cos(thes) #pasa de coordenadas polares a cartesinas
yp = r1*sin(thes)
zp = 0.


sleeptime = 0.0001 # tiempon con el que se utiliza la posicion de la particula

prtcl = sphere(pos=vector(xp,yp,zp), radius=R, color=color.cyan) #define objeto con que se va a trabajar

time_i = 0 #es un contador que se mueve ene el espacio temporal en donde se resolvio la ecuacion deferencial
t_run = 0 #tiempo en el q se ejecuta la animacion

#for i in omega:
#    print(i)
#print(r)

while t_run < t_final: #animacion 
    sleep(sleeptime) 
    prtcl.pos = vector(r[time_i]*cos(theta[time_i]), -(r[time_i]*sin(theta[time_i]))**2, zp )
    
    t_run += t_delta
    time_i += 1

