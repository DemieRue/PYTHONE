import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands

cap=cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image= cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
        image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=hands.process(image)
        