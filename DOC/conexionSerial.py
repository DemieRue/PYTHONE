import serial # librería de python que permite comunicarse a través de comunicaciones por serial
import time   # proporciona varias funciones relacionadas con el tiempo

# ard del puerto serial,puerto del arduino 'com6'y le velocidad de lectura o la tx de datos a 9600 Baudios
ard =serial.Serial('COM6',9600) 
datos=ard.readline() # lectura de datos

while 1: #bucle infinito
    print(datos.decode('utf-8')) # eliminamos saltos de linea con decode'utf-8'
    time.sleep(1)                # tiempo de duracion
    

