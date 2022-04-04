# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 20:15:48 2022

@author: johnf
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.close("all")
df=pd.read_csv("data1.txt",names=["x","y"])
df.info()

m=len(df) #Número de muestras

plt.plot(df["x"],df["y"],"+")
plt.xlabel("x")
plt.ylabel("y")

th0= 0
th1= 0
x=np.arange(0,22.5,0.5)
h=th0+th1*x
plt.plot(x,h)
plt.close("all")

th0a=np.arange(-20,20,1) 
th1a=np.arange(-20,20,.5) 
"""
thi=-100; thf=100; # dominio
delta=5
th0a=np.arange(thi,thf,delta) 
th1a=np.arange(thi,thf,delta) 
"""
SME=np.zeros(shape=[len(th0a),len(th1a)])
i=0
j=0
for th0 in th0a:
    for th1 in th1a:
        SME[i][j]=1/(2*m)*sum(((th0+th1*df["x"])-df["y"])**2)
        j+=1
        #print(th0)
    j=0
    i+=1

th0m,th1m=np.meshgrid(th0a,th1a)

SME[SME>100]=100 #Como hay un problema de visualización, el error es muy alto en unos extremos, no se observa bien la gráfica
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(th0m,th1m,SME.T,alpha= .7)
ax.contour(th0m,th1m,SME.T,alpha= .7)
ax.set_ylim(-1.5,2.5)
plt.xlabel("th0")
plt.ylabel("th1")

#Implementación de gradiente descendente
th0=5 #Valores arbitarios para empezar el algoritmo
th1=0
th_v=np.array([th0,th1])
alfa=0.02

for i in range(500):
    th_v=th_v-alfa*np.array([1/m*sum(((th_v[0]+th_v[1]*df["x"])-df["y"])), 1/(m)*sum(((th_v[0]+th_v[1]*df["x"])-df["y"])*df["x"])])   
    plt.plot(th_v[0],th_v[1],"ok")
    plt.pause(0.0001)
print(th_v)

#Graficar caminito en la gráfica 3D solo en el piso
#Graficar iteraciones contr thetao y theta1
