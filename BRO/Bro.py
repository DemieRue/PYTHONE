import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import numpy as np


def getSerialData(self,Samples,numData,serialConnection, lines):
    for i in range(numData):
        value  = float(serialConnection.readline().strip())  
        data[i].append(value)
        lines[i].set_data(range(Samples),data[i]) 

        
serialPort = 'COM7' 
baudRate = 9600  

try:
  serialConnection = serial.Serial(serialPort, baudRate) 
except:
  print('Cannot conect to the port')

Samples = 100  
sampleTime = 150  
numData = 4



xmin = 0
xmax = Samples
ymin = [0, 0 , -100 ,0]
ymax = [5.5, 5.5 , 100 , 100]
lines = []
data = []

for i in range(numData):
    data.append(collections.deque([0] * Samples, maxlen=Samples))
    lines.append(Line2D([], [], color='#FF0000'))
  
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1,xlim=(xmin, xmax), ylim=(ymin[0] , ymax[0]))
ax1.title.set_text('OSCILOSCOPIO')
ax1.set_xlabel("TIEMPO")
ax1.set_ylabel("VOLTAJE")
ax1.add_line(lines[0])
    
anim = animation.FuncAnimation(fig,getSerialData, fargs=(Samples,numData,serialConnection,lines), interval=sampleTime)
plt.show()

serialConnection.close()