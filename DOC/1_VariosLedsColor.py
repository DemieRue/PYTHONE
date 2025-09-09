import pyfirmata  # nos permite hacer la conexion y mandandar los datos a la tarjeta arduino
import time       # proporciona varias funciones relacionadas con el tiempo

board =pyfirmata.Arduino('COM6') # puerto del Arduino 

while True:  #ciclo infito
    #Leds rojos
    board.digital[5].write(1) # puerto 5 con salida de encendido
    board.digital[8].write(1) # puerto 8 con salida de encendido
    time.sleep(1)             # un segundo de led encendido,nos permite detener el tiempo
    board.digital[5].write(0) # puerto 5 con salida de apagado
    board.digital[8].write(0) # puerto 8 con salida de apagado

    #Leds amarillos
    board.digital[9].write(1)
    board.digital[6].write(1)
    time.sleep(1)
    board.digital[9].write(0)
    board.digital[6].write(0)

    #Leds verdes
    board.digital[10].write(1)
    board.digital[7].write(1)
    time.sleep(1)
    board.digital[10].write(0)
    board.digital[7].write(0)

