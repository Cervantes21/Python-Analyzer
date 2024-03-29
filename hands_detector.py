import cv2
import mediapipe as mp

# Importamos las Librerías a usar.

mp_drawing = mp.solutions.drawing_utils  # Dibuja los resultados de las detecciones.
mp_hands = mp.solutions.hands  # Es un modelo para la detección de las manos.

# Llamamos a los métodos de mediapipe.

cap = cv2.VideoCapture(0)  # Para hacer uso de la webcam.

with mp_hands.Hands(
    # Entramos a la configuración de mediapipe-hands.
    static_image_mode=False,  # Puede tener valores de True, o False. False para Streaming y True para imágenes estáticas, o cambiantes.
    max_num_hands=2,  # El número máximo de manos a detectar.
    min_detection_confidence=0.5  # Valor mínimo de confianza. Nos ayuda a saber si la detección es exitosa.
) as hands:
    while True:
        # Comenzamos con el ciclo para leer los fotogramas.
        ret, frame = cap.read()
        if not ret:
            break

        height, width, _ = frame.shape  # Pedimos el alto y ancho del fotograma.
        frame = cv2.flip(frame, 1)  # Lo volteamos para efecto tipo espejo.

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Transformamos los fotogramas a RGB.

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

        cv2.imshow("Frame", frame)  # Mostramos el vídeo.
        q = cv2.waitKey(1)
        if q == 27:  # 27 es el valor ASCII para ESC.
            break  # Función para salir de la aplicación con Esc.

cap.release()
#cv2.destroyAllWindows()

# import cv2
# import mediapipe as mp

# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# with mp_hands.Hands(
#     static_image_mode=False,
#     max_num_hands=2,
#     min_detection_confidence=0.5
# ) as hands:
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         height, width, _ = frame.shape
#         frame = cv2.flip(frame, 1)
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         results = hands.process(frame_rgb)

#         if results.multi_hand_landmarks is not None:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(
#                     frame,
#                     hand_landmarks,
#                     mp_hands.HAND_CONNECTIONS
#                 )

#         cv2.imshow("Frame", frame)
#         q = cv2.waitKey(1)
#         if q == 27:
#             break

#         # Puntos de control:
#         print("Number of hands detected:", len(results.multi_hand_landmarks))
#         if results.multi_hand_landmarks:
#             for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
#                 print(f"Hand {i+1} landmarks:")
#                 for idx, landmark in enumerate(hand_landmarks.landmark):
#                     print(f"Landmark {idx}: ({landmark.x}, {landmark.y}, {landmark.z})")

# cap.release()
# cv2.destroyAllWindows()