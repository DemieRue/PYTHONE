import cv2
import mediapipe as mp
import serial

# Configuración de la comunicación serial con Arduino
arduino = serial.Serial('COM5', 9600)  # Reemplaza 'COM3' con el puerto correspondiente
arduino.timeout = 1

# Configuración de MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Configuración de la cámara
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convertir el frame a RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detectar las manos en la imagen
        results = hands.process(image)

        # Contar los dedos levantados
        finger_count = 0
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                for finger in mp_hands.HandLandmark:
                    landmark = hand_landmarks.landmark[finger]
                    if landmark.y < hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y:
                        finger_count += 1

        # Enviar el conteo de dedos a Arduino
        arduino.write(f"{finger_count}\n".encode())

        # Mostrar la imagen con los landmarks y el conteo de dedos
        cv2.putText(image, f"Finger Count: {finger_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Hand Tracking', image)

        # Salir si se presiona 'q'
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
arduino.close()