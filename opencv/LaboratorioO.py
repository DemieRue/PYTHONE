import cv2
import mediapipe as mp
import numpy as np
from math import acos,degrees #util para calcular el arco coseno

#librearias comunicacion serial
import serial
import time

R=0   #para restringir el uso y error de lectura de datos
texto=texto1=texto2="" #nos permitira utilizar texto para escribir en pantalla
texto4=texto5=texto6=""
m=[2,2,2,2,2,2]  #define el tamaño del borde de los cuadros que muestran en pantalla
#ard=serial.Serial('COM3')
#time.sleep(2)
##calculamos el centro de la palma
def palm_centroid(coordinates_list):
    coordinates=np.array(coordinates_list)   #convertimos en un arreglo
    centroid=np.mean(coordinates,axis=0)    #eje 0 como media para calcular la media de las coordinadas
    centroid=int(centroid[0]),int(centroid[1])  #coordenaDAS EN ENTEROS
    return centroid   #resultado dela funcion calculado
mp_drawing=mp.solutions.drawing_utils   #funcion para dibujar o visulizar video
mp_drawing_styles=mp.solutions.drawing_styles #permite defiunir colores y espesores de linea
mp_hands=mp.solutions.hands      #modelos y metodos y seguimiento de manos en el video
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)  #TOMAMAMOS LA CAPTURA CON 0 DE LA CAMARA DE LA COMPUTADOTA

#DEFINIMOS QUE DEDOS ESTAN LEVANTADOS
ROJO=np.array([True,True,True,True,False])  #encender foco rojo
VERDE=np.array([True,True,True,False,False])  #encender foco verde
AZUL=np.array([True,True,False,True,False])  #encender foco  azul

#pulgar
thump_points=[1,2,4]  #puntos de referencia del pulgar
#indice, medio,anular y meñique
palm_points=[0,1,2,5,9,13,17]  #puntos de referencia de la palma
fingertips_points=[8,12,16,20]
finger_base_points=[6,10,14,18]#puntos de referencia de los dedos
#colores
VERDE=(48,255,48)  #DEFINE COLOR VERDE CON RGB
AZUL=(192,101,21)
ROJO=(255,165,255)

with mp_hands.Hands (model_complexity=1,max_num_hands=1,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands 

    while True:
        ret,frame=cap.read()   #leemos el video se le asigna una trama
        if ret==False:         #comprueba si fallo la lectura
            break
        frame=cv2.flip(frame,1)   #reflejar el video
        height,width,_=frame.shape   #obtener las dimenciones de lectura y ancho del fotograma
        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  #CAMBIAMOS A RGB PARA EL TRABAJO CON MEDIAPIPE
        results=hands.process(frame_rgb)
        fingers_counter="_"   #contador de dedos inicializando
        if results.multi_hand_landmarks:
            coordinates_thumb=[]   #lista vacia para cecibir puntos de referencia de pulgar
            coordinates_palm=[]
            coordinates_ft=[]   #lista vacia de dedos
            coordinates_fb=[]    #base de dedos
            
            for hand_landmarks in results.multi_hand_landmarks:
                for index in thumb_points:
                    x=int(hand_landmarks.landmark[index].x*width)  #obtenemos posicion de x
                    y=int(hand_landmarks.landmark[index].y*height)  #obtenemos posicion de y
                    coordinates_thumb.append([x,y])   #coordenadas de punto de referencia
                    for index in palm_points:
                        x=int(hand_landmarks.landmark[index].x*width)
                        y=int(hand_landmarks.landmark[index].y*height)
                        coordinates_palm.append([x,y])
                    for index in fingertips_points:
                        x=int(hand_landmarks.landmark[index].x*width)
                        y=int(hand_landmarks.landmark[index].y*height)
                        coordinates_ft.append([x,y])
                    for index in finger_base_points:
                        x=int(hand_landmarks.landmark[index].x*width)
                        y=int(hand_landmarks.landmark[index].y*height)
                        coordinates_fb.append([x,y])
                    #pulgar
                    p1=np.array(coordinates_thumb[0]) #arreglo del primer punto de referencia
                    p2=np.array(coordinates_thumb[1])
                    p3=np.array(coordinates_thumb[2])

                    l1=np.linalg.norm(p2-p3)   #calcula la longitud de p2 y p3
                    l2=np.linalg.norm(p1-p3)
                    l3=np.linalg.norm(p1-p2)
                    #calcular el angulo
                    angle=np.degrees(np.arccos((l1**2+l3**2-l2**2)/(2*l1*l3)))
                    thumb_finger=np.array(False)  #indica que el pulgar nop esta extendido
                    if angle>150:
                        thumb_finger=np.array(True)   #el pulgar esta extendido
                        nx,ny=palm_centroid(coordinates_palm)
                        cv2.circle(frame,(nx,ny),3,(0,255,0),2)  #dibuja un punto centro en la palma
                        coordinates_centroid=np.array([nx,ny])
                        coordinates_ft=np.array(coordinates_ft)
                        coordinates_fb=np.array(coordinates_fb)
                        #distancias
                        
                    
            
            
            
