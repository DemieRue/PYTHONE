import pyfirmata        # nos permite hacer la conexion y mandandar los datos a la tarjeta arduino
import time             # proporciona varias funciones relacionadas con el tiempo

board =pyfirmata.Arduino('COM6') #puerto del Arduino

while True: #ciclo infito
    # ciclo for ,va recorrer todos los leds segun su posicion empieza del 5 y se detendra antes del 11
    for i in range (5,11): 
        board.digital[i].write(1) # hacemos uso de lo que esta en la variable "i" para luego encender dicha variable
        time.sleep(.3)            # 3mili[seg] de led encendido,nos permite detener el tiempo
        board.digital[i].write(0) # hacemos uso de lo que esta en la variable "i" para luego apagar dicha variable
        time.sleep(.3)            # 3mili[seg] de led apagado,nos permite detener el tiempo
        