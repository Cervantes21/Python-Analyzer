# import cv2
# # Importando Librerías.

# face_cascade = cv2.CascadeClassifier('./raw/haarcascade_frontalface_default.xml')
# # Guardamos en una variable nuestra Haarcascade # Yo dejaré la versión por default.

# # face_cascade = cv2.CascadeClassifier('./raw/haarcascade_frontalcatface_extended.xml')
# # Probamos la versión extendida, o por default. Depende de como se comporte tu programa.


# cap = cv2.VideoCapture(0)
# # Hacemos referencia de nuestra web-cam. Canal de referencia 0.

# while True:
# # Comenzamos llamando un ciclo While para analizar los fotogramas.
#     _, img = cap.read()
# # Con la función cap.read() para leer cada uno de los fotogramas del vídeo.

#     img = cv2.flip(img,1)
#     # Aplicamos un efecto espejo.
    
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Convertimos los fotogramas a escala de grises.

#     faces = face_cascade.detectMultiScale(gray, 1.1,4)
# # En la variable faces guardaremos todas las caras que detecte el programa con el metodo detectMultiScale()
# # '''
# # Los dos últimos parametros después de gray, son para ir manejando la escala de grises y como los irá detectando el programa. ['Más información:'](https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81)
# # '''
#     for (x, y, w, h) in faces:
# # (x,y,w,h) son los vertices del cuadrado.
#         cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
# # Luego con la función cv2.rectangle() pintaremos ese cuadro encima de las caras. (255,0,0) se refiere al color del cuadro y el 2 al grosor de la línea.
#     cv2.imshow('img', img)
#     # Utilizamos esta función para mostrar el fotograma ya modificado y con la cara detectada.

#     k = cv2.waitKey(30)
# # Está función nos permite revisar cada 30 milisegundos si se esta presionando alguna tecla. 
#     if k == 27: # 27 es el ascii para Esc
#         break
# cap.release()
# # Para salir del programa y cerrar la cámara web.

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5
) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

        cv2.imshow("Frame", frame)
        q = cv2.waitKey(1)
        if q == 27:
            break

        # Puntos de control:
        print("Number of hands detected:", len(results.multi_hand_landmarks))
        if results.multi_hand_landmarks:
            for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
                print(f"Hand {i+1} landmarks:")
                for idx, landmark in enumerate(hand_landmarks.landmark):
                    print(f"Landmark {idx}: ({landmark.x}, {landmark.y}, {landmark.z})")

cap.release()
cv2.destroyAllWindows()


