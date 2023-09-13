# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:55:13 2023

@author: Camille Gontier
"""

# Packages ####################################################################

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
# %matplotlib qt

# Parameters ##################################################################

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 15}
matplotlib.rc('font', **font)

# Fig 3 #######################################################################

input_files = ["flight1.csv","flight2.csv"]

fig,ax = plt.subplots(figsize=(6, 4), tight_layout=True)

for flight_idx,input_file in enumerate(input_files):
    data = pd.read_csv(input_file,sep=';', decimal=",")
    altitude = data.loc[:,"_12"].values
    time = data.loc[:,"timestamp"].values*1e-3
    time = time - time[0]
    ax.plot(time,altitude,label='Flight ' + str(flight_idx+1))
    ax.legend()
    ax.set_xlabel('Flight time [s]')
    ax.set_ylabel('Altitude [m]')
ax.grid()
plt.savefig("Figure_3.png", dpi=300)

# Fig 4 #######################################################################

fig,ax = plt.subplots(2,figsize=(6, 4), tight_layout=True)

input_file = "flight2.csv"
data = pd.read_csv(input_file,sep=';', decimal=",")
altitude = data.loc[:,"_12"].values
time = data.loc[:,"timestamp"].values*1e-3
a_z = data.loc[:,"_3"].values
time = time - time[0]

ax[0].plot(time,altitude)
ax[0].set_ylabel('Altitude [m]')
ax[1].plot(time[::5],a_z[::5],label='IMU')
ax[1].set_xlabel('Flight time [s]')
ax[1].set_ylabel('Acceleration [g]')
plt.setp(ax[0].get_xticklabels(), visible=False) 
ax[0].grid()
ax[1].grid()

z = []
t = []
input_file = "g-Force Recorder 2023-Sep-06 12 24 08 (12m) .txt"
with open(input_file) as f:
    next(f)
    for line in f:
        z.append(-float(line.strip().split(',')[-1])/981)
        t.append(float(line.strip().split(',')[0])*0.001)
t = np.array(t)

# Origin alignment
t = t-94.5

ax[1].plot(t,z,linestyle='--',label='Smartphone')
plt.setp(ax, xlim=(156,236))
ax[0].set_ylim([1100,1500])
ax[1].set_ylim([-0.5,4])
ax[1].legend()
plt.savefig("Figure_4.png", dpi=300)

# Fig 5 #######################################################################

input_file = "flight2.csv"

fig,ax = plt.subplots(3,figsize=(6, 4), tight_layout=True)

data = pd.read_csv(input_file,sep=';', decimal=",")
time = data.loc[:,"timestamp"].values*1e-3
time = time - time[0]
gx = data.loc[:,"_4"].values
gy = data.loc[:,"_5"].values
gz = data.loc[:,"_6"].values

ax[0].plot(time,gx)
ax[1].plot(time,gy)
ax[2].plot(time,gz)

ax[2].set_xlabel('Flight time [s]')
ax[1].set_ylabel(r'Angular velocity [$rad \cdot s^{-1}$]')
      
ax[0].grid()
ax[1].grid()
ax[2].grid()

plt.setp(ax[0].get_xticklabels(), visible=False) 
plt.setp(ax[1].get_xticklabels(), visible=False) 

plt.savefig("Figure_5.png", dpi=300)




       
