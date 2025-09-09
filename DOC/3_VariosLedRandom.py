import pyfirmata        # nos permite hacer la conexion y mandandar los datos a la tarjeta arduino
import time             # proporciona varias funciones relacionadas con el tiempo
import random  # Este módulo implementa generadores de números pseudoaleatorios para varias distribuciones.

board =pyfirmata.Arduino('COM6') #puerto del Arduino

while True: #ciclo infito
    led=random.randint(5,10)    # genera numeros al azar de los pines del 5 al 10
    board.digital[led].write(1) # hacemos uso de lo que esta en la variable "led" para luego encender dicha variable
    time.sleep(.3)              # 3mili[seg] de led encendido,nos permite detener el tiempo
    board.digital[led].write(0) # hacemos uso de lo que esta en la variable "led" para luego apagar dicha variable
    time.sleep(.3)              # 3mili[seg] de led apagado,nos permite detener el tiempo
    